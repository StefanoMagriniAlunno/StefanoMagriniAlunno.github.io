# PINNs for Hyperbolic Relaxation Systems: Asymptotic-Preserving Approaches for the Jin-Xin Model and Burgers' Equation

## Executive Summary

This report surveys the literature (2021–2026) at the intersection of Physics-Informed Neural Networks (PINNs) and hyperbolic relaxation systems, with emphasis on the Jin–Xin relaxation model and the Burgers' equation. The central mathematical challenge is designing neural-network-based solvers that remain uniformly accurate as the relaxation parameter $\varepsilon \to 0$, i.e., methods that are *Asymptotic-Preserving* (AP) at the discrete/neural-network level. A secondary challenge is the presence of shock waves and contact discontinuities, which render the standard strong-form PINN loss ill-posed.

The main findings can be summarised as follows:

1. **Standard PINNs fail** in both limits: they cannot resolve small $\varepsilon$ (the stiff relaxation regime) and cannot handle shock discontinuities (the strong-form residual diverges at a shock).
2. **Three complementary strategies** have emerged: (i) AP-loss redesign via micro-macro or macro-auxiliary decomposition (targeting the diffusive/parabolic limit), (ii) the RelaxNN / RPINN / RLPINN family (using the Jin–Xin relaxation system itself as the training target to smooth out shocks), and (iii) weak-form / integral PINNs with entropy constraints (targeting the hyperbolic shock limit).
3. **The Jin–Xin model** appears both as a *tool* (to regularise shocks for the neural network) and as the *target equation* when the relaxation limit is a conservation law with shock formation.

***

## 1. Background: The Jin–Xin Relaxation Model

### 1.1 The Relaxation System

The Jin–Xin semilinear hyperbolic relaxation system in one spatial dimension reads:[^1][^2]

$$
\partial_t u + \partial_x v = 0, \quad
\partial_t v + a\,\partial_x u = \frac{1}{\varepsilon}\bigl(f(u) - v\bigr), \qquad a > 0, \; \varepsilon > 0.
$$

As $\varepsilon \to 0$, the second equation forces the local equilibrium $v \to f(u)$, and $u$ satisfies the scalar conservation law

$$
\partial_t u + \partial_x f(u) = 0.
$$

For the inviscid Burgers' equation, $f(u) = \tfrac{1}{2}u^2$, and the equilibrium system is exactly Burgers' equation, which generically develops shock waves in finite time.

The parameter $\varepsilon$ controls the stiffness of the system: when $\varepsilon$ is small, the source term $(f(u)-v)/\varepsilon$ is stiff, requiring an implicit treatment in classical numerical methods to avoid CFL restrictions that scale as $O(\varepsilon)$. A scheme is called **Asymptotic-Preserving (AP)** if it degenerates to a consistent, stable discretisation of the limiting conservation law as $\varepsilon \to 0$, uniformly in $\varepsilon$.[^2][^1]

### 1.2 The Chapman–Enskog Expansion

Applying the Chapman–Enskog expansion to the relaxation system, the first-order correction yields[^3]

