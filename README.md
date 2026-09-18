# CausalLift

CausalLift is a causal decisioning project focused initially on marketing
incrementality and treatment optimization.

Its core business question is:

> Which customers should receive an intervention to maximize incremental
> business value?

The project distinguishes three different problems:

- **Prediction:** who will convert?
- **Causality:** who will convert because of treatment?
- **Decision:** who should receive treatment given expected incremental benefit,
  cost, and operational constraints?

## Current status

CausalLift is currently in **Phase 0 — Engineering Foundation**.

Phase 0 has established the repository, development quality gates,
reproducibility conventions, and the project's first causal ground-truth test.

The implemented causal capability is intentionally small:

- a randomized binary-treatment synthetic data-generating process;
- explicit potential outcomes;
- a known constant treatment effect;
- deterministic simulation from explicit random seeds;
- an unadjusted difference-in-means estimator implemented from first principles;
- statistical recovery tests against analytically known ground truth.

This establishes a minimal randomized causal correctness foundation.

It does **not** yet establish support for observational identification,
propensity methods, doubly robust estimation, heterogeneous treatment effects,
uplift optimization, sensitivity analysis, production deployment, or causal
monitoring.

Phase 0 is not complete until the remaining technical and phase-gate reviews
are finished.

## Repository setup

Requirements:

- Python `>=3.12,<3.13`
- `uv`

Clone and initialize the repository:

```bash
git clone git@github.com:Lineker98/causallift.git
cd causallift
uv sync --locked
uv run pre-commit install
```

`uv` is the sole Python dependency and environment manager for the project.

The package is built with `uv_build` and uses a `src` layout.

## Development commands

Run the complete local quality suite:

```bash
uv lock --check
uv run ruff check .
uv run ruff format --check .
uv run mypy src
uv run pytest
uv run pre-commit run --all-files
git diff --check
```

Pre-commit intentionally contains only fast deterministic checks:

- Ruff lint;
- Ruff format check.

The full type-checking and test gates remain separate commands and are also
enforced by GitHub Actions.

## Current source structure

The production package is:

```text
src/causallift/
```

Current causal simulation code lives under:

```text
src/causallift/simulations/
```

The repository intentionally does not yet contain production APIs, databases,
orchestration, experiment tracking, deployment infrastructure, or other
components that have not been justified by current requirements.

## Documentation

- [`docs/PROJECT.md`](docs/PROJECT.md) — project purpose, thesis, and principles.
- [`docs/ROADMAP.md`](docs/ROADMAP.md) — capability progression and current status.
- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) — current architectural conventions.
- [`docs/DECISIONS.md`](docs/DECISIONS.md) — significant engineering decisions.
- [`docs/CAUSAL_ASSUMPTIONS.md`](docs/CAUSAL_ASSUMPTIONS.md) — explicit causal assumptions.
- [`docs/EXPERIMENTS.md`](docs/EXPERIMENTS.md) — documented causal experiments and validation.

Future documentation is added only when substantive project content justifies
it.