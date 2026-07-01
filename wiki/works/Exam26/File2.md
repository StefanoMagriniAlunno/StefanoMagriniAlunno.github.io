# AP-PINN for the Jin-Xin Relaxation System: Addressing Spectral Bias, Gradient Pathology, and Shock Discontinuities

## Executive Summary

Training physics-informed neural networks (PINNs) on the Jin-Xin relaxation system — a two-speed hyperbolic system with a stiff source term of order $1/\varepsilon$ that converges to the Burgers equation as $\varepsilon \to 0$ — presents two interacting failure modes: (1) **stiffness-induced gradient pathology**, where the neural tangent kernel (NTK) norm grows as $\mathcal{O}(\varepsilon^{-2})$ as $\varepsilon \to 0$, making gradient-flow dynamics increasingly stiff and poorly conditioned; and (2) **shock-discontinuity failure**, where the strong-form $L^2$ PDE residual is structurally inappropriate near shocks, causing loss stagnation and erroneous solutions. The literature has produced a rich set of techniques organized around five design axes: **(i)** asymptotic-preserving (AP) loss reformulations, **(ii)** relaxation-based network architectures, **(iii)** weak/entropy-based loss formulations, **(iv)** adaptive weighting and NTK-informed balancing, and **(v)** causal/domain-decomposition training strategies. Each addresses a distinct failure mode, and current best practice combines several simultaneously.

***

## 1. The Core Difficulty: Why Standard PINNs Fail

For the Jin-Xin system
$$
\partial_t u + \partial_x v = 0, \quad \varepsilon \partial_t v + \varepsilon A\, \partial_x u = -(v - F(u)),
$$
applying a vanilla PINN with a single network and an $L^2$ PDE loss encounters two catastrophic failures as $\varepsilon \to 0$.

### 1.1 NTK Stiffness and Gradient Pathology

The NTK theory of PINNs (Wang et al., 2022) demonstrates that fully-connected PINNs suffer not only from spectral bias, but also from a *remarkable discrepancy in convergence rates* among the different loss components. For a multiscale BVP with scale parameter $\varepsilon$, it has been proved that the **Frobenius norm of the NTK matrix grows as $\mathcal{O}(1/\varepsilon^2)$** as $\varepsilon \downarrow 0$. This implies that the gradient-flow ODE governing the evolution of training residuals becomes increasingly stiff as scale separation grows. Numerical experiments confirm that, under this regime, gradient descent either requires prohibitively small learning rates (conditional stability) or fails to decrease the loss entirely. Simply rescaling $\mathcal{L}_\text{PDE}$ by $\lambda_\text{PDE} = \varepsilon^2$ to cancel the $1/\varepsilon^2$ factor does **not** resolve the problem: while this changes eigenvalue magnitudes, it does not alter the NTK eigenvalue *distribution*, and spectral bias persists.[^1][^2][^3][^4]

A separate but related issue is **spectral bias** (also called F-principle): standard feedforward networks trained with gradient descent learn low-frequency components of the solution much faster than high-frequency ones. For the Burgers shock, the solution has a steep, localized layer that demands high-frequency content; spectral bias causes the network to converge to a smoothed, physically incorrect solution.[^5][^6]

### 1.2 Strong-Form Loss Breakdown Near Shocks

Near a shock, the strong-form PDE $\partial_t u + \partial_x F(u) = 0$ does not hold in the classical sense — the solution is only a *weak* (distributional) solution. When collocation-based Monte Carlo approximation of the $L^2$ residual is used, the PDE loss **stagnates at a high level** near the shock location, and the absolute error concentrates precisely at $x = x_\text{shock}$. Explicit computations by Chaumet & Giesselmann confirm analytically why the strong-form residual must diverge at shock points for the inviscid Burgers equation. This structural inconsistency is further amplified by the Jin-Xin stiff relaxation term, which introduces an additional implicit layer structure of thickness $\mathcal{O}(\varepsilon)$ around the equilibrium manifold $v = F(u)$.[^7][^8][^9]

***

## 2. AP Loss Formulations and Micro-Macro Decomposition

The most principled solution to the $\varepsilon \to 0$ failure is to redesign the loss function so that it **preserves the asymptotic structure** of the system — i.e., the loss automatically converges to the limiting Burgers loss as $\varepsilon \to 0$.

### 2.1 The APNN Framework (Jin, Ma, Wu — 2023)

The foundational Asymptotic-Preserving Neural Networks (APNN) methodology was developed by Jin, Ma, and Wu for the time-dependent linear transport equation with diffusive scaling. The key insight is that *not all classical AP numerical formats are directly suitable for neural networks*: simply applying a standard AP discretization to the loss can cause the neural network to stagnate at the initial condition in the zero-$\varepsilon$ limit. The APNN is defined by the property that, as $\varepsilon \to 0$, the full-model loss function **converges to the loss of the corresponding reduced-order model** (e.g., the Burgers loss). For the linear transport equation under diffusive scaling, the APNN loss is built from:[^10][^11][^12]
- A **micro-macro decomposition**, introducing odd and even parities as auxiliary networks;
- An explicit **macroscopic moment equation** embedded in the loss, ensuring that the conservation of mass (or momentum/energy for nonlinear problems) is actively enforced and not merely constrained as a soft penalty;
- **Boundary condition enforcement** through hard constraints rather than soft penalties, which was found to be critical for accurate inflow boundary layers.[^11]