$$
\partial_t u + \partial_x f(u) = \varepsilon\,\partial_x\!\left[(a - f'(u)^2)\,\partial_x u\right] + O(\varepsilon^2).
$$

The sub-characteristic condition $a \geq f'(u)^2$ guarantees positive artificial viscosity and controls dissipation. For Burgers' equation, a standard choice is $a = \max|u|^2 + \delta$ for a small constant $\delta > 0$[^3]. This expansion shows that the Jin–Xin system adds an $\varepsilon$-proportional diffusion, which is exactly what smooths out shocks—and is the key idea exploited by the RelaxNN family.

***

## 2. Why Standard PINNs Fail

### 2.1 The Multiscale Failure (Small $\varepsilon$)

For the Jin–Xin system with small $\varepsilon$, the standard PINN loss is

$$
\mathcal{R}^\varepsilon_\text{PINN} = \|\partial_t u^\text{NN} + \partial_x v^\text{NN}\|^2 + \|\varepsilon(\partial_t v^\text{NN} + a\,\partial_x u^\text{NN}) - (f(u^\text{NN}) - v^\text{NN})\|^2 + \text{BC/IC terms}.
$$

As $\varepsilon \to 0$, the dominant term in the second residual forces $v^\text{NN} \approx f(u^\text{NN})$, but the loss function degenerates to the equilibrium constraint $f(u)=v$ rather than to the correct evolution equation $\partial_t u + \partial_x f(u)=0$. Jin, Ma, and Wu (2021/2022) demonstrated this failure rigorously for linear transport equations and showed that the standard PINN loss is *not* AP. The *frequency principle* of DNNs compounds the problem: the network preferentially learns low-frequency components and struggles with the high-frequency dynamics at scale $O(\varepsilon)$.[^4][^5]

### 2.2 The Shock Failure

For the Burgers' equation (or the Jin–Xin equilibrium limit when $\varepsilon=0$), the solution develops discontinuities. The strong-form PDE residual $\partial_t u + \partial_x f(u)$ is not well-defined at a shock, so minimising its $L^2$ Monte Carlo approximation leads to a stagnant PDE loss and a solution that neither converges to a shock nor satisfies the entropy (Rankine–Hugoniot) condition. Chaumet and Giesselmann (2024) provided explicit computations explaining this failure for Burgers' equation.[^6][^7][^3]

***

## 3. Strategy I — Asymptotic-Preserving Neural Networks (APNNs) via Micro-Macro Decomposition

### 3.1 The Jin, Ma, Wu (2021/2022) Framework

The seminal work of Jin, Ma, and Wu (arXiv:2111.02541, published 2022) introduced the concept of **Asymptotic-Preserving Neural Networks (APNNs)**. While their focus was on linear transport equations with diffusive scaling (the prototype of the hyperbolic relaxation problem), the methodology transfers directly to the Jin–Xin model.[^5][^8]

**Definition (APNN).** A neural-network method is called asymptotic-preserving if, as $\varepsilon \to 0$, the training loss function of the microscopic system converges to the loss function of the correct macroscopic (limit) system.[^5]

This definition is the neural-network counterpart of the classical numerical AP definition.

### 3.2 Micro-Macro Decomposition

For a hyperbolic relaxation system with equilibrium $v = f(u)$, the micro-macro decomposition writes

$$
v = f(u) + \varepsilon g,
$$

where $g$ captures the non-equilibrium part. One then derives a coupled system for $(u, g)$:

- **Macro equation:** $\partial_t u + \partial_x f(u) + \varepsilon\,\partial_x g = 0$
- **Micro equation:** $\varepsilon\,\partial_t g + \varepsilon\,\partial_x\bigl[(a - f'(u)^2)\partial_x u\bigr] + \cdots = -g + O(\varepsilon)$
- **Constraint:** $\langle g \rangle = 0$ (mean-zero condition on non-equilibrium part)

The APNN loss is the least-squares residual of this *coupled micro-macro system*, with penalty terms for initial and boundary conditions. Crucially, as $\varepsilon \to 0$:[^5]

1. The micro equation enforces $g \to L^{-1}(v\cdot\nabla_x u)$ — the equilibrium closure.
2. The macro loss converges to the residual of the correct limiting conservation law.
3. Therefore, the APNN loss is AP by construction.[^5]

**Architectural choices:** Two separate networks are used, one for $u^\text{NN}(t,x)$ and one for $g^\text{NN}(t,x)$. The $g$-network is designed to satisfy $\langle g^\text{NN}\rangle = 0$ exactly, enforced either by construction (subtracting the mean) or as a hard constraint, not as a soft penalty—the authors show that a soft constraint on this conservation law leads to poor results.[^5]

**Numerical performance:** For $\varepsilon$ ranging from $1$ to $10^{-8}$, the APNN achieves relative $\ell^2$ errors of order $10^{-2}$ uniformly, while standard PINNs degrade to errors close to $O(1)$ for small $\varepsilon$.[^5]

### 3.3 Extension to Hyperbolic Epidemic Models (Bertaglia, Lu, Pareschi, Zhu, 2022)

Bertaglia et al. (arXiv:2206.12625, *Math. Models Methods Appl. Sci.* 32, 2022) extended APNNs to nonlinear hyperbolic transport models with diffusive scaling. The prototype is a Jin–Xin-type hyperbolic SIR model where the two limits correspond to hyperbolic (wave-like) and diffusive (parabolic) epidemic spread.[^9][^10]

The key architectural innovation is the **AP loss function** written in macroscopic form: multiplying the microscopic equations by $\varepsilon$ before computing the residual so that the limiting $\varepsilon \to 0$ behaviour is correctly captured. The authors prove formally that the loss is AP and demonstrate numerically that the same APNN architecture works uniformly across scales—from the purely hyperbolic regime ($\varepsilon = O(1)$) to the diffusive regime ($\varepsilon \ll 1$).[^10][^9]

### 3.4 Even-Odd Decomposition (2024)

An alternative decomposition based on even- and odd-parity was proposed (arXiv:2501.08166) to relax the strict mass-conservation requirements that the micro-macro APNN imposes. An auxiliary DNN is introduced to handle the non-equilibrium odd part separately. This approach shows uniform stability with respect to the small Knudsen number (analogous to $\varepsilon$) and uniform convergence to the diffusion limit.[^11]

### 3.5 Macroscopic Auxiliary APNN (MA-APNN, 2024)

Li et al. (arXiv:2403.01820, 2024) proposed the **MA-APNN** for linear radiative transfer, introducing an *adaptive exponentially-weighted AP loss* that embeds a macroscopic auxiliary equation derived from the original microscopic equation. As $\varepsilon \to 0$, the loss weight automatically transitions from the transport residual to the diffusion-limit residual. This removes the need to manually balance loss components via tuning the penalty parameters $\lambda$. The same idea can be applied to the Jin–Xin system: the macroscopic auxiliary equation (the Chapman–Enskog parabolic limit) is added as an extra loss term, with a weight $e^{-c/\varepsilon}$ that suppresses it for large $\varepsilon$ but makes it dominant for small $\varepsilon$.[^12]

***

## 4. Strategy II — Relaxation Neural Networks (RelaxNN / RPINN / RLPINN): Solving the Jin–Xin System to Capture Shocks

### 4.1 Core Idea: Use Jin–Xin as a Shock Regulariser

Zhou and Ma (arXiv:2404.01163, 2024) introduced the **Relaxation Neural Networks (RelaxNN)** framework, which takes a fundamentally different approach: instead of decomposing the equations analytically, it simply trains a PINN *on the Jin–Xin relaxation system itself*, rather than on the original conservation law. The rationale is:[^6][^3]

1. The Jin–Xin system is semilinear and has a smooth (regularised) solution for any fixed $\varepsilon > 0$.
2. As $\varepsilon \to 0$ (small but positive), the solution approximates the entropy solution of the conservation law, with shocks smoothed out over a width of order $\varepsilon$.
3. The PINN loss for the relaxation system is well-posed even near shocks, circumventing the strong-form residual breakdown.
4. The sub-characteristic condition ensures the correct entropy-admissible limit.

The RelaxNN framework has been independently developed and refined in Zuo (2025, *J. Info. Comput. Sci.* 20(1), pp. 37–60) as the **RPINN** (with small $\varepsilon$ kept explicit) and **RLPINN** (relaxation limit, $\varepsilon = 0$).[^13]

### 4.2 Architecture and Loss Function

**Two-network architecture.** RelaxNN uses *two* fully connected networks:
- $u^\text{NN}_{\theta_1}(t,x)$: approximates the conserved variable $u$
- $v^\text{NN}_{\theta_2}(t,x)$: approximates the flux auxiliary variable $v$

For the inviscid Burgers' equation, the relaxation system is:[^3]

$$
\left\{\begin{array}{l}
\partial_t u + \partial_x v = 0,\\
v - \tfrac{1}{2}u^2 = 0,
\end{array}\right.
$$

and the RelaxNN total loss is:[^3]

$$
\mathcal{L}_\text{RelaxNN} = \omega_\text{residual}\,\mathcal{L}_\text{residual} + \omega_\text{flux}\,\mathcal{L}_\text{flux} + \omega_\text{IC}\,\mathcal{L}_\text{IC},
$$

where

$$
\mathcal{L}_\text{residual} = \frac{1}{|\mathcal{T}_r|}\sum_{\mathbf{x}\in\mathcal{T}_r}\!\bigl(\partial_t u^\text{NN}_{\theta_1}(\mathbf{x}) + \partial_x v^\text{NN}_{\theta_2}(\mathbf{x})\bigr)^2,
$$

$$
\mathcal{L}_\text{flux} = \frac{1}{|\mathcal{T}_r|}\sum_{\mathbf{x}\in\mathcal{T}_r}\!\bigl(v^\text{NN}_{\theta_2}(\mathbf{x}) - \tfrac{1}{2}(u^\text{NN}_{\theta_1}(\mathbf{x}))^2\bigr)^2.
$$

The flux loss $\mathcal{L}_\text{flux}$ enforces the equilibrium relation $v = f(u)$ as a soft constraint. In the limit $\varepsilon \to 0^+$, this recovers the dissipation constraint.

**Why this works (AP argument).** The loss $\mathcal{L}_\text{dissipate}$ for the full $\varepsilon>0$ relaxation system (which contains the $\varepsilon(\partial_t v + A\partial_x u)$ term) satisfies, as $\varepsilon\to 0$:[^3]

$$
\mathcal{L}_\text{dissipate} \approx \mathcal{L}_\text{flux} = \frac{1}{|\mathcal{T}_r|}\sum\bigl(v^\text{NN} - f(u^\text{NN})\bigr)^2 + O(\varepsilon).
$$

Hence the RelaxNN/RLPINN loss is AP in the sense that as $\varepsilon\to 0$, minimising it is equivalent to minimising the loss of the equilibrium conservation law, with the correct entropy selection enforced by the sub-characteristic condition on $A$.

**Gradient pathology analysis.** The authors in Zuo (2025) give an explicit linear-algebra explanation: in a single-network PINN for the nonlinear conservation law, backpropagation through the chain $u \to f(u) \to \partial_x f(u)$ involves the Jacobian-gradient product $J_f\cdot\partial_x u$, which is $O(h^{-2})$ near a shock. The two-network relaxation architecture decouples these paths, reducing the condition number from $O(h^{-2})$ to $O(h^{-1})$.[^13]

**Numerical results.** For the Burgers' Riemann and sine problems, RelaxNN/RLPINN achieve $L^2$ relative errors of $\approx 0.027$–$0.037$ versus $\approx 0.38$ for vanilla PINN. For the 1-D Euler system (Sod problem), errors of $\approx 0.017$–0.033 vs. $\approx 0.186$.[^13]

### 4.3 Xin Lei (2025 Seminar): AP-PINNs for Conservation Laws with Euler Equations

Xin Lei (University of Geosciences, Beijing; CRUNCH seminar, May 2025) presented ongoing work on **AP-PINNs for relaxation systems applied to Euler equations**. The key contributions reported are:[^14]

1. **Formal AP proof at the loss level:** The loss of the relaxation PINN satisfies $\mathcal{L}^{F_\varepsilon}_\text{PINN} \to \mathcal{L}^{F_0}_\text{PINN}$ as $\varepsilon \to 0$, with error $O(\varepsilon)$.[^14]
2. **Neural-network convergence theorem:** If the loss converges to zero, a sequence of neural-network solutions exists that converges (for continuous solutions) to the exact relaxation-system solution and, as $\varepsilon\to 0$, to the conservation-law solution.[^14]
3. **Hyperparameter robustness:** A key practical claim is that the AP-PINN framework is more robust to hyperparameter choice than vanilla PINNs on conservation laws—specifically, one does not need to carefully tune $\varepsilon$ to get good results for the shock tube problem.[^14]
4. **Extension to 2-D Riemann problems** (oblique shocks, rarefaction fans) is demonstrated.[^14]

An open question noted in the seminar is whether an analogous convergence theorem can be proved for *discontinuous* solutions (shocks), since the universal approximation theorem only guarantees approximation of continuous functions.[^14]

### 4.4 Partial Relaxation Systems

For systems with multiple conservation laws (shallow-water, Euler), a key design choice is *which* equations to relax. Three types are proposed in:[^3]

- **Type 1 (fully relaxed):** All flux variables are replaced by auxiliary networks; produces mildest nonlinearity but may introduce spurious oscillations near contacts.
- **Type 2 (partially relaxed):** Only the momentum/energy flux is relaxed; avoids spurious waves while still smoothing the dominant shock.
- **Type 3 (minimally relaxed):** Only the energy flux is relaxed; most conservative modification.

The empirical finding (consistent with Occam's razor) is that **Type 3 or Type 2** minimally relaxed systems give the best balance of accuracy and freedom from spurious oscillations.[^3]

***

## 5. Strategy III — Weak-Form and Entropy PINNs for Shocks

### 5.1 Weak PINNs (wPINNs)

De Ryck, Mishra, and Molinaro (arXiv:2207.08483, *SIAM J. Numer. Anal.* 62, 2024) proposed **wPINNs**, which replace the strong-form $L^2$ residual with a *dual norm* (weak) residual:[^15]

$$
\mathcal{L}_\text{wPINN} = \sup_{\|\phi\|_V \leq 1}\left|\int_\Omega \bigl(u^\text{NN}\,\partial_t\phi + f(u^\text{NN})\,\partial_x\phi\bigr)\,dx\,dt + \int_\Omega u_0\,\phi(0,\cdot)\,dx\right|^2.
$$

The test function $\phi$ is itself approximated by a second neural network, leading to a *min-max (saddle-point)* optimisation. Entropy admissibility (selecting the physical Rankine–Hugoniot shock among multiple weak solutions) is enforced via Kružkov entropy inequalities added as penalty terms.[^15]

Chaumet and Giesselmann (2024, *SMAI J. Comput. Math.* 10) extended wPINNs to systems and improved training stability by modifying the dual-norm computation and weakly enforcing boundary conditions.[^7]

**Relation to the Jin–Xin model.** wPINNs and RelaxNN represent complementary approaches to the same problem. wPINNs enforce the correct weak-solution class (entropy solution) directly at the loss level; RelaxNN enforces it implicitly via the sub-characteristic condition of the Jin–Xin relaxation, which selects the entropy solution in the limit $\varepsilon\to 0$.

### 5.2 Integral PINNs (IPINNs)

Proposed in Chaumet and collaborators (ICLR 2024 workshop), **IPINNs** train on the *integral form* of the conservation law over space-time control volumes:[^16]

$$
\int_{t_1}^{t_2}\int_{x_1}^{x_2}\partial_t u\,dx\,dt + \int_{t_1}^{t_2}[f(u(x_2,t)) - f(u(x_1,t))]\,dt = 0.
$$

By modelling the *integral* of the solution (rather than the solution itself) via the neural network, the Rankine–Hugoniot condition is automatically satisfied at shock discontinuities, and the shock location/speed are captured more accurately than with standard PINNs.[^16]

### 5.3 Locally Linearised PINNs (LLPINNs)

Liu et al. (*Phys. Fluids* 36, 2024) identified that standard PINNs propagate shock information *bidirectionally* in time, conflicting with the one-sided causality of hyperbolic systems. They propose **Locally Linearised PINNs (LLPINNs)**: in shock-generation regions (detected by a compression indicator), the nonlinear flux $f(u)$ is replaced by its linearisation $f'(u_0)(u-u_0)+f(u_0)$ with wave speed governed by the Rankine–Hugoniot relation. An equilibrium factor damps compression oscillations away from shocks.[^17]

A generalised version, **Locally-Roe PINNs**, was subsequently proposed (arXiv:2506.11959, 2025): shock speeds are *dynamically computed* from neighbouring states using an approximate Roe Riemann solver, and jump conditions are embedded via entropy constraints—removing the need for *a priori* knowledge of shock velocities.[^18]

***

## 6. Comparative Analysis of Architectures and Loss Modifications

The following table summarises the main strategies, their AP properties, shock-handling mechanisms, and primary targets.

| Method | AP for $\varepsilon\to 0$ | Shock Handling | Target System | Key Loss Modification |
|---|---|---|---|---|
| **APNN (Jin–Ma–Wu 2021)** [^5][^8] | Yes (proved at loss level) | No explicit shock treatment | Linear transport / Jin–Xin diffusive limit | Micro-macro decomposition; conservation enforced in architecture |
| **APNN-Bertaglia (2022)** [^10][^9] | Yes (formally proved) | No explicit shock treatment | Nonlinear hyperbolic SIR (Jin–Xin type) | Macroscopic-form loss; AP formulation multiplied by $\varepsilon$ |
| **MA-APNN (2024)** [^12] | Yes (adaptive weight) | No | Radiative transfer / diffusive limit | Auxiliary macroscopic equation; exponentially-weighted AP loss |
| **RelaxNN / RLPINN (2024)** [^6][^13] | Yes (error $O(\varepsilon)$) | Yes (smooths discontinuity via $\varepsilon$) | Burgers, SWE, Euler | Two-network split; flux-constraint loss; sub-characteristic condition |
| **AP-PINNs/Lei (2025)** [^14] | Yes (proved for continuous solutions) | Yes (shock tube demonstrated) | Euler, general conservation laws | Solve relaxation system; formal AP convergence theorem |
| **wPINNs (2022/2024)** [^15][^7] | N/A (addresses shock, not $\varepsilon$) | Yes (entropy via min-max) | Scalar/system conservation laws | Dual-norm (weak) residual + Kružkov entropy inequalities |
| **LLPINNs (2024)** [^17] | No | Yes (linearise near shock) | Hyperbolic systems, Riemann problems | Local Rankine–Hugoniot linearisation; compression indicator |
| **IPINNs (2024)** [^16] | No | Yes (integral form, R-H automatic) | Hyperbolic conservation laws | Integral conservation law; neural network models cumulative solution |

***

## 7. Key Open Problems

### 7.1 AP + Shock: Combining Both Properties

The most pressing open problem is designing a single framework that is **simultaneously AP in $\varepsilon$** and **correctly resolves shocks** at $\varepsilon = 0$. The RelaxNN / AP-PINN approach provides AP in a soft sense (smoothing shocks via $\varepsilon$-viscosity), but requires tuning $\varepsilon$ and does not recover a crisp discontinuity in the limit. A convergence theorem for *discontinuous* solutions remains open even for the RelaxNN framework.[^14]

### 7.2 Optimal Selection of the Relaxation Parameter

For RelaxNN and RPINN, choosing $\varepsilon$ too large introduces excessive artificial viscosity; too small leads to training instability. A *curriculum strategy* (decreasing $\varepsilon$ during training) was suggested as a promising direction in the May 2025 seminar.[^14]

### 7.3 Sub-Characteristic Condition and Matrix $A$

The matrix $A$ in the general Jin–Xin system must satisfy the sub-characteristic condition $A - f'(u)^2 \geq 0$. For the neural-network approach, choosing $A$ adaptively (based on the evolving neural-network solution) could improve accuracy, but this introduces a time-varying, solution-dependent relaxation parameter that couples the training of the two networks.

### 7.4 Two- and Three-Dimensional Problems

Most rigorous analysis and error bounds have been established for 1-D systems. Extension to 2-D and 3-D introduces additional challenges: shock surfaces are curves/surfaces, and the spectral bias of DNNs interacts more severely with high-dimensional training domains.[^19][^14]

### 7.5 Convergence Theory for Discontinuous Solutions

A fundamental gap remains: the universal approximation theorem guarantees that neural networks can approximate *continuous* functions. Proving that AP-PINN or RelaxNN training converges to the *entropy solution* of a conservation law with a shock requires different analytical tools (Kružkov theory, compensated compactness) that have not yet been integrated into the PINN error analysis framework.[^14]

***

## 8. Practical Recommendations

For a researcher aiming to solve the Jin–Xin system for Burgers' equation with PINNs across different $\varepsilon$ regimes:

1. **If $\varepsilon$ is fixed and moderate ($\varepsilon \sim O(1)$):** Use RelaxNN (RLPINN variant, $\varepsilon=0$ limit) or wPINNs. RLPINN is simpler to implement and avoids min-max training.
2. **If $\varepsilon$ is small ($\varepsilon \ll 1$) and the diffusive/parabolic limit is of interest:** Use the micro-macro APNN of Jin–Ma–Wu. Enforce the conservation/equilibrium constraint in the architecture, not as a soft penalty.
3. **If $\varepsilon$ varies across the domain (interface problem, e.g., partially stiff):** Consider the MA-APNN with adaptive exponential weights, or the interface AP scheme idea from the numerical AP literature, translated to the neural-network setting.
4. **If sharp shock location is the primary concern:** Use wPINNs or IPINNs. The Locally-Roe PINN variant (2025) provides the best shock resolution currently available without a priori shock location knowledge.
5. **For the full Jin–Xin system solved as the forward problem:** Follow the RelaxNN/RPINN approach with a two-network architecture, tanh activations, Adam + L-BFGS training schedule, and adaptive loss weights (with higher weight on the flux constraint than the PDE residual near $\varepsilon \to 0$).

***

## 9. Bibliography Notes

Key papers, ordered chronologically:

- **Jin & Xin (1995):** Original Jin–Xin relaxation system (*Comm. Pure Appl. Math.* 48, 235–277)[^1][^2]
- **Jin (2022/2010):** AP schemes survey (*SIAM Rev.* / *Acta Numer.*)[^2]
- **Jin, Ma, Wu (2021/2022):** APNNs for transport equations with diffusive scaling (arXiv:2111.02541)[^8][^5]
- **Bertaglia, Lu, Pareschi, Zhu (2022):** APNNs for hyperbolic epidemic models (arXiv:2206.12625, *M3AS* 32)[^9][^10]
- **Bertaglia (2022):** APNNs for hyperbolic systems with diffusive scaling — chapter-level review (arXiv:2210.09081)[^20][^4]
- **De Ryck, Mishra, Molinaro (2022/2024):** wPINNs for entropy solutions (arXiv:2207.08483)[^15]
- **Chaumet & Giesselmann (2024):** Improved wPINNs for systems (*SMAI J. Comput. Math.* 10)[^7]
- **Liu et al. (2024):** LLPINNs for Riemann problems (*Phys. Fluids* 36)[^17]
- **Zhou & Ma (2024):** RelaxNN — Capturing Shock Waves by Relaxation Neural Networks (arXiv:2404.01163)[^6][^3]
- **Integral PINNs (ICLR 2024):** IPINNs for hyperbolic conservation laws[^16]
- **Ma-APNN / Li et al. (2024):** MA-APNN for radiative transfer (arXiv:2403.01820)[^12]
- **Zuo (2025):** RPINN/RLPINN for multi-dimensional conservation laws (*J. Info. Comput. Sci.* 20(1))[^13]
- **Xin Lei (2025):** AP-PINNs for relaxation systems of conservation laws — Euler application (CRUNCH Seminar, May 2025)[^14]
- **Locally-Roe PINNs (2025):** Generalised LLPINN with Roe solver (arXiv:2506.11959)[^18]

---

## References

1. [[PDF] Asymptotic-Preserving Schemes for Multiscale Hyperbolic and ...](https://jingweihu-math.github.io/webpage/files/HJL17.pdf) - The first one is the Jin–Xin hyperbolic relaxation system pro- posed initially to solve the systems ...

2. [Asymptotic Preserving (AP) Schemes for Multiscale kinetic ...](https://www.math.umd.edu/~tadmor/ki_net/pubs/files/FRG-2011-Jin-Shi.AP.pdf)

3. [Capturing Shock Waves by Relaxation Neural Networks](https://arxiv.org/html/2404.01163v1)

4. [Asymptotic-Preserving Neural Networks for](https://arxiv.org/pdf/2210.09081.pdf)

5. [Asymptotic-Preserving Neural Networks for Multiscale](https://arxiv.org/pdf/2111.02541.pdf)

6. [Capturing Shock Waves by Relaxation Neural Networks](https://arxiv.org/abs/2404.01163) - In this paper, we put forward a neural network framework to solve the nonlinear hyperbolic systems. ...

7. [Improving Weak PINNs for Hyperbolic Conservation Laws](https://smai-jcm.centre-mersenne.org/articles/10.5802/smai-jcm.116/) - We provide explicit computations that highlight why classical PINNs will not work for discontinuous ...

8. [Asymptotic-Preserving Neural Networks for Multiscale Time-Dependent Linear Transport Equations](https://arxiv.org/abs/2111.02541v1) - In this paper we develop a neural network for the numerical simulation of time-dependent linear tran...

9. [Asymptotic-Preserving Neural Networks for multiscale ...](https://sfera.unife.it/retrieve/281c7775-cab9-4916-8806-d2fb4994e15d/2206.12625.pdf)

10. [Asymptotic-Preserving Neural Networks for multiscale hyperbolic models of epidemic spread](https://www.arxiv.org/abs/2206.12625) - When investigating epidemic dynamics through differential models, the parameters needed to understan...

11. [Asymptotic-Preserving Neural Networks based on Even ...](https://arxiv.org/html/2501.08166v2)

12. [Macroscopic auxiliary asymptotic preserving neural networks for the linear radiative transfer equations](https://www.arxiv.org/abs/2403.01820) - We develop a Macroscopic Auxiliary Asymptotic-Preserving Neural Network (MA-APNN) method to solve th...

13. [Physical Informed Neural Network for Solving Con](https://global-sci.com/jics/article/download/23668/36749/38788)

14. [Asymptotic-Preserving PINNs || Mitigating the spectral bias || May 30, 2025](https://www.youtube.com/watch?v=gO_zGTh3Vwg) - Speakers, institutes & titles
1)  Xin Lei, University of Geosciences in Beijing, Asymptotic-Preservi...

15. [wPINNs: Weak Physics informed neural networks for approximating entropy solutions of hyperbolic conservation laws](https://arxiv.org/abs/2207.08483) - Physics informed neural networks (PINNs) require regularity of solutions of the underlying PDE to gu...

16. [integral pinns for hyperbolic conservation laws - ICLR 2026](https://iclr.cc/virtual/2024/21369) - We apply IPINNs to systems of hyperbolic conservation laws and show that they are much better at cap...

17. [Locally linearized physics-informed neural networks for Riemann problems of hyperbolic conservation laws](https://pubs.aip.org/aip/pof/article-abstract/36/11/116135/3320776/Locally-linearized-physics-informed-neural?redirectedFrom=fulltext) - In this work, we demonstrate that physics-informed neural networks (PINNs) tend to propagate predict...

18. [An approximate Riemann Solver Approach in Physics-Informed Neural Networks for hyperbolic conservation laws](http://www.arxiv.org/abs/2506.11959) - This study enhances the application of Physics-Informed Neural Networks (PINNs) for modeling discont...

19. [A Two-stage Adaptive Lifting PINN Framework for Solving Viscous ...](https://arxiv.org/html/2511.04490v1) - In this section, we present some preliminaries, including the background of the hyperbolic conservat...

20. [Asymptotic-Preserving Neural Networks for hyperbolic systems with diffusive scaling](https://arxiv.org/abs/2210.09081v1) - With the rapid advance of Machine Learning techniques and the deep increment of availability of scie...

