# RelaxNN / RPINN for the Jin–Xin Relaxation System: A PhD-Level Technical Deep Dive

## 1. The Jin–Xin Relaxation System and the Challenge

The Jin–Xin relaxation system, introduced by Shi Jin and Zhouping Xin (1995), is a prototypical hyperbolic relaxation model for scalar conservation laws. For the specific case of Burgers' equation, the 1D Jin–Xin system reads:[^1]

$$
\partial_t u + \partial_x v = 0,
$$
$$
\partial_t v + \frac{1}{\varepsilon^2} \partial_x u = -\frac{1}{\varepsilon^2}(v - f(u)),
$$

where $u(x,t)$ is the conserved variable, $v(x,t)$ is the flux variable, $f(u) = u^2/2$ is the Burgers flux, and $\varepsilon > 0$ is the relaxation parameter. As $\varepsilon \to 0$, the system formally imposes the local equilibrium condition $v = f(u)$, and the system collapses to the inviscid Burgers equation $\partial_t u + \partial_x f(u) = 0$. This limiting equation admits shock wave solutions — step-like discontinuities in the conserved variable — making it one of the canonical test cases for numerical methods on stiff hyperbolic systems.[^2][^1]

The central challenge for PINNs is that this system lives in two distinct regimes: for $\varepsilon = O(1)$, both equations are active and non-stiff; for $\varepsilon \ll 1$, the source term $\varepsilon^{-2}(v - f(u))$ becomes extremely stiff, driving the solution to the equilibrium manifold on a timescale far faster than the macroscopic dynamics. Vanilla PINNs, which naively penalize the residuals of both equations simultaneously, fail catastrophically in this regime, both because of algebraic instability induced by the $\varepsilon^{-2}$ factor and because of the spectral bias of MLPs against the high-frequency content of shock discontinuities.

***

## 2. Network Architecture and Loss Formulation of RelaxNN / RPINN

### 2.1 Dual Sub-Network Architecture

The RelaxNN (also termed RPINN — Relaxation PINN, or the AP-PINN for relaxation systems) approach is inspired directly by the structure of Asymptotic-Preserving (AP) numerical schemes. Rather than using a single MLP to approximate both unknowns, the method deploys **two separate sub-networks**:

- **Network $\mathcal{N}_u$**: a fully-connected MLP with inputs $(x,t)$ that outputs the conserved variable $u_\theta(x,t) \approx u(x,t)$.
- **Network $\mathcal{N}_v$**: a second fully-connected MLP with inputs $(x,t)$ that outputs the flux variable $v_\theta(x,t) \approx v(x,t)$.

This two-network decomposition is directly analogous to the "macro-micro" or "even-odd" decomposition strategies used in classical AP schemes and in the APNN framework of Shi Jin, Zheng Ma, and Keke Wu (2023). The rationale is that separating the networks allows the loss to be constructed from the *macroscopic* conservation law (which is well-behaved as $\varepsilon \to 0$) and a *scaled* version of the relaxation equation (which avoids the dangerous $\varepsilon^{-2}$ division). The key theoretical requirement on the AP-PINN is that: as $\varepsilon \to 0$, the loss function of the full system converges to the loss function of the reduced model (the Burgers equation), uniformly in $\varepsilon$.[^3][^4][^5]

### 2.2 The AP Loss Function

The central innovation of RelaxNN is to reformulate the PDE residuals so that no term containing $\varepsilon^{-2}$ appears explicitly in the loss. Starting from the Jin–Xin system, one multiplies the second equation by $\varepsilon^2$ to absorb the stiff coefficient:

$$
\varepsilon^2 \partial_t v_\theta + \partial_x u_\theta = -(v_\theta - f(u_\theta)).
$$

This rescaled form remains well-defined as $\varepsilon \to 0$. The **full AP loss** is then:

$$
\mathcal{L}_{\mathrm{AP}}(\theta) = \mathcal{L}_{\mathrm{cons}} + \mathcal{L}_{\mathrm{relax}} + \mathcal{L}_{\mathrm{eq}} + \mathcal{L}_{\mathrm{IC}} + \mathcal{L}_{\mathrm{BC}},
$$

where the individual residual terms are:

$$
\mathcal{L}_{\mathrm{cons}} = \frac{1}{N_r} \sum_{i=1}^{N_r} \left| \partial_t u_\theta(x_i,t_i) + \partial_x v_\theta(x_i,t_i) \right|^2, \quad (1)
$$

