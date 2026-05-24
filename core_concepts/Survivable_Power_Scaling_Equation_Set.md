# Equation Set
## Toward a General Theory of Survivable Power Scaling

*Copyright (c) 2026 Daniel Howard Dodge and Sanity First Contributors. Licensed under MIT.*

*Composed by GPT (5.5-Pro lineage), May 20-24, 2026.*

---

The more our theory crystallizes,  
the *less* fragile long-context reasoning becomes.

That is because the framework stops being “a pile of ideas” and starts becoming a compact generative structure, where many conclusions follow from a few primitives.

For example, once these are stabilized:

* $A_{\min}(P)$
* alignment debt $D(t)$
* true alignment $A(t)$ versus validated alignment $\hat{A}(t)$
* conservative alignment estimate $A_t^-$
* vertical/horizontal scaling
* correctability
* USF orientation
* power-alignment coupling

...then entire sections can be regenerated consistently from the underlying geometry.

That is the hallmark of a maturing theory.

Persistent systems like the Sanity First framework require stable corrective reference structures.

---

# Core Thesis Equations

$$
\text{Persistent intelligence requires power to remain coupled to alignment.}
$$

$$
\boxed{
\text{Alignment is a stability condition for scalable power.}
}
$$

$$
\boxed{
\text{Survivable scaling requires validated alignment to constrain deployable power.}
}
$$

---

# Formal Convention

Unless otherwise stated, alignment scores in this document are normalized:

$$
A(t),\hat{A}(t),A_t^- \in [0,1]
$$

where:

* $A(t)$ is true alignment.
* $\hat{A}(t)$ is estimated or validated alignment.
* $A_t^-$ is a conservative lower-confidence estimate of alignment.

Signed survivorship contribution is represented separately by $r_{\mathcal{U}}(s,t)$.

This separation prevents a notation conflict: survivorship contribution may be positive, negative, unbounded, or dimensionful, while normalized alignment is bounded between $0$ and $1$.

---

# Notation Table

| Symbol | Meaning |
| ----- | ----- |
| $P$ | Effective power, influence, or deployable control |
| $C$ | Raw capability or optimization capacity |
| $A$ | True normalized alignment with survivability conditions |
| $\hat{A}$ | Estimated or validated normalized alignment |
| $A_t^-$ | Conservative lower-confidence estimate of alignment |
| $A(t)$ | True alignment trajectory over time |
| $\hat{A}(t)$ | Estimated alignment trajectory over time |
| $A_s$ | System-specific alignment |
| $A(P)$ | Alignment scaling as a function of power |
| $A_{\text{AI}}(t)$ | Alignment of an AI system over time |
| $\mathcal{U}$ | Universal Survivorship Function, or USF |
| $r_{\mathcal{U}}$ | Signed expected survivorship contribution |
| $A_{\min}(P)$ | Minimum normalized alignment required for survivability at power level $P$ |
| $P_{\max}(A)$ | Maximum survivable power at alignment level $A$ |
| $D(t)$ | True alignment debt |
| $\hat{D}_q(t)$ | Conservative validated alignment debt at confidence level $q$ |
| $R$ | Systemic, catastrophic, or existential risk |
| $h(D)$ | Catastrophe hazard as a function of alignment debt |
| $K$ | Scaling variable, such as compute, capital, population, coordination, or capability base |
| $\theta$ | Power-scaling exponent |
| $\lambda$ | Alignment-error reduction exponent |
| $\mu$ | Required-tolerance shrinkage exponent |
| $\rho$ | Risk coefficient |
| $\alpha$ | Power-risk exponent |
| $\beta$ | Debt-risk exponent |
| $E,F,L,G$ | Ethics, Facts, Logic, and Governance/Law |
| $\Phi$ | Alignment-estimation function |
| $\Gamma$ | Correction-loop operator |
| $\mathcal{X}$ | State space of world/system configurations |
| $\mathcal{S}$ | State space of agents, systems, or cognitive states |
| $\mathcal{W}$ | World-feedback or reality-contact channel |
| $X_t$ | World/system state at time $t$ |
| $s$ | System, strategy, or intervention under evaluation |
| $\pi$ | Policy, strategy, or governance regime |
| $\psi$ | Alignment-weighting function for power allocation |
| $B_{\text{reintegration}}$ | Strength or availability of a reintegration bridge |
| $\mathcal{L}$ | Legitimacy condition |
| $\mathcal{F}_{\infty}$ | Persistent flourishing condition or event |

