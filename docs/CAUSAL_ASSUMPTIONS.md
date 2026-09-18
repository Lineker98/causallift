# Causal Assumptions

## P0-T09 — Synthetic Randomized-Treatment DGP

### Causal question

What is the average causal effect of a binary intervention on a continuous
post-treatment outcome in a randomized synthetic population?

### Unit of analysis

One independently generated synthetic experimental unit. In the initial
CausalLift product framing, a unit may be interpreted as one customer eligible
for an intervention.

### Treatment

$T \in \{0, 1\}$ is a single binary intervention.

Treatment assignment follows:

$$
T_i \sim \operatorname{Bernoulli}(p), \qquad 0 < p < 1
$$

### Outcome

$Y$ is a continuous post-treatment outcome observed once after assignment.

### Target population and time horizon

The target population is the superpopulation implied by the structural
equations below.

The time horizon contains one treatment assignment followed by one outcome
measurement. There are no repeated treatments or longitudinal effects.

### Structural equations

$$
\epsilon_i \sim \mathcal{N}(0, \sigma^2)
$$

$$
Y_i(0) = \mu + \epsilon_i
$$

$$
Y_i(1) = Y_i(0) + \tau
$$

$$
Y_i = Y_i(0) + T_i \tau
$$

Treatment assignment is generated independently of the outcome noise.

### Estimand

The target estimand is the population average treatment effect:

$$
\mathrm{ATE} = \mathbb{E}\left[Y(1) - Y(0)\right]
$$

Since:

$$
Y_i(1) - Y_i(0) = \tau
$$

for every unit,

$$
\mathrm{ATE} = \tau
$$

analytically.

### Individual treatment effects

This synthetic model genuinely defines both potential outcomes for every unit.

Therefore the individual treatment effect is known:

$$
\mathrm{ITE}_i = Y_i(1) - Y_i(0) = \tau
$$

The effect is constant rather than heterogeneous.

### Consistency

The observed outcome satisfies:

$$
Y_i = Y_i(T_i)
$$

The intervention is treated as well-defined and there is no interference
between units.

### Exchangeability

Randomized assignment implies:

$$
T \perp\!\!\!\perp \bigl(Y(0), Y(1)\bigr)
$$

by construction.

Treatment does not depend on the outcome noise or any variable affecting
potential outcomes. Therefore treated and control units are exchangeable in
expectation, and the difference in observed group means identifies the ATE.

### Positivity

Population positivity holds because:

$$
0 < \mathbb{P}(T = 1) = p < 1
$$

for every unit.

Finite samples can nevertheless contain only one treatment arm, especially
when the sample is small or $p$ is extreme. The estimator explicitly rejects
such samples.

### Confounders

None are present in this DGP.

### Mediators

None are present.

### Colliders

None are present.

### Effect modifiers

None are present because the treatment effect is constant.

### Scope

These assumptions apply only to the P0-T09 randomized-treatment simulation.

They must not be generalized to later observational or heterogeneous-treatment
scenarios.