The AP property is verified formally by sending $\varepsilon \to 0$ in the loss expression and showing that it reduces to the diffusion-limit loss.[^12][^11]

### 2.2 MA-APNN: Macroscopic Auxiliary AP Networks (Li et al. — 2024)

Li, Jiang, Sun, Xu, and Zhou (arXiv:2403.01820, 2024) developed the **Macroscopic Auxiliary APNN (MA-APNN)** for the time-dependent linear radiative transfer equations. Their key innovation is an **adaptive exponentially weighted AP loss**:[^13][^14]
$$
\mathcal{L}(\theta) = e^{-\alpha/\varepsilon} \mathcal{L}_\text{transport}(\theta) + (1 - e^{-\alpha/\varepsilon})\mathcal{L}_\text{diffusion}(\theta),
$$
where $\alpha$ is a tunable parameter and $\mathcal{L}_\text{diffusion}$ is derived from the macroscopic auxiliary equation that directly encodes the diffusion limit. As $\varepsilon \to 0$, the exponential weight smoothly transitions the loss from the full transport form to the limiting diffusion form. This avoids the sharp, discontinuous transition in the loss landscape that can destabilize training near the crossover. Conservation laws serve as regularization terms in the loss.[^15][^13]

### 2.3 Even-Odd Decomposition APNN for Nonlinear Problems (Wu, Ma et al. — 2024)

For nonlinear kinetic equations (BGK, gray radiative transfer), the even-odd decomposition APNN relaxes the stringent conservation prerequisites of the micro-macro approach while introducing an auxiliary deep neural network for the odd parity. The method encodes *both* the original governing equation *and* the dynamical equations for the moments (density, momentum, energy) simultaneously in the loss, closing the system and guaranteeing AP convergence. This redundant-constraint strategy — absent from classical AP numerical schemes — is necessary for the neural network setting because the optimizer cannot otherwise discover the appropriate scaling of each field as $\varepsilon \to 0$.[^16][^17][^11]

**Direct relevance to Jin-Xin AP-PINN:** The Jin-Xin system $\partial_t u + \partial_x v = 0$, $\varepsilon (\partial_t v + A \partial_x u) = -(v - F(u))$ has identical AP structure to these kinetic problems. The APNN strategy is to include in the loss both the full relaxation system residuals **and** an explicit Burgers residual term $\partial_t u + \partial_x F(u)$, weighted by $\varepsilon^2$ or an exponential schedule, so that the network always has a gradient signal toward the correct limit regardless of $\varepsilon$.

***

## 3. Relaxation-Based Network Architectures (RelaxNN)

### 3.1 Relaxation Neural Networks for Shock Capture (Zhou & Ma — arXiv:2404.01163, 2024)

Zhou and Ma (SJTU, 2024) introduced **Relaxation Neural Networks (RelaxNN)**, the most directly relevant work to an AP-PINN for the Jin-Xin system. The key observation is that the PINN's strong-form loss fails near shocks because the conservation law only holds in the weak sense there. Rather than using a weak-form loss (which requires additional infrastructure), RelaxNN works by **solving the Jin-Xin relaxation system itself** with a dual-network architecture:[^18][^7]

- Network $u_{\theta_1}^{NN}(t,x)$ approximates the conservative variable $u$;
- Network $v_{\theta_2}^{NN}(t,x)$ approximates the auxiliary relaxation variable $v$.

The training loss has three components:
$$
\mathcal{L}_\text{RelaxNN} = \omega_\text{res}\,\mathcal{L}_\text{residual} + \omega_\text{flux}\,\mathcal{L}_\text{flux} + \omega_\text{IC}\,\mathcal{L}_\text{IC},
$$
where
$$
\mathcal{L}_\text{residual} = \frac{1}{|\mathcal{T}_r|}\sum_{x_i \in \mathcal{T}_r}\left(\partial_t u_{\theta_1}^{NN} + \partial_x v_{\theta_2}^{NN}\right)^2,
$$
$$
\mathcal{L}_\text{flux} = \frac{1}{|\mathcal{T}_r|}\sum_{x_i \in \mathcal{T}_r}\left(v_{\theta_2}^{NN} - F(u_{\theta_1}^{NN})\right)^2.
$$
The stiff relaxation equation ($1/\varepsilon$ term) is *not* enforced in its original form; instead, the equilibrium condition $v = F(u)$ is enforced as a soft penalty in $\mathcal{L}_\text{flux}$. In the limit $\varepsilon \to 0$, the dissipation loss $\mathcal{L}_\text{dissipate} \approx \mathcal{L}_\text{flux}$, so the RelaxNN naturally recovers the Burgers dynamics. This sidesteps the $1/\varepsilon$ stiffness completely by never explicitly including the stiff term in the loss.[^7]