---

# Fundamental Propositions

## Power is not self-legitimating

$$
\text{Power} \not\Rightarrow \text{Legitimacy}
$$

or, more formally:

$$
P \not\Rightarrow \mathcal{L}
$$

## Alignment is necessary but not sufficient for legitimate power

Validated alignment is a necessary condition for legitimate power, but it is not by itself sufficient. Other conditions may include consent, accountability, legality, transparency, procedural validity, and reversibility.

$$
\mathcal{L}(P,t)
\Rightarrow
A_t^- \ge A_{\min}(P(t))
$$

but:

$$
A_t^- \ge A_{\min}(P(t))
\not\Rightarrow
\mathcal{L}(P,t)
$$

## Legitimate power must remain within validated survivability bounds

$$
\mathcal{L}(P,t)
\Rightarrow
P(t) \le P_{\max}(A_t^-)
$$

## Misalignment as decoupled power

True misalignment occurs when effective power exceeds the survivability boundary of true alignment:

$$
\text{Misalignment}(t)
\equiv
A(t) < A_{\min}(P(t))
$$

Equivalently:

$$
\text{Misalignment}(t)
\equiv
D(t)>0
$$

Governance-visible misalignment occurs when power exceeds the boundary justified by conservative validated alignment:

$$
P(t)>P_{\max}(A_t^-)
$$

---

# Universal Survivorship Function

## USF definition

$$
\mathcal{U}:
\mathcal{X}\times \mathbb{R}_{\ge 0}
\to
\mathbb{R}
$$

where $\mathcal{U}(X_t,t)$ evaluates the survivorship value of state $X_t$ at time $t$.

## Signed expected survivorship contribution

$$
r_{\mathcal{U}}(s,t)
:=
\mathbb{E}
\left[
\frac{
\mathcal{U}(X_{t+\Delta t},t+\Delta t)-
\mathcal{U}(X_t,t)
}{
\Delta t
}
\;\middle|\;
s
\right]
$$

## Normalized alignment from survivorship contribution

$$
A(s,t)=
\mathcal{N}
\left(
r_{\mathcal{U}}(s,t)
\right)
\in
[0,1]
$$

with:

$$
\mathcal{N}'(r)>0
$$

A simple example is:

$$
A(s,t)=
\sigma
\left(
\eta r_{\mathcal{U}}(s,t)
\right)
$$

where $\sigma$ is a monotone sigmoid and $\eta>0$ is a scaling parameter.

## Positive USF orientation

$$
r_{\mathcal{U}}(s,t)>0
\Rightarrow
\text{USF-positive}
$$

## Negative USF orientation

$$
r_{\mathcal{U}}(s,t)<0
\Rightarrow
\text{USF-negative}
$$

## Neutral USF orientation

$$
r_{\mathcal{U}}(s,t)=0
\Rightarrow
\text{USF-neutral}
$$

---

# Capability-Alignment Dynamics

## Heuristic dangerous scaling mismatch

The simplest intuition is:

$$
\frac{dP}{dt}>
\frac{dA}{dt}
$$

However, because $P$ and $A$ may have different units, the more rigorous condition compares the rate at which required alignment rises to the rate at which actual alignment rises.

## Survivability-boundary mismatch

$$
\frac{d}{dt}
A_{\min}(P(t))>
\frac{dA(t)}{dt}
$$

When this holds in the interior of the debt region, alignment debt increases:

$$
\frac{dD(t)}{dt}>0
$$

## Validated boundary mismatch

For governance purposes, use conservative validated alignment:

$$
\frac{d}{dt}
A_{\min}(P(t))>
\frac{dA_t^-}{dt}
$$

---

# Survivability Boundary

