"""Randomness utilities for causal simulations."""

from numpy.random import Generator, default_rng


def create_rng(seed: int) -> Generator:
    """Create an isolated NumPy random generator from an explicit seed."""
    return default_rng(seed)