**Numerical results** for the inviscid Burgers Riemann problem, shallow water equations (dam-break), and Euler equations (Sod, Lax) confirm that RelaxNN significantly outperforms standard PINN in shock capture. The framework preserves PINN simplicity: all standard acceleration strategies (causal weighting, adaptive sampling, time-marching) remain compatible.[^18][^7]

For the explicit **full Jin-Xin case** where the goal is to simulate across all $\varepsilon$ scales, an AP extension of RelaxNN should: (a) keep the stiff term in the loss for finite $\varepsilon$, rescaled as $\varepsilon \cdot \mathcal{L}_\text{dissipate}$, and (b) add an explicit limit-consistency loss $\mathcal{L}_\text{Burgers}$ with an $\varepsilon$-dependent scheduling weight, combining the RelaxNN and MA-APNN strategies.

***

## 4. Weak and Entropy Loss Formulations

### 4.1 wPINNs (De Ryck, Mishra, Molinaro — 2022/2024)

De Ryck, Mishra, and Molinaro introduced **weak PINNs (wPINNs)**, which replace the $L^2$ strong-form residual with a **min-max formulation over Kružkov entropy residuals**:[^19]
$$
\mathcal{L}_\text{wPINN} = \sup_{\phi \in \mathcal{F}_\phi} \left| \int \left[ u_\theta \partial_t \phi + F(u_\theta)\partial_x \phi \right] dt\,dx \right|^2,
$$
where the test-function network $\phi$ is optimized adversarially. The resulting loss is a weak norm of the PDE residual, which remains finite and well-defined even for discontinuous solutions. The authors prove rigorous error bounds, and Chaumet & Giesselmann (2024) extend and improve the approach to systems of conservation laws, computing entropy residuals via auxiliary elliptic dual problems for greater stability.[^8][^9]

### 4.2 WE-PINNs: Weak and Entropy PINNs (2026)

A 2026 preprint (arXiv:2603.24819) proposes **Weak and Entropy PINNs (WE-PINNs)** as a mesh-free control-volume framework. Conservation is enforced via **boundary flux integrals over dynamically sampled space-time control volumes** derived from the divergence theorem, and entropy admissibility is incorporated in integral form to guarantee uniqueness of the entropy solution. Crucially, this avoids saddle-point formulations and auxiliary potential networks entirely, yielding a single standard network architecture. A rigorous $L^1$ convergence analysis via the Bouchut-Perthame framework is provided — the first explicit $L^1$ convergence rate for a mesh-free control-volume PINN. Numerical experiments on Burgers, shallow water, and compressible Euler equations confirm accurate shock resolution.[^20]

### 4.3 Coupled Integral PINN (2024)

The Coupled Integral PINN (CI-PINN) takes inspiration from finite-volume methods to fit the **integral solutions** of conservation laws using auxiliary networks, bypassing the need for spatial and temporal discretization. This eliminates the complexity of non-convex flux reconstruction and the need to evaluate derivatives at shock locations.[^21]

**Applicability to Jin-Xin AP-PINN:** The weak/entropy formulation is particularly important for the zero-relaxation limit of the Jin-Xin system, where the limiting Burgers equation develops true shocks. Embedding entropy conditions (either the Kružkov formulation or the Rankine-Hugoniot condition as an additional loss term) ensures the network selects the physically correct, entropy-admissible weak solution.

***

## 5. Adaptive Weighting, NTK-Based Strategies, and Modified Loss Formulations

### 5.1 NTK-Based Adaptive Weight Scheduling (Wang et al. — 2022)

Wang, Teng, and Perdikaris (2022) provided both the diagnosis and the remedy for gradient pathology in PINNs via NTK theory. The **learning rate annealing (LRA)** algorithm adaptively sets loss weights at each training step by computing the ratio of maximum gradient magnitudes across loss terms:[^3]
$$
\lambda_k \leftarrow (1-\alpha)\lambda_k + \alpha\,\frac{\hat{\lambda}\cdot \max_\theta |\nabla_\theta \mathcal{L}_\text{PDE}|}{\overline{|\nabla_\theta \mathcal{L}_k|}},
$$
where $\hat{\lambda}$ is a target scale and the average is computed over the training batch. This prevents any single loss component from dominating and ensures balanced gradient magnitudes throughout training. However, for multiscale stiff problems, it has been noted that adaptive weighting alone does not fully resolve spectral bias — it balances magnitudes but cannot fix the eigenvalue *distribution* of the NTK.[^2][^3]

### 5.2 ReLoBRaLo and Self-Adaptive Loss Balancing