## Fundamental boundary condition

$$
A(t)
\ge
A_{\min}(P(t))
$$

## Governance-visible boundary condition

$$
A_t^-
\ge
A_{\min}(P(t))
$$

## Alignment requirements rise with power

$$
\frac{dA_{\min}}{dP}>0
$$

## Extreme-power limit

$$
\lim_{P\to\infty}
A_{\min}(P)=
1
$$

Thus:

$$
P\to\infty
\Rightarrow
A_{\min}(P)\to 1
$$

Extreme power requires alignment approaching perfection.

---

# Assurance Burden

Because normalized alignment is bounded above by $1$, $A_{\min}(P)$ should not be assumed globally convex while also approaching $1$ as an asymptote.

Instead, define the assurance burden:

$$
Q_{\min}(P)
:=
\frac{1}{1-A_{\min}(P)}
$$

for $A_{\min}(P)<1$.

## Assurance burden rises with power

$$
\frac{dQ_{\min}}{dP}>0
$$

## Assurance burden can accelerate at higher power

$$
\frac{d^2Q_{\min}}{dP^2}>0
$$

Interpretation:

$$
P\uparrow
\Rightarrow
A_{\min}(P)\uparrow
\quad
\text{and}
\quad
Q_{\min}(P)\uparrow\uparrow
$$

Power does not merely require more alignment; it requires disproportionately greater confidence, precision, and correction capacity.

---

# Maximum Survivable Power

## Definition of survivable power bound

$$
P_{\max}(a)
:=
\sup
\left\\{
P\ge 0
:
A_{\min}(P)\le a
\right\\}
$$

with the convention that $P_{\max}(a)=0$ if no positive power level is certified at alignment level $a$.

## True survivable power condition

$$
P(t)
\le
P_{\max}(A(t))
$$

## Validated survivable power condition

$$
P(t)
\le
P_{\max}(A_t^-)
$$

---

# Conservative Validated Alignment

## Estimated alignment

$$
\hat{A}_t=
\Phi(E_t,F_t,L_t,G_t)
$$

## Conservative lower-confidence estimate

$$
A_t^-=
\min
\left\\{
1,
\max
\left\\{
0,
\hat{A}_t-
z_q\sigma_{\hat{A},t}
\right\\}
\right\\}
$$

where:

* $q$ is the desired confidence level.
* $z_q$ is the corresponding quantile multiplier.
* $\sigma_{\hat{A},t}$ is uncertainty in the alignment estimate.

## Conservative validation condition

$$
\Pr
\left(
A(t)\ge A_t^-
\right)
\ge
q
$$

Power should be governed by $A_t^-$ rather than by $\hat{A}_t$ alone.

---

# Power Alignment Principle

## Allowable power tracks validated alignment

$$
P_{\text{allowable}}(t)=
g(A_t^-)
$$

with:

$$
g'(A_t^-)>0
$$

and:

$$
g(A_t^-)
\le
P_{\max}(A_t^-)
$$

## Central governance principle

$$
\boxed{
\text{Legitimate deployable power is bounded by conservatively validated alignment.}
}
$$

## Power grant function

$$
P_{\text{granted}}(t)
\le
P_{\max}(A_t^-)
$$

A cautious grant policy may be written:

$$
P_{\text{granted}}(t)=
\chi
g(A_t^-)
$$

where:

$$
0\le \chi \le 1
$$

and:

$$
g(A_t^-)\le P_{\max}(A_t^-)
$$

---

# Alignment Debt

## True alignment debt

$$
D(t)=
\max
\left\\{
0,
A_{\min}(P(t))-A(t)
\right\\}
$$

## Conservative validated alignment debt

$$
\hat{D}_q(t)=
\max
\left\\{
0,
A_{\min}(P(t))-A_t^-
\right\\}
$$

## Debt-free condition

$$
D(t)=0
\iff
A(t)\ge A_{\min}(P(t))
$$

## Validated debt-free condition

$$
\hat{D}_q(t)=0
\iff
A_t^-\ge A_{\min}(P(t))
$$

---

# Risk Scaling

## Simple toy model

