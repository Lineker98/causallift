import numpy as np

from causallift.simulations.randomness import create_rng


def test_same_seed_produces_identical_sample() -> None:
    first = create_rng(42).standard_normal(128)
    second = create_rng(42).standard_normal(128)

    np.testing.assert_array_equal(first, second)


def test_generators_have_independent_local_state() -> None:
    advanced = create_rng(42)
    untouched = create_rng(42)
    reference = create_rng(42)

    advanced.standard_normal(256)

    actual = untouched.standard_normal(64)
    expected = reference.standard_normal(64)

    np.testing.assert_array_equal(actual, expected)


def test_different_seeds_produce_different_sample() -> None:
    first = create_rng(42).standard_normal(128)
    second = create_rng(43).standard_normal(128)

    assert not np.array_equal(first, second)