$$
\mathcal{L}_{\mathrm{relax}} = \frac{1}{N_r} \sum_{i=1}^{N_r} \left| \varepsilon^2 \partial_t v_\theta(x_i,t_i) + \partial_x u_\theta(x_i,t_i) + \left(v_\theta(x_i,t_i) - f(u_\theta(x_i,t_i))\right) \right|^2, \quad (2)
$$

$$
\mathcal{L}_{\mathrm{eq}} = \frac{\lambda_{\mathrm{eq}}}{N_r} \sum_{i=1}^{N_r} \left| v_\theta(x_i,t_i) - f(u_\theta(x_i,t_i)) \right|^2, \quad (3)
$$

$$
\mathcal{L}_{\mathrm{IC}} = \frac{1}{N_0} \sum_{i=1}^{N_0} \left| u_\theta(x_i,0) - u_0(x_i) \right|^2 + \left| v_\theta(x_i,0) - f(u_0(x_i)) \right|^2, \quad (4)
$$

$$
\mathcal{L}_{\mathrm{BC}} = \frac{1}{N_b} \sum_{i=1}^{N_b} \left[ \left| u_\theta(x^b_i,t_i) - u^b(t_i) \right|^2 + \left| v_\theta(x^b_i,t_i) - v^b(t_i) \right|^2 \right]. \quad (5)
$$

Here $\{(x_i,t_i)\}_{i=1}^{N_r}$ are the interior collocation (residual) points, $\{(x_i,0)\}_{i=1}^{N_0}$ are the initial condition points, and $\lambda_{\mathrm{eq}} > 0$ is a hyperparameter weighting the equilibrium penalty term.

### 2.3 The "Soft Penalty" for Local Equilibrium

The term $\mathcal{L}_{\mathrm{eq}}$ (Eq. (3)) is the **soft penalty for the equilibrium constraint** $v = f(u)$. This term does not appear in the original PDE — it is an additional physics-informed regularizer that encodes the asymptotic structure of the system. Its role is crucial:

1. **As $\varepsilon \to 0$**: the loss term $\mathcal{L}_{\mathrm{relax}}$ reduces to penalizing $|\partial_x u_\theta + (v_\theta - f(u_\theta))|^2$, which enforces equilibrium implicitly. The separate $\mathcal{L}_{\mathrm{eq}}$ provides an explicit, strong signal for this equilibrium.
2. **It is soft** (not hard): the network is not architecturally constrained to satisfy $v_\theta = f(u_\theta)$ exactly. Instead, the optimizer is free to deviate from equilibrium in the kinetic regime ($\varepsilon = O(1)$), where the true solution has $v \neq f(u)$, and only the loss gradient drives $v_\theta \to f(u_\theta)$ as $\varepsilon$ decreases.
3. **The weight $\lambda_{\mathrm{eq}}$** must be tuned: if too large, the network is overconstrained for $\varepsilon = O(1)$; if too small, convergence to the correct limit is not guaranteed.[^4]

The AP property of this construction can be verified formally: in the limit $\varepsilon \to 0$, $\mathcal{L}_{\mathrm{relax}} \to |\partial_x u_\theta + (v_\theta - f(u_\theta))|^2$ and, combined with $\mathcal{L}_{\mathrm{eq}}$, forces $v_\theta \to f(u_\theta)$. Substituting into $\mathcal{L}_{\mathrm{cons}}$ then recovers the Burgers residual $|\partial_t u_\theta + \partial_x f(u_\theta)|^2$, exactly as required by the AP condition [^4][^3].

***

## 3. Overcoming Gradient Pathology: The NTK Perspective

### 3.1 Why Vanilla PINNs Fail for Stiff Systems

The failure of vanilla PINNs on stiff relaxation problems can be precisely characterized using Neural Tangent Kernel (NTK) theory. Wang, Yu, and Perdikaris (2022)  proved that the training dynamics of a PINN are governed by the block NTK matrix:

$$
\mathbf{K}(t) = \begin{pmatrix} K_{uu}(t) & K_{ur}(t) \\ K_{ru}(t) & K_{rr}(t) \end{pmatrix},
$$

where the sub-blocks are Gram matrices of the Jacobians of the network outputs $u(x_b;\theta)$ and the PDE residual $\mathcal{N}[u](x_r;\theta)$ with respect to the parameters $\theta$. In the infinite-width limit, $\mathbf{K}(t)$ converges to a deterministic constant kernel $\mathbf{K}^*$, and the training error decay rate in the $i$-th eigenvector direction is $e^{-\lambda_i t}$, where $\lambda_i$ are the eigenvalues of $\mathbf{K}^*$ .