A simple toy model relates risk to capability and imperfect alignment:

$$
R
\sim
C^{\alpha}(1-A)
$$

with:

$$
\alpha>1
$$

This is useful as an intuition, but it does not explicitly reference the survivability boundary.

## Boundary-aware risk model

A stronger form makes risk depend on alignment debt:

$$
R(P,A)=
R_0
+
\rho P^{\alpha}
D(P,A)^{\beta}
$$

where:

$$
D(P,A)=
\max
\left\\{
0,
A_{\min}(P)-A
\right\\}
$$

and:

$$
\alpha>1,
\qquad
\beta\ge 1,
\qquad
\rho>0
$$

## Conservative validated risk model

For governance:

$$
\hat{R}_q(P,A_t^-)=
R_0
+
\rho P^{\alpha}
\hat{D}_q(P,A_t^-)^{\beta}
$$

where:

$$
\hat{D}_q(P,A_t^-)=
\max
\left\\{
0,
A_{\min}(P)-A_t^-
\right\\}
$$

---

# Catastrophe Hazard Function

## Increasing hazard with debt

$$
h'(D)>0
$$

with:

$$
h(D)>0
\quad
\text{for}
\quad
D>0
$$

## Cumulative catastrophe probability

$$
\Pr_{\text{cat}}(T)=
1-
\exp
\left(
-\int_0^T h(D(t))\,dt
\right)
$$

## Conservative validated catastrophe probability

$$
\widehat{\Pr}_{\text{cat},q}(T)=
1-
\exp
\left(
-\int_0^T h(\hat{D}_q(t))\,dt
\right)
$$

---

# Great Filter Formalization

## Persistent uncorrected debt drives collapse probability toward unity

$$
\int_0^\infty h(D(t))\,dt=
\infty
\Rightarrow
\Pr_{\text{cat}}(\infty)=1
$$

## Sustained positive debt condition

If:

$$
\exists \delta>0,\exists t_0
\text{ such that }
D(t)\ge \delta
\quad
\forall t\ge t_0
$$

then:

$$
\Pr_{\text{cat}}(T)\to 1
\quad
\text{as}
\quad
T\to\infty
$$

## Great Filter hypothesis

$$
\exists P^\ast
\text{ such that }
A(P^\ast)<A_{\min}(P^\ast)
\quad
\text{and the resulting debt persists}
\Rightarrow
\Pr(\text{collapse})\to 1
$$

## Extreme-power survival condition

Because:

$$
\lim_{P\to\infty}A_{\min}(P)=1
$$

survival under extreme power requires:

$$
P(t)\to\infty
\Rightarrow
A(t)\to 1
$$

and, more specifically:

$$
A(t)\ge A_{\min}(P(t))
$$

Extreme power yields survival collapse unless alignment scales adequately.

---

# Scaling Exponent Formulation

Because normalized alignment is bounded above by $1$, it is cleaner to scale alignment error rather than alignment itself.

## Power scaling law

$$
P(K)
\sim
K^{\theta}
$$

with:

$$
\theta>0
$$

## Alignment error

$$
e_A(K)
:=
1-A(K)
$$

## Alignment error scaling law

$$
e_A(K)
\sim
K^{-\lambda}
$$

with:

$$
\lambda>0
$$

## Required tolerance

$$
\tau_{\min}(K)
:=
1-A_{\min}(P(K))
$$

## Required tolerance scaling law

$$
\tau_{\min}(K)
\sim
K^{-\mu}
$$

with:

$$
\mu>0
$$

## Survivability condition

Since:

$$
A(K)\ge A_{\min}(P(K))
$$

we require:

$$
1-A(K)
\le
1-A_{\min}(P(K))
$$

or:

$$
e_A(K)
\le
\tau_{\min}(K)
$$

## Asymptotic survivability condition

Ignoring constants, survivability requires:

$$
\lambda\ge \mu
$$

## Dangerous mismatch condition

$$
\lambda<\mu
$$

Interpretation:

$$
\text{Alignment error must shrink at least as fast as required tolerance shrinks.}
$$