Bischof et al. introduced **ReLoBRaLo (Relative Loss Balancing with Random Lookback)**, which updates loss weights based on both current gradient statistics and exponentially-decayed historical loss statistics. A Bernoulli random variable decides whether to incorporate early-training statistics, helping escape local minima by randomly changing the effective loss landscape. For the Jin-Xin system, separate weights for the relaxation equation, the continuity equation, and initial/boundary terms can be tuned by ReLoBRaLo without manual $\varepsilon$-dependent prescriptions.[^22]

### 5.3 VS-PINN: Variable-Scaling for Stiff PDEs (Ko & Park — 2024)

Ko and Park (arXiv:2406.06287, 2024) propose **Variable-Scaling PINNs (VS-PINN)**, where the input coordinates and solution fields are rescaled according to the characteristic scales of the PDE before constructing the PINN. For a stiff system with scale parameter $\varepsilon$, the scaling effectively normalizes the NTK eigenvalue distribution, reducing the condition number of the gradient-flow Jacobian. NTK analysis confirms that variable scaling can improve PINN performance by approximately $\mathcal{O}(1/\varepsilon)$ in gradient convergence rate. For the Jin-Xin system, natural scalings include rescaling $v$ by $\varepsilon$ and the temporal coordinate by $\varepsilon$ in the stiff regime, consistent with the Chapman-Enskog expansion.[^23]

### 5.4 MMPINN: Multi-Magnitude Loss (Wang et al. — 2024)

Wang et al. (J. Comput. Phys., 2024) developed **MMPINN**, a framework for multiscale problems with multi-magnitude loss terms. Their regularization strategy applies **power operations** to each loss term to equalize magnitudes:[^6]
$$
\mathcal{L}_\text{MMPINN} = \sum_k \left(\mathcal{L}_k\right)^{p_k},
$$
where exponents $p_k \in (0,1]$ are adapted at multiple training levels (curriculum). This is supplemented by grouping regularization for subdomains. The strategy is particularly relevant for the Jin-Xin system where the relaxation residual scales as $\varepsilon^{-2}$ relative to the continuity residual.[^10][^6]

### 5.5 Gradient-Weighted PDE Loss for Shocks (Liu et al. — PINN-WE)

Liu et al. introduced **PINN-WE (Equation Weighting)** and the companion framework studied in, where a positive **gradient-based (compressibility) weight** is applied to the PDE loss pointwise:[^24][^25][^26]
$$
\mathcal{L}_\text{PDE}^\text{weighted} = \frac{1}{|\mathcal{T}_r|}\sum_{x_i} w(x_i)\,\left(\partial_t u + \partial_x F(u)\right)^2, \quad w = \frac{1}{1+|\partial_x u|/\bar{\partial}},
$$
so that residuals near high-gradient shock regions are **down-weighted**. The network thereby focuses training on smooth regions; the shock zone is then passively compressed by the physical compressibility structure, yielding a sharp, well-located discontinuity without explicit shock detection. This achieves up to 67% reduction in relative $L^2$ error for Burgers shock solutions compared to standard PINN.[^27][^25][^26]

***

## 6. Asymptotic-Informed Architectures and Singular-Layer Methods

### 6.1 Singular-Layer PINN (Chang, Gie, Hong, Jung — arXiv:2410.09723, 2024)

Chang et al. (2024) introduced **sl-PINN** specifically for the viscous Burgers equation at small viscosity $\nu \to 0$, which is directly analogous to the Jin-Xin zero-relaxation limit. The methodology is:[^28][^29]

1. **Asymptotic analysis** of the interior layer: via matched asymptotic expansions, compute corrector functions $\varphi_L(x)$ and $\varphi_R(x)$ that capture the behavior of the viscous solution near the shock (the difference between the full viscous solution and the inviscid limit solution);
2. **Dual-domain architecture**: two separate networks are deployed on $\Omega_{x,L}$ (left of shock) and $\Omega_{x,R}$ (right of shock), each incorporating the corrector functions in their output layer: $u_\theta(t,x) = u_\text{outer}(t,x) + \varphi_{L/R}(t,x)$;
3. **Loss function**: includes PDE residuals on each subdomain, plus interface continuity conditions and Rankine-Hugoniot jump conditions to resolve the mismatch at the shock.[^29]

The approach dramatically reduces errors in the interior-layer region and remains accurate as $\nu \to 0$. The Adam + L-BFGS two-phase optimizer is used for stable convergence. The direct analogy to the Jin-Xin system is that the $\varepsilon$-layer structure around the equilibrium manifold corresponds precisely to the viscous interior layer, and Chapman-Enskog correctors for the Jin-Xin system play the role of $\varphi_{L/R}$.[^29]

### 6.2 Two-Stage Adaptive Lifting PINN (Zhu, Deng, Bi — arXiv:2511.04490, 2025)