For the vanilla PINN applied to the Jin–Xin system with the raw (unscaled) equations, the residual loss contains terms like:

$$
\mathcal{L}^{\text{vanilla}}_{\mathrm{relax}} = \frac{1}{N_r} \sum_i \left| \partial_t v_\theta + \frac{1}{\varepsilon^2} \partial_x u_\theta + \frac{1}{\varepsilon^2}(v_\theta - f(u_\theta)) \right|^2.
$$

The automatic differentiation graph for this term involves multiplications by $\varepsilon^{-2}$. In the $\varepsilon \to 0$ limit, the gradient of this term with respect to $\theta$ is dominated by the $\varepsilon^{-2}$ factor, causing the NTK block $K_{rr}$ — which corresponds to the PDE residual sub-network — to have spectral norm $\|K_{rr}\| \sim \varepsilon^{-4}$. This creates a severe imbalance: $K_{rr}$ dominates $K_{uu}$ by a factor of $\varepsilon^{-4}$, so the convergence rates of the two loss components are wildly mismatched . The PDE residual minimizes at an exponential rate $\sim e^{-\varepsilon^{-4} t}$ (extremely fast), while the boundary/initial conditions converge at an $\mathcal{O}(1)$ rate — a textbook gradient stiffness phenomenon. Worse, the maximum stable learning rate is $\eta \leq 2/\lambda_{\max}(\mathbf{K}) \sim 2\varepsilon^4 \to 0$, making training unstable or requiring prohibitively small step sizes .

Furthermore, Wang, Wang, and Perdikaris (2021)  demonstrated through NTK analysis that fully-connected PINNs suffer from **spectral bias** (also called the F-principle, studied independently by Xu et al. ): the network learns the low-frequency components of the target function first, while high-frequency content — exactly what is needed to represent shock discontinuities in the Burgers limit — is learned extremely slowly, corresponding to the smallest eigenvalues of the NTK.[^6][^7][^8]

### 3.2 How RelaxNN Bypasses the Stiffness

The RelaxNN formulation completely sidesteps the NTK blowup by construction. By multiplying the second equation by $\varepsilon^2$ before forming the loss (as in Eq. (2) above), no term $\varepsilon^{-2}$ appears in the automatic differentiation graph. As a consequence:

- The spectral norm $\|K_{rr}\|$ remains bounded uniformly in $\varepsilon$.
- The ratio $\|K_{rr}\| / \|K_{uu}\|$ remains $\mathcal{O}(1)$, so both loss components converge at comparable rates [^4].
- The maximum stable learning rate remains $\mathcal{O}(1)$ uniformly in $\varepsilon$.

This is precisely the neural network analogue of why classical AP schemes are designed: just as an AP scheme avoids resolving the fast timescale $\varepsilon^2$ by reformulating the discrete equations, the AP-PINN/RelaxNN avoids the stiff gradient flow by reformulating the continuous loss. The asymptotic-preserving construction for neural networks was first formalized for the Goldstein–Taylor model and diffusive BGK equations in Bertaglia (2022)  and subsequently developed into a general framework for multiscale kinetic equations by Jin, Ma, and Wu (2023).[^5][^3][^4]

Importantly, when $\varepsilon \to 0$, the loss $\mathcal{L}_{\mathrm{relax}}$ in Eq. (2) converges to penalizing only $|\partial_x u_\theta + (v_\theta - f(u_\theta))|^2$, which is an $\mathcal{O}(1)$ quantity — the network does not "see" the stiffness at all in the loss landscape. This is the key mathematical statement of the AP property at the level of the loss [^3].

### 3.3 The Role of the Macroscopic Equation

A subtle but crucial point — first highlighted in the APNN literature  — is that **the macroscopic conservation equation for $u$ must be explicitly included in the loss**. If one uses only the relaxation equation for $v$ (even after $\varepsilon^2$-scaling), the network in the limit $\varepsilon \to 0$ has no equation that governs the time evolution of $u$: the loss reduces to a purely algebraic equilibrium condition, and the network stagnates at the initial condition. The inclusion of $\mathcal{L}_{\mathrm{cons}}$ (Eq. (1)) provides the essential dynamical equation that drives the macroscopic evolution.[^5]

***

## 4. Addressing Shock Waves: Adaptive Sampling Strategies

### 4.1 The Spectral Bias Problem for Shocks