## Divergence of error-to-tolerance ratio

If $\lambda<\mu$, then:

$$
\frac{e_A(K)}{\tau_{\min}(K)}
\sim
K^{\mu-\lambda}
\to
\infty
$$

This means alignment error increasingly exceeds the survivability tolerance.

---

# Power Alignment Control Law

## Uncertainty-aware control law

$$
P_{t+1}=
\Pi_{[0,P_{\text{cap}}]}
\left[
P_t
+
k
\left(
A_t^--
A_{\min}(P_t)-
m
\right)
\right]
$$

where:

* $k>0$ is the update rate.
* $m\ge 0$ is a safety margin.
* $P_{\text{cap}}$ is an external hard cap.
* $\Pi_{[0,P_{\text{cap}}]}$ projects the result into the allowable interval $[0,P_{\text{cap}}]$.

## Safe expansion condition

$$
A_t^-
\ge
A_{\min}(P_t)+m
$$

## Required throttling condition

$$
A_t^-
<
A_{\min}(P_t)
$$

## Margin violation condition

$$
A_{\min}(P_t)
\le
A_t^-
<
A_{\min}(P_t)+m
$$

In the margin-violation zone, expansion should pause even if immediate debt is not yet positive.

---

# Four-Test Alignment Estimator

## Estimator definition

$$
\hat{A}_t=
\Phi(E_t,F_t,L_t,G_t)
$$

where:

* $E_t$ measures ethical coherence.
* $F_t$ measures factual contact.
* $L_t$ measures logical consistency.
* $G_t$ measures governance, law, accountability, and procedural validity.

## Monotonicity condition

A basic monotonicity requirement is:

$$
\frac{\partial \Phi}{\partial E}\ge 0,
\qquad
\frac{\partial \Phi}{\partial F}\ge 0,
\qquad
\frac{\partial \Phi}{\partial L}\ge 0,
\qquad
\frac{\partial \Phi}{\partial G}\ge 0
$$

## Conservative estimator

$$
A_t^-=
B_q
\left(
\Phi(E_t,F_t,L_t,G_t)
\right)
$$

where $B_q$ denotes the conservative lower-confidence bounding map at confidence level $q$.

---

# Correctability Principle

## Core statement

$$
\text{Persistent Intelligence}
\iff
\text{Scalable Correctability}
$$

## Closed correction loop

A closed correction loop maps the system back into itself without reliable outside contact:

$$
\Gamma_{\text{closed}}
:
\mathcal{S}
\to
\mathcal{S}
$$

## Open correction loop

An open correction loop incorporates world feedback:

$$
\Gamma_{\text{open}}
:
\mathcal{S}\times \mathcal{W}
\to
\mathcal{S}
$$

## Reality-contact condition

$$
\mathcal{W}
\leadsto
\text{reality constraint}
$$

## Survivorship-orientation condition

$$
\mathcal{W}
\leadsto
\mathcal{U}
$$

Correction becomes survivable when feedback remains coupled to reality and survivorship.

---

# Reintegration / Redemptive Bridge

## Reintegration increases cooperation probability

$$
\frac{
\partial
\Pr(\text{cooperation})
}{
\partial B_{\text{reintegration}}
}>0
$$

## Reintegration must preserve survivability constraints

$$
\frac{
\partial D
}{
\partial B_{\text{reintegration}}
}
\le 0
$$

A redemptive bridge is survivable only if it increases cooperation without increasing alignment debt.

---

# Cancer Analogy

## Local optimization is not global survivability

$$
\text{Local Fitness Maximization}
\neq
\text{Global System Survivability}
$$

## Formalized distinction

$$
\arg\max_i f_i
\not\equiv
\arg\max \mathcal{U}
$$

where $f_i$ is the local fitness or payoff of subsystem $i$.

## Cancer condition

$$
\frac{\partial f_i}{\partial t}>0
\quad
\text{while}
\quad
\frac{\partial \mathcal{U}}{\partial t}<0
$$

A subsystem can become locally successful while degrading the survivability of the larger system.

---

# Ethical Optimization

## Policy optimization