Zhu, Deng, and Bi (2025) propose a **Two-stage Adaptive Lifting PINN (TAL-PINN)** for viscous conservation laws near the inviscid limit. The key idea is **input augmentation via a learned auxiliary field**: the physical coordinates $(t, x)$ are lifted to a higher-dimensional space via adaptive coordinate transformations, which are optimized concurrently with the network parameters. An NTK and gradient-flow analysis proves that this input augmentation **improves the conditioning of the NTK**, resulting in faster residual decay. An $L^2$ a posteriori error estimate quantifies how training difficulty scales with viscosity (or, by analogy, with $\varepsilon$ in the Jin-Xin system). Numerical experiments on 1D Burgers (stationary and advancing shock), 2D scalar Burgers, and 1D Euler Lax shock tube confirm stable convergence and accurate shock reconstruction.[^30][^31]

### 6.3 Neural Spectral Element Methods (NSEM — arXiv:2606.02335)

For stiff multiphysics PDEs, the NSEM framework[^32] replaces Monte Carlo collocation with a **spectral element basis** (Legendre-Gauss-Lobatto quadrature), achieving exponential convergence $|E_N| \leq C e^{-\sigma N}$ scaling. The standard collocation-PINN baseline saturates two to three orders of magnitude higher at the same parameter budget due to spectral bias from the Monte Carlo gradient noise[^32]. Furthermore, per-element normalization of quadrature weights prevents the loss-weight pathology where bulk residuals dominate by orders of magnitude over boundary residuals — a problem that directly mirrors the $\varepsilon$-scaling issue in the Jin-Xin stiff source term[^32].

***

## 7. Causal Training and Domain Decomposition

### 7.1 Causal Training (Wang et al. — 2022/2024)

Wang, Sankaran, and Perdikaris (arXiv:2203.07404, published CMAME 2024) propose a **temporally causal loss reformulation**: PDE residuals at time $t$ are weighted by a factor $\omega_i = e^{-\epsilon \sum_{j<i} \mathcal{L}_r(t_j)}$, so that the weight for time $t_i$ becomes active **only after** the network has already achieved small residuals at all earlier times. This prevents the network from fitting future time steps before it has accurately resolved the initial dynamics — a critical issue for stiff evolution equations where the characteristic timescale varies as $\varepsilon$. For the Jin-Xin system, causal training ensures the $\mathcal{O}(\varepsilon)$ fast relaxation dynamics are captured before the $\mathcal{O}(1)$ Burgers dynamics.[^33][^34]

### 7.2 Time-Marching and Sequential Domain Decomposition

Time-marching strategies (Mattey & Ghosh 2022; CEEN, 2024) partition the temporal domain into non-overlapping windows $[t_0, t_1], [t_1, t_2], \ldots$ and train separate networks sequentially on each window. Each window uses the output of the previous network as a Dirichlet initial condition, preventing catastrophic forgetting and enforcing causality at window boundaries. Extra collocation points are concentrated near window beginnings (typically 25% more in the first 10% of each window) to improve initial-condition matching. For the Jin-Xin system near $\varepsilon \to 0$, window sizes should be chosen adaptively based on the relaxation time $\varepsilon$: windows of size $\mathcal{O}(\varepsilon)$ near $t=0$ and larger windows in the quasi-steady Burgers phase.[^35][^36]

### 7.3 XPINNs and cPINNs for Shock Localization

Extended PINNs (XPINNs) and Conservative PINNs (cPINNs) deploy separate, smaller networks in each spatial subdomain with interface conditions (Rankine-Hugoniot, flux conservation) enforced explicitly. For Burgers shock problems, the shock interface can be learned adaptively. Adversarial Adaptive Sampling (AAS) as used in PINN-BALLS provides a learnable, residual-driven domain decomposition that autonomously concentrates capacity near shock regions without requiring a priori knowledge of the shock location.[^37][^38]

***

## 8. Activation Functions and Spectral Bias Mitigation

### 8.1 Fourier Feature Embedding

Tancik et al.'s **Fourier Feature Embedding (FFE)** technique (adopted broadly for PINNs) maps input coordinates to a high-dimensional periodic space:[^39]
$$
\gamma(x,t) = [\sin(2\pi B (x,t)^T),\, \cos(2\pi B (x,t)^T)]^T,
$$
where $B$ is a random frequency matrix. This explicitly embeds high-frequency basis functions into the input representation, directly counteracting spectral bias. A 30% error reduction in high-frequency regimes has been reported compared to decoder-only baselines. For the Jin-Xin system, the relevant frequency scales include the Burgers shock scale ($\mathcal{O}(1)$) and the relaxation layer scale ($\mathcal{O}(\varepsilon^{-1})$); a **multi-scale FFE** with separate frequency bands for each scale is appropriate.[^40][^41][^39]

### 8.2 Sinusoidal and Non-Standard Activations

The choice of activation function significantly impacts the network's frequency response. Sinusoidal activations (SIREN) and trigonometric activations more generally enable the network to directly represent high-frequency oscillatory functions, achieving superior approximation compared to tanh for stiff-solution problems. For the Jin-Xin system, tanh is standard for smooth problems, but near the shock layer a switch to sinusoidal or Swish activations can improve resolution. Jagtap et al.'s **adaptive activation functions** introduce a learnable scaling parameter $a_k$ per neuron such that $\sigma_k(x) = \sigma(a_k \cdot x)$, where $a_k$ is updated via gradient descent alongside network weights, enabling the network to adaptively tune its effective frequency content.[^42][^41][^43][^22]

