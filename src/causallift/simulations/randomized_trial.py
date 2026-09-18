"""Simple randomized-treatment simulation with known causal ground truth."""

import numpy as np
from numpy.typing import NDArray

from causallift.simulations.randomness import create_rng

IntArray = NDArray[np.int64]
FloatArray = NDArray[np.float64]


def simulate_randomized_trial(
    *,
    n: int,
    treatment_probability: float,
    baseline_mean: float,
    treatment_effect: float,
    outcome_noise_sd: float,
    seed: int,
) -> tuple[IntArray, FloatArray, FloatArray, FloatArray]:
    """Simulate a randomized trial with a constant additive treatment effect.

    Structural equations:

        T ~ Bernoulli(treatment_probability)
        Y(0) = baseline_mean + epsilon
        Y(1) = Y(0) + treatment_effect
        Y = Y(0) + T * treatment_effect

    where epsilon ~ Normal(0, outcome_noise_sd**2) independently of treatment.

    Returns:
        treatment, observed_outcome, potential_outcome_0, potential_outcome_1
    """
    if n <= 0:
        raise ValueError("n must be positive")

    if not 0.0 < treatment_probability < 1.0:
        raise ValueError("treatment_probability must be strictly between 0 and 1")

    if outcome_noise_sd < 0.0:
        raise ValueError("outcome_noise_sd must be non-negative")

    rng = create_rng(seed)

    treatment = rng.binomial(
        n=1,
        p=treatment_probability,
        size=n,
    ).astype(np.int64)

    noise = rng.normal(
        loc=0.0,
        scale=outcome_noise_sd,
        size=n,
    )

    potential_outcome_0 = baseline_mean + noise
    potential_outcome_1 = potential_outcome_0 + treatment_effect
    observed_outcome = potential_outcome_0 + treatment * treatment_effect

    return (
        treatment,
        observed_outcome,
        potential_outcome_0,
        potential_outcome_1,
    )


def difference_in_means(
    treatment: IntArray,
    outcome: FloatArray,
) -> float:
    """Estimate the ATE as treated mean outcome minus control mean outcome."""
    if treatment.ndim != 1 or outcome.ndim != 1:
        raise ValueError("treatment and outcome must be one-dimensional")

    if treatment.shape != outcome.shape:
        raise ValueError("treatment and outcome must have the same shape")

    if not np.all((treatment == 0) | (treatment == 1)):
        raise ValueError("treatment must contain only 0 and 1")

    treated = outcome[treatment == 1]
    control = outcome[treatment == 0]

    if treated.size == 0 or control.size == 0:
        raise ValueError("both treatment arms must be present")

    return float(np.mean(treated) - np.mean(control))