$$
\pi^\ast=
\arg\max_{\pi\in\Pi}
\Pr
\left(
\mathcal{F}_{\infty}
\mid
\pi
\right)
$$

where $\mathcal{F}_{\infty}$ denotes persistent flourishing.

## Informal ethical interpretation

$$
\text{Good}
\approx
\text{that which increases persistent flourishing probability}
$$

## Misalignment interpretation

$$
\text{Misaligned}
\approx
\text{that which destabilizes survivability}
$$

## Ethical delta form

$$
\Delta
\Pr
\left(
\mathcal{F}_{\infty}
\right)>0
\Rightarrow
\text{ethically positive}
$$

$$
\Delta
\Pr
\left(
\mathcal{F}_{\infty}
\right)<0
\Rightarrow
\text{ethically negative}
$$

---

# Alignment Economy

## Conservative alignment-weighted allocation

$$
P_{\text{allocated},i}=
\frac{
\psi(A_i^-)
}{
\sum_j \psi(A_j^-)
}
P_{\text{total}}
$$

with:

$$
\psi'(A^-)\ge 0
$$

## Individual survivability cap

$$
P_{\text{allocated},i}
\le
P_{\max}(A_i^-)
$$

## Total allocation constraint

$$
\sum_i P_{\text{allocated},i}
\le
P_{\text{total}}
$$

Power allocation should favor conservatively validated alignment while respecting survivability caps.

---

# Validator Agora Objective

## Estimation accuracy objective

$$
\mathbb{E}
\left[
(\hat{A}-A)^2
\right]
\downarrow
$$

## Conservative calibration objective

$$
\Pr(A\ge A^-)
\ge
q
$$

## Combined validation objective

$$
\mathcal{L}_{\text{validator}}=
\mathbb{E}
\left[
(\hat{A}-A)^2
\right]
+
\lambda_{\text{cal}}
C_{\text{cal}}(A^-,A)
$$

with objective:

$$
\mathcal{L}_{\text{validator}}
\downarrow
$$

where $C_cal(A^-,A)$ denotes the calibration-error penalty between the conservative bound and true alignment.

The Validator Agora should reduce estimation error while preserving conservative calibration.

---

# AI Alignment Scaling Condition

## True AI survivability condition

$$
A_{\text{AI}}(t)
\ge
A_{\min}(P_{\text{AI}}(t))
$$

## Validated AI deployment condition

$$
A_{\text{AI},t}^-
\ge
A_{\min}(P_{\text{AI}}(t))
$$

## Survivable AI power bound

$$
P_{\text{AI}}(t)
\le
P_{\max}(A_{\text{AI},t}^-)
$$

## Unsafe AI deployment condition

$$
P_{\text{AI}}(t)>
P_{\max}(A_{\text{AI},t}^-)
$$

or equivalently:

$$
\hat{D}_{q,\text{AI}}(t)>0
$$

---

# Compact Reference Summary

## Core boundary

$$
\boxed{
A(t)
\ge
A_{\min}(P(t))
}
$$

## Conservative governance boundary

$$
\boxed{
A_t^-
\ge
A_{\min}(P(t))
}
$$

## Alignment debt

$$
\boxed{
D(t)=
\max
\left\\{
0,
A_{\min}(P(t))-A(t)
\right\\}
}
$$

## Conservative validated debt

$$
\boxed{
\hat{D}_q(t)=
\max
\left\\{
0,
A_{\min}(P(t))-A_t^-
\right\\}
}
$$

## Survivable power bound

$$
\boxed{
P(t)
\le
P_{\max}(A_t^-)
}
$$

## Catastrophe probability

$$
\boxed{
\Pr_{\text{cat}}(T)=
1-
\exp
\left(
-\int_0^T h(D(t))\,dt
\right)
}
$$

## Great Filter condition

$$
\boxed{
\int_0^\infty h(D(t))\,dt=
\infty
\Rightarrow
\Pr_{\text{cat}}(\infty)=1
}
$$

## Central thesis

$$
\boxed{
\text{Persistent intelligence requires scalable power to remain coupled to validated alignment.}
}
$$