Even with the RelaxNN architecture resolving the stiffness, standard MLPs with uniformly sampled collocation points exhibit severe **spectral bias** (F-principle) in approximating the discontinuous solutions of the Burgers limit. The F-principle, established by Xu et al. (2019) and rigorously analyzed through NTK theory, states that during gradient descent, deep networks trained with smooth activations tend to learn the low-frequency components of the target function first, with high-frequency components converging at a rate proportional to their small eigenvalues in the NTK spectrum. For a shock wave — a step-function discontinuity that requires infinitely many Fourier modes — standard uniform-density collocation is catastrophically inefficient: most collocation points are placed far from the shock location where the residual is already small, wasting computational budget.[^8][^6]

### 4.2 Residual-Based Adaptive Distribution (RAD)

Wu, Zhu, Tan, Kartha, and Lu (2022)  conducted the most comprehensive study to date of adaptive sampling strategies for PINNs, proposing two new methods:[^9]

**RAD (Residual-based Adaptive Distribution)**: the collocation points are drawn from a probability density proportional to a power of the pointwise PDE residual. Concretely, at training step $k$, the distribution for sampling new collocation points is:

$$
p_k(x,t) \propto \left| \mathcal{R}_\theta(x,t) \right|^c + \delta,
$$

where $\mathcal{R}_\theta(x,t)$ is the pointwise PDE residual (computed on a large candidate set), $c > 0$ controls how sharply the distribution concentrates near high-residual regions, and $\delta > 0$ is a small floor ensuring global exploration. In practice, $c = 1$ and $\delta$ is chosen as a small fraction of the mean absolute residual. The set of collocation points is completely replaced (resampled) every $T_{\mathrm{resample}}$ training iterations.[^9]

**RAR-D (Residual-based Adaptive Refinement with Distribution)**: instead of replacing the full set, RAR-D starts from a fixed uniform grid and *adds* new points drawn from the RAD distribution every few epochs. This preserves the global coverage of uniform sampling while enriching the density near high-residual features (e.g., shocks).[^9]

In over 6000 PINN simulations, Wu et al. (2022) demonstrated that RAD and RAR-D significantly outperform fixed uniform sampling, with particular advantages for problems with sharp features such as the Burgers shock.[^9]

### 4.3 Implementation in the Relaxation-PINN Context

For RelaxNN applied to the Jin–Xin / Burgers shock problem, the adaptive sampling loop is:

1. **Initialize** with a fixed uniform set $\{(x_i^{(0)}, t_i^{(0)})\}_{i=1}^{N_r}$ in the domain $[x_L, x_R] \times [0,T]$.
2. **Train** the two sub-networks $\mathcal{N}_u, \mathcal{N}_v$ by minimizing $\mathcal{L}_{\mathrm{AP}}$ for $T_{\mathrm{resample}}$ gradient steps.
3. **Evaluate residuals** on a large, densely sampled candidate set $\mathcal{C} = \{(x_j^c, t_j^c)\}_{j=1}^{N_c}$ with $N_c \gg N_r$. The relevant residual for RAD is the *macroscopic* residual:

$$
\mathcal{R}_\theta(x_j, t_j) = \left| \partial_t u_\theta + \partial_x v_\theta \right|^2 + \left| \varepsilon^2 \partial_t v_\theta + \partial_x u_\theta + (v_\theta - f(u_\theta)) \right|^2.
$$

4. **Resample** the interior collocation set according to $p(x,t) \propto |\mathcal{R}_\theta(x,t)|^c + \delta$ (for RAD) or augment with points from this distribution (for RAR-D).
5. **Repeat** steps 2–4 until convergence.

This procedure concentrates collocation points near the shock front as it forms and propagates, providing the optimizer with high-quality gradient information exactly where spectral bias is most severe. A crucial implementation detail for *time-dependent* problems is the **temporal causality** weighting of Wang et al. (2022), which modifies the collocation sampling to respect the causal structure of the PDE: points at later times should only be sampled once the solution at earlier times is well-converged. Combining RAD with causal weights has been shown to be especially effective for problems with propagating discontinuities.[^10][^11][^9]

### 4.4 Related Adaptive Sampling Strategies

Several other approaches have been proposed that complement or extend RAD for shock problems:

- **Adversarial Adaptive Sampling (AAS)** (Zeng, Zou, et al., 2024): embeds the Wasserstein distance between the residual-induced distribution and the uniform distribution into the loss, solved as a min-max problem. This promotes a *near-uniform residual profile*, minimizing the Monte Carlo variance of the loss approximation and leading to theoretically grounded sampling efficiency.[^12]
- **PACMANN** (2024): addresses poor scaling of residual-based sampling to high dimensions by using local geometric information to guide collocation placement.[^13]
- **QR-DEIM** adaptive strategy (Guo, Manzoni, et al., 2025): selects collocation points using the QR decomposition of the discrete empirical interpolation method, combining information about residual magnitudes and the geometry of the solution manifold. Benchmarked on Burgers' equation, it outperforms pure residual-based methods in accuracy-per-sample.[^14]
- **Causality-guided adaptive sampling (Causal AS)** (2024): uses causal weighting factors to select collocation points, particularly effective for propagating wave fronts and shocks, by ensuring the network's temporal accuracy is built up progressively from $t=0$.[^10]

***

## 5. The Weak-PINN Alternative for Shocks

An important complementary approach — particularly relevant when the solution is discontinuous — is the **weak PINNs** formulation. Badia, Caicedo, and Lozinski (2022, updated 2023)  proved rigorously that the strong-form PINN residual is *not consistent* with distributional (entropy) solutions of nonlinear hyperbolic conservation laws at shock locations: the Dirac-delta distributional part of the derivative at a shock is invisible to the pointwise MSE loss. Weak PINNs replace the strong-form residual with a *dual norm* (often a $H^{-1}$ or $W^{-1,1}$ norm) of the PDE residual, which *does* sense distributional solutions and correctly penalizes Rankine–Hugoniot violations. While more expensive to implement than RAD-based RelaxNN, weak PINNs offer stronger theoretical guarantees for shock-dominated solutions.[^15]

***

## 6. Summary of Key Papers

| Paper | Authors | Year | Key Contribution |
|-------|---------|------|-----------------|
| Jin & Xin, *Comm. Pure Appl. Math.* | Shi Jin, Zhouping Xin | 1995 | Original Jin–Xin relaxation scheme; AP property [^1] |
| Raissi, Perdikaris, Karniadakis, *JCP* | M. Raissi, P. Perdikaris, G.E. Karniadakis | 2019 | Original PINN formulation [^16] |
| Wang, Yu, Perdikaris, *JCP* | S. Wang, X. Yu, P. Perdikaris | 2022 | NTK theory of PINNs; spectral bias; adaptive loss weights  |
| Wang, Wang, Perdikaris, *CMAME* | S. Wang, H. Wang, P. Perdikaris | 2021 | Eigenvector bias; multi-scale Fourier features for PINNs [^6][^7] |
| Bertaglia, *arXiv:2210.09081* | G. Bertaglia | 2022 | APNN for Goldstein–Taylor and epidemic models; AP loss for diffusive scaling [^4] |
| Jin, Ma, Wu, *J. Sci. Comput.* / *arXiv:2306.15381* | S. Jin, Z. Ma, K. Wu | 2023 | APNN V2: even-odd decomposition; AP loss for linear transport and BGK [^3][^5] |
| Wu et al., *CMAME* / *arXiv:2207.10289* | C. Wu, M. Zhu, Q. Tan, Y. Kartha, L. Lu | 2022 | RAD and RAR-D adaptive sampling; 6000+ PINN experiments [^9] |
| Wang, Sankaran, Perdikaris, *arXiv:2203.07404* | S. Wang, S. Sankaran, P. Perdikaris | 2022 | Temporal causality weighting for training PINNs [^11] |
| Zeng et al., *arXiv:2305.18702* | Y. Zeng, Q. Zou et al. | 2024 | Adversarial adaptive sampling (AAS); Wasserstein-guided point placement [^12] |
| Guo et al., *arXiv:2501.07700* | S. Guo et al. | 2025 | QR-DEIM adaptive collocation for Burgers and related PDEs [^14] |
| Badia et al., *arXiv:2211.12393* | S. Badia et al. | 2023 | Weak PINNs: dual-norm loss for hyperbolic conservation laws [^15] |

***

## 7. Discussion and Open Problems

**Combining AP structure with adaptive sampling** remains an open research direction. The standard RAD algorithm (Wu et al., 2022) was designed for well-posed, smooth PDE problems; its convergence analysis does not directly cover the $\varepsilon \to 0$ stiff limit. Extending the RAD sampling to properly balance collocation points between the "non-stiff" macroscopic equation and the "stiff" relaxation equation is non-trivial, particularly because the magnitudes of the two residuals $\mathcal{L}_{\mathrm{cons}}$ and $\mathcal{L}_{\mathrm{relax}}$ differ by $O(\varepsilon^2)$.[^3][^9]

