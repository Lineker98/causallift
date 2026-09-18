# Experiments

## P0-T09 — Randomized-Treatment Causal Smoke Test

### Purpose

Validate the repository's first causal data-generating process against an
analytically known causal effect.

This experiment tests causal construction and basic estimation correctness. It
is not intended as a general simulation framework or estimator benchmark.

### Data-generating process

Treatment:

$$
T_i \sim \operatorname{Bernoulli}(p)
$$

Outcome noise:

$$
\epsilon_i \sim \mathcal{N}(0, \sigma^2)
$$

Potential outcomes:

$$
Y_i(0) = \mu + \epsilon_i
$$

$$
Y_i(1) = Y_i(0) + \tau
$$

Observed outcome:

$$
Y_i = Y_i(0) + T_i \tau
$$

### Estimand and ground truth

The estimand is:

$$
\mathrm{ATE} = \mathbb{E}\left[Y(1) - Y(0)\right]
$$

The DGP implies:

$$
\mathrm{ATE} = \tau
$$

exactly.

The individual treatment effect is also $\tau$ for every synthetic unit.

### Estimator

The smoke-test estimator is the unadjusted difference in observed means:

$$
\hat{\tau} = \bar{Y}_{T=1} - \bar{Y}_{T=0}
$$

Randomization makes this estimator unbiased for the ATE under the DGP.

### Sampling error

For realized treatment-arm sizes $n_1$ and $n_0$:

$$
\hat{\tau} = \tau + \bar{\epsilon}_1 - \bar{\epsilon}_0
$$

and therefore:

$$
\operatorname{Var}\left(\hat{\tau} \mid n_1, n_0\right)
= \sigma^2 \left( \frac{1}{n_1} + \frac{1}{n_0} \right)
$$

The corresponding conditional standard error is:

$$
\mathrm{SE} = \sigma \sqrt{\frac{1}{n_1} + \frac{1}{n_0}}
$$

Automated recovery tests use a tolerance of four conditional standard errors
rather than an arbitrary absolute error threshold.

### Validation design

Automated tests verify:

- identical seeds reproduce identical generated arrays;
- treatment is binary;
- both treatment groups are present in the deterministic test setup;
- potential outcomes encode the analytically known treatment effect;
- observed outcomes satisfy consistency;
- difference-in-means recovers a positive ATE across multiple fixed seeds;
- a zero treatment effect remains statistically compatible with zero;
- a negative treatment effect is recovered;
- samples lacking one treatment arm are rejected by the estimator.

### Interpretation

The finite-sample estimate is not expected to equal the population ATE
exactly.

Differences between $\hat{\tau}$ and $\tau$ in this experiment are sampling
error, not evidence of estimator bias.

Repeated sampling would cause estimates to vary around the true ATE.

### Limitations

This experiment intentionally excludes:

- confounding;
- heterogeneous treatment effects;
- covariates;
- mediators;
- colliders;
- latent variables;
- poor population overlap;
- missingness;
- measurement error;
- estimator adjustment;
- uncertainty estimation from observed data.

Those belong to later simulation and estimator tasks.
