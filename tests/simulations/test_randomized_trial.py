import numpy as np
import pytest

from causallift.simulations.randomized_trial import (
    difference_in_means,
    simulate_randomized_trial,
)

N = 20_000
TREATMENT_PROBABILITY = 0.5
BASELINE_MEAN = 10.0
NOISE_SD = 1.0


def _assert_estimate_within_sampling_error(
    *,
    treatment_effect: float,
    seed: int,
) -> None:
    treatment, outcome, _, _ = simulate_randomized_trial(
        n=N,
        treatment_probability=TREATMENT_PROBABILITY,
        baseline_mean=BASELINE_MEAN,
        treatment_effect=treatment_effect,
        outcome_noise_sd=NOISE_SD,
        seed=seed,
    )

    estimated_ate = difference_in_means(treatment, outcome)

    n_treated = int(np.sum(treatment == 1))
    n_control = int(np.sum(treatment == 0))

    standard_error = NOISE_SD * np.sqrt(1.0 / n_treated + 1.0 / n_control)

    tolerance = 4.0 * standard_error

    assert abs(estimated_ate - treatment_effect) <= tolerance


def test_same_seed_reproduces_same_dataset() -> None:
    first = simulate_randomized_trial(
        n=1_000,
        treatment_probability=0.5,
        baseline_mean=10.0,
        treatment_effect=2.0,
        outcome_noise_sd=1.0,
        seed=42,
    )

    second = simulate_randomized_trial(
        n=1_000,
        treatment_probability=0.5,
        baseline_mean=10.0,
        treatment_effect=2.0,
        outcome_noise_sd=1.0,
        seed=42,
    )

    for first_array, second_array in zip(first, second, strict=True):
        np.testing.assert_array_equal(first_array, second_array)


def test_treatment_is_binary_and_both_arms_are_present() -> None:
    treatment, _, _, _ = simulate_randomized_trial(
        n=1_000,
        treatment_probability=0.5,
        baseline_mean=10.0,
        treatment_effect=2.0,
        outcome_noise_sd=1.0,
        seed=42,
    )

    assert set(np.unique(treatment)) == {0, 1}


def test_potential_outcomes_encode_known_constant_treatment_effect() -> None:
    treatment_effect = 2.0

    _, outcome, potential_outcome_0, potential_outcome_1 = simulate_randomized_trial(
        n=1_000,
        treatment_probability=0.5,
        baseline_mean=10.0,
        treatment_effect=treatment_effect,
        outcome_noise_sd=1.0,
        seed=42,
    )

    individual_effects = potential_outcome_1 - potential_outcome_0

    np.testing.assert_allclose(individual_effects, treatment_effect)

    true_ate = float(np.mean(individual_effects))

    assert true_ate == pytest.approx(treatment_effect)

    assert outcome.shape == potential_outcome_0.shape


def test_observed_outcome_satisfies_consistency() -> None:
    treatment, outcome, potential_outcome_0, potential_outcome_1 = (
        simulate_randomized_trial(
            n=1_000,
            treatment_probability=0.5,
            baseline_mean=10.0,
            treatment_effect=2.0,
            outcome_noise_sd=1.0,
            seed=42,
        )
    )

    expected_outcome = np.where(
        treatment == 1,
        potential_outcome_1,
        potential_outcome_0,
    )

    np.testing.assert_array_equal(outcome, expected_outcome)


@pytest.mark.parametrize("seed", [11, 22, 33, 44, 55])
def test_difference_in_means_recovers_positive_ate(seed: int) -> None:
    _assert_estimate_within_sampling_error(
        treatment_effect=2.0,
        seed=seed,
    )


def test_difference_in_means_behaves_correctly_for_zero_effect() -> None:
    _assert_estimate_within_sampling_error(
        treatment_effect=0.0,
        seed=2026,
    )


def test_difference_in_means_recovers_negative_effect() -> None:
    _assert_estimate_within_sampling_error(
        treatment_effect=-1.5,
        seed=2027,
    )


def test_difference_in_means_rejects_missing_treatment_arm() -> None:
    treatment = np.ones(10, dtype=np.int64)
    outcome = np.arange(10, dtype=np.float64)

    with pytest.raises(ValueError, match="both treatment arms"):
        difference_in_means(treatment, outcome)