### 8.3 Residual-Based Adaptive Sampling (RAD/RAR-D)

Lu et al.'s **RAR-D (Residual-based Adaptive Refinement with Distribution)** dynamically redistributes collocation points by sampling proportionally to the current PDE residual magnitude. This concentrates points at the shock location (high residual) and in the $\varepsilon$-layer (steep gradients) without prior knowledge of their location. Comparative studies across 6,000+ PINN simulations confirm that RAD and RAR-D **significantly improve accuracy** with fewer total residual points compared to uniform sampling. For the Jin-Xin AP-PINN, RAR-D can be applied separately to the relaxation residual and the continuity residual, with their respective densities scaled by $\varepsilon$.[^44]

***

## 9. Numerical Robustness of PINNs for Multiscale Transport

A rigorous theoretical study by De Ryck et al. (arXiv:2412.14683, 2024) investigated PINN numerical robustness for multiscale transport equations using ReLU activations, establishing an analogy between PINNs and least-squares finite elements (LSFE). The key finding is that **in the diffusive regime ($\varepsilon \to 0$), the standard PINN does not reach the correct limit** — in full agreement with known LSFE results. A *diffusive scaling* of the unknowns, introduced at the level of the network input/output normalization, restores convergence to the correct limit — again in perfect analogy with the fix for first-order LSFE methods. This provides rigorous theoretical grounding for the variable-scaling and AP reformulation approaches described above.[^45]

***

## 10. Synthesis and Recommendations for Jin-Xin AP-PINN

The table below synthesizes the key methods with their targeted failure mode and implementation complexity.

| Method | Targets | Key Reference | Complexity |
|---|---|---|---|
| AP loss (micro-macro decomposition) | $\varepsilon \to 0$ limit failure | Jin, Ma, Wu (J. Sci. Comput. 2023)[^10] | Moderate |
| MA-APNN (adaptive exp. weighting) | $\varepsilon$-transition stiffness | Li et al. (2024)[^13] | Moderate |
| Even-odd APNN with conservation | Non-conservation failure, multiscale | Wu, Ma et al. (CiCP 2024)[^16] | Moderate |
| RelaxNN (dual-network relaxation) | Strong-form loss breakdown at shock | Zhou & Ma (2024)[^18] | Low |
| wPINN / WE-PINN (weak formulation) | Entropy condition, shock admissibility | De Ryck et al.[^19]; 2026[^20] | High |
| NTK adaptive weighting (LRA) | Loss imbalance, gradient pathology | Wang et al. (CMAME 2022)[^3] | Low |
| VS-PINN (variable scaling) | NTK stiffness as $\varepsilon \to 0$ | Ko & Park (arXiv:2406.06287)[^23] | Low |
| sl-PINN (singular-layer correctors) | Spectral bias in shock layer | Chang et al. (arXiv:2410.09723)[^28] | High |
| TAL-PINN (adaptive coordinate lifting) | NTK conditioning near inviscid limit | Zhu et al. (arXiv:2511.04490)[^31] | Moderate |
| Fourier Feature Embedding (FFE) | Spectral bias (high-frequency) | Tancik et al. / Wang et al.[^39] | Low |
| Sinusoidal / adaptive activations | Frequency selectivity | Jagtap et al.[^22]; SIREN[^43] | Low |
| Causal temporal weighting | Temporal causality violation | Wang et al. (CMAME 2024)[^33] | Low |
| Time-marching / CEEN | Long-time stiff integration | Mattey & Ghosh; CEEN[^35][^36] | Low |
| RAR-D adaptive sampling | Shock localization, residual density | Lu et al.[^44] | Low |
| Gradient-weighted PDE loss (PINN-WE) | Shock smearing from strong form | Liu et al.[^25][^26] | Low |
| NSEM (spectral elements) | Collocation noise, stiff coupling | arXiv:2606.02335[^32] | High |

**For an AP-PINN on the Jin-Xin system targeting the uniform-$\varepsilon$ regime**, the recommended combination is:

1. **AP loss formulation**: adopt the MA-APNN adaptive exponential weighting, combining a Jin-Xin residual loss with an explicit Burgers residual loss smoothly weighted by $e^{-\alpha/\varepsilon}$;
2. **Dual-network RelaxNN architecture**: avoid the explicit $1/\varepsilon$ stiff term by encoding equilibrium as a flux-matching penalty;
3. **Entropy / weak formulation for the zero-$\varepsilon$ limit**: incorporate either a Kružkov entropy inequality term or a space-time flux balance formulation to guarantee the correct entropy-admissible Burgers shock is selected;
4. **NTK-based adaptive weighting (LRA or MMPINN)**: balance the relaxation loss, continuity loss, and Burgers consistency loss throughout training;
5. **Causal training with $\varepsilon$-adaptive windows**: respect temporal causality and match window sizes to the relaxation timescale;
6. **RAR-D adaptive sampling**: concentrate collocation points at the shock location and in the $\varepsilon$-layer;
7. **Fourier feature embedding or sinusoidal activations**: address spectral bias in the shock layer at scale $\varepsilon^{-1}$;
8. **Variable scaling of the $v$ field** by $\varepsilon$ at input/output level to normalize NTK eigenvalues.