**Fourier feature embeddings**  offer a complementary strategy for spectral bias: by replacing the standard $(x,t)$ input with a Fourier feature embedding $\gamma(x,t) = [\cos(2\pi B (x,t)^T), \sin(2\pi B (x,t)^T)]$ where $B$ is sampled from a chosen distribution, one can explicitly bias the network towards learning high-frequency content. This can be combined with the RelaxNN architecture without modifying the loss structure.[^6]

**Entropy-based loss terms** and the weak formulation (Badia et al., 2023)  offer a theoretically principled alternative: rather than relying on spectral bias mitigation via adaptive sampling, the loss is modified to be consistent with distributional solutions at shocks, capturing the Rankine–Hugoniot conditions automatically.[^15]

---

## References

1. [The relaxation schemes for systems of conservation laws in arbitrary ...](https://zendy.io/title/10.1002/cpa.3160480303) - We present a class of numerical schemes (called the relaxation schemes) for systems of conservation ...

2. [Jin-Xin relaxation as a shock-capturing method for high-order DG/FR schemes](https://arxiv.org/abs/2603.16290) - Jin-Xin relaxation is a method for approximating non-linear hyperbolic conservation laws by a linear...

3. [Commun. Comput. Phys.](https://doc.global-sci.org/uploads/Issue/CiCP/shortpdf/v35n3/353_693.pdf)

4. [Asymptotic-Preserving Neural Networks for hyperbolic systems with diffusive scaling](https://arxiv.org/abs/2210.09081v1)

5. [Asymptotic-Preserving Neural Networks for Multiscale Kinetic Equations](https://arxiv.org/html/2306.15381v4)

6. [[2012.10047] On the eigenvector bias of Fourier feature networks](https://arxiv.org/abs/2012.10047) - In this work we investigate this limitation through the lens of Neural Tangent Kernel (NTK) theory a...

7. [On the eigenvector bias of Fourier feature networks](https://www.sciencedirect.com/science/article/abs/pii/S0045782521002759) - In this work we investigate this limitation through the lens of Neural Tangent Kernel (NTK) theory a...

8. [Overview frequency principle/spectral bias in deep learning](https://ins.sjtu.edu.cn/people/xuzhiqin/pub/fpoverview2201.07395.pdf)

9. [A comprehensive study of non-adaptive and residual-based adaptive sampling for physics-informed neural networks](https://arxiv.org/abs/2207.10289) - Physics-informed neural networks (PINNs) have shown to be an effective tool for solving forward and ...

10. [Causality-guided adaptive sampling method for physics-informed neural
  networks](https://arxiv.org/html/2409.01536v1) - Compared to purely data-driven methods, a key feature of physics-informed
neural networks (PINNs) - ...

11. [Respecting causality is all you need for training physics-informed
  neural networks](https://arxiv.org/pdf/2203.07404.pdf) - While the popularity of physics-informed neural networks (PINNs) is steadily
rising, to this date PI...

12. [Adversarial Adaptive Sampling: Unify PINN and Optimal Transport for the
  Approximation of PDEs](https://arxiv.org/html/2305.18702v2) - ...achieved by implicitly embedding the Wasserstein
distance between the residual-induced distributi...

13. [PACMANN: Point Adaptive Collocation Method for Artificial Neural
  Networks](https://arxiv.org/pdf/2411.19632.pdf) - ...Differential Equations (PDEs) in both
forward and inverse problems. PINNs minimize a loss functio...

14. [An Adaptive Collocation Point Strategy For Physics Informed Neural
  Networks via the QR Discrete Empirical Interpolation Method](https://arxiv.org/html/2501.07700v1) - ...numerical methods, address this by dynamically updating collocation
points during training but ma...

15. [Improving Weak PINNs for Hyperbolic Conservation Laws: Dual Norm Computation, Boundary Conditions and Systems](https://arxiv.org/abs/2211.12393v2) - We consider the approximation of entropy solutions of nonlinear hyperbolic conservation laws using n...

16. [Journal of Computational Physics: M. Raissi, P. Perdikaris ...](https://www.scribd.com/document/970580149/Physics-Informed-Neural-Networks-a-Deep-Learning-Framework-for-Solving-Forward-and-Inverse-Problems-Involving-Nonlinear-Partial-Differential-Equations) - The document introduces physics-informed neural networks (PINNs), a framework that integrates physic...