---

## References

1. [Understanding and mitigating gradient pathologies in PINNs](https://odi.inf.ethz.ch/teaching/AI4Science/Group7.pdf)

2. [Under review as submission to TMLR](https://openreview.net/notes/edits/attachment?id=po0YIiDiBV&name=pdf)

3. [When and why PINNs fail to train: A neural tangent kernel perspective](https://www.sciencedirect.com/science/article/abs/pii/S002199912100663X) - We analyze the training dynamics of PINNs using neural tangent kernel theory. We derive the NTK of P...

4. [Physics informed neural networks for elliptic equations with ... - arXiv](https://arxiv.org/html/2212.13531v2)

5. [[PDF] Neural Tangent Kernel of Neural Networks with Loss Informed by ...](https://arxiv.org/pdf/2503.11029.pdf)

6. [An adaptive wavelet-based PINN for problems with localized ... - arXiv](https://arxiv.org/html/2604.28180v1)

7. [Capturing Shock Waves by Relaxation Neural Networks - arXiv](https://arxiv.org/html/2404.01163v1) - In this paper, we put forward a neural network framework to solve the nonlinear hyperbolic systems. ...

8. [Improving Weak PINNs for Hyperbolic Conservation Laws - arXiv](https://arxiv.org/html/2211.12393v2) - We provide explicit computations that highlight why classical PINNs will not work for discontinuous ...

9. [Improving Weak PINNs for Hyperbolic Conservation Laws](https://smai-jcm.centre-mersenne.org/articles/10.5802/smai-jcm.116/) - We provide explicit computations that highlight why classical PINNs will not work for discontinuous ...

10. [Asymptotic-Preserving Neural Networks for Multiscale Time-Dependent Linear Transport Equations](https://dl.acm.org/doi/10.1007/s10915-023-02100-0) - In this paper we develop a neural network for the numerical simulation of time-dependent linear tran...

11. [Asymptotic-Preserving Neural Networks for Multiscale Kinetic Equations](https://arxiv.org/html/2306.15381v4)

12. [Asymptotic-Preserving Neural Networks for multiscale ...](https://sfera.unife.it/retrieve/281c7775-cab9-4916-8806-d2fb4994e15d/2206.12625.pdf)

13. [Macroscopic auxiliary asymptotic preserving neural networks for the ...](https://arxiv.org/abs/2403.01820) - We develop a Macroscopic Auxiliary Asymptotic-Preserving Neural Network (MA-APNN) method to solve th...

14. [Asymptotic-Preserving Neural Networks for Multiscale Kinetic Equations](https://global-sci.com/article/90937/asymptotic-preserving-neural-networks-for-multiscale-kinetic-equations)

15. [Macroscopic auxiliary asymptotic preserving neural networks for the linear radiative transfer equations](https://www.arxiv.org/pdf/2403.01820.pdf)

16. [Asymptotic-Preserving Neural Networks for Multiscale Kinetic ...](https://global-sci.com/cicp/article/view/7246) - In this paper, we present two novel Asymptotic-Preserving Neural Networks (APNNs) for tackling multi...

17. [Asymptotic-Preserving Neural Networks based on Even-odd ... - arXiv](https://arxiv.org/html/2501.08166v2) - We present a novel Asymptotic-Preserving Neural Network (APNN) approach utilizing even-odd decomposi...

18. [[2404.01163] Capturing Shock Waves by Relaxation Neural Networks](https://arxiv.org/abs/2404.01163) - In this paper, we put forward a neural network framework to solve the nonlinear hyperbolic systems. ...

19. [wPINNs: Weak Physics informed neural networks for approximating entropy solutions of hyperbolic conservation laws](https://arxiv.org/abs/2207.08483) - Physics informed neural networks (PINNs) require regularity of solutions of the underlying PDE to gu...

20. [[2603.24819] Weak and entropy physics-informed neural networks ...](https://arxiv.org/abs/2603.24819) - We propose Weak and Entropy PINNs (WE-PINNs) for the approximation of entropy solutions to nonlinear...

21. [Coupled Integral PINN for conservation law - arXiv](https://arxiv.org/html/2411.11276v1) - These methods resolve the integral form of conservation laws and delineate the shock characteristics...

22. [Multi-Objective Loss Balancing for Physics-Informed Deep ...](https://www.research-collection.ethz.ch/server/api/core/bitstreams/a4a7cc55-9469-4dec-86c6-4ba466eaf2f5/content)

23. [VS-PINN: A fast and efficient training of physics-informed neural networks using variable-scaling methods for solving PDEs with stiff behavior](https://www.arxiv.org/abs/2406.06287) - Physics-informed neural networks (PINNs) have recently emerged as a promising way to compute the sol...

24. [[PDF] Gradient weighted physics-informed neural networks for capturing ...](https://ml4physicalsciences.github.io/2023/files/NeurIPS_ML4PS_2023_227.pdf)

25. [Discontinuity Computing using Physics-Informed Neural Network](https://arxiv.org/abs/2206.03864) - Simulating discontinuities is a long standing problem especially for shock waves with strong nonline...

26. [Physics-informed neural network with weighted loss and hard ...](https://pmc.ncbi.nlm.nih.gov/articles/PMC12858974/) - In this study, we proposed a weighted loss hard constraint physics-informed neural networks (PINNs) ...

27. [Enhanced Physics-Informed Neural Networks with ...](https://academianexusjournal.com/index.php/anj/article/download/39/40)

28. [[2410.09723] Singular layer PINN methods for Burgers' equation](https://arxiv.org/abs/2410.09723) - In this article, we present a new learning method called sl-PINN to tackle the one-dimensional visco...

29. [[Papierüberprüfung] Singular layer PINN methods for Burgers' equation](https://www.themoonlight.io/de/review/singular-layer-pinn-methods-for-burgers-equation) - In the paper "Singular Layer PINN Methods for Burgers’ Equation" by Teng-Yuan Chang, Gung-Min Gie, Y...

30. [A Two-stage Adaptive Lifting PINN Framework for Solving Viscous ...](https://arxiv.org/html/2511.04490v1)

31. [A Two-stage Adaptive Lifting PINN Framework for Solving Viscous ...](https://arxiv.org/abs/2511.04490) - The key idea is to augment the physical coordinates by introducing a learned auxiliary field generat...

32. [Neural Spectral Element Methods for stiff multiphysics PDEs with electrochemical transport benchmarks](https://arxiv.org/pdf/2606.02335.pdf)

33. [Respecting causality for training physics-informed neural networks](https://www.sciencedirect.com/science/article/abs/pii/S0045782524000690) - While the popularity of physics-informed neural networks (PINNs) is steadily rising, to this date PI...

34. [Unraveling the Design Pattern of Physics-Informed Neural Networks: Part 06 | Towards Data Science](https://towardsdatascience.com/unraveling-the-design-pattern-of-physics-informed-neural-networks-part-06-bcb3557199e2/) - Welcome to the 6th blog of this series, where we continue our exciting journey of exploring design p...

35. [Contents](https://arxiv.org/html/2512.23396v1)

36. [Causality-enforced evolutional networks for solving time ...](https://www.sciencedirect.com/science/article/abs/pii/S0045782524002925)

37. [[PDF] PINN Balls: Scaling Second-Order Methods for PINNs with Domain ...](https://papers.nips.cc/paper_files/paper/2025/file/05dbca96b388e7dc4138b73bd1515cdf-Paper-Conference.pdf) - Our model – PINN BALLS – also features a fully learnable domain decomposition structure, achieved th...

38. [[PDF] Extended Physics-informed Neural Networks (XPINNs): A Generalized Space-Time Domain Decomposition based Deep Learning Framework for Nonlinear Partial Differential Equations | Semantic Scholar](https://www.semanticscholar.org/paper/Extended-Physics-informed-Neural-Networks-(XPINNs):-Jagtap-Karniadakis/547552a62423b9eb1aab2ff6c6f87f4fbcd89362) - The proposed XPINN method is the generalization of PINN and cPINN approaches, both in terms of appli...

39. [University of Birmingham](https://pure-oai.bham.ac.uk/ws/portalfiles/portal/198274421/PINN_manuscript_accepted_version.pdf)

40. [[PDF] Physics-Informed Neural Networks with Fourier Features and ...](https://openreview.net/pdf/b2254bd449cb12ac6ce5da4cad7890297d02a416.pdf) - The Fourier feature embeddings enabling the S-Pformer to better capture multiscale behaviors by adap...

41. [Multi-Scale Separable Fourier Neural Networks for Solving High-Frequency PDEs](https://arxiv.org/html/2605.31027v2)

42. [Physical Informed Neural Network for Solving Con](https://global-sci.com/jics/article/download/23668/36749/38788)

43. [Physics-informed Neural Networks with Fourier Features for Seismic ...](https://arxiv.org/html/2409.03536v1)

44. [A comprehensive study of non-adaptive and residual-based adaptive sampling for physics-informed neural networks](https://arxiv.org/abs/2207.10289) - Physics-informed neural networks (PINNs) have shown to be an effective tool for solving forward and ...

45. [Numerical Robustness of PINNs for Multiscale Transport Equations](https://arxiv.org/abs/2412.14683) - We investigate the numerical solution of multiscale transport equations using Physics Informed Neura...

