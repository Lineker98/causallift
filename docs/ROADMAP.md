# CausalLift Roadmap

This roadmap describes the intended capability progression of CausalLift.

It is directional rather than a commitment to specific libraries,
infrastructure, or implementation details. Methods and architecture should be
introduced only when the scientific or product requirement justifies them.

## Status meanings

- **DONE** — implemented and validated at the current required scope.
- **CURRENT / NEXT** — immediate project work.
- **FUTURE** — intended capability, not currently implemented.
- **DEFERRED** — intentionally postponed until a concrete requirement exists.

## DONE — Phase 0 foundations

Phase 0 has established the minimum engineering and causal foundation needed
for further work.

Engineering foundations include:

- Python 3.12 project;
- `uv` dependency and environment management;
- locked dependencies;
- installable `src/causallift` package using `uv_build`;
- pytest;
- Ruff;
- mypy;
- pre-commit;
- GitHub Actions;
- explicit parameter-flow conventions;
- explicit seed ownership and local NumPy `Generator` instances.

The first causal ground-truth capability includes:

- a randomized binary treatment;
- explicit potential outcomes;
- a constant additive treatment effect;
- known population ATE;
- a first-principles difference-in-means estimator;
- deterministic simulation;
- statistical recovery tests;
- tests for consistency and potential-outcome ground truth.

This is a randomized causal smoke test, not a general causal inference system.

## CURRENT / NEXT

The immediate sequence is:

1. consolidate Phase 0 documentation;
2. perform the Phase 0 technical review;
3. perform the formal Phase 0 gate review.

After the gate, the learning and implementation path should deepen causal
foundations and randomized experimentation before introducing observational
complexity.

Near-term work should progressively cover:

- potential-outcomes reasoning;
- causal DAG reasoning;
- randomized experiment design and analysis;
- estimands and uncertainty;
- regression adjustment where justified;
- synthetic DGPs with richer known ground truth;
- causal tests that verify recovery under controlled conditions.

## FUTURE — Observational identification

Observational causal inference should be introduced only after the randomized
foundation is well understood.

Expected topics include:

- explicit confounding structures;
- observational identification assumptions;
- covariate adjustment;
- propensity-score estimation;
- matching where useful;
- inverse-probability weighting;
- overlap and balance diagnostics;
- failure under poor overlap and misspecification.

The presence of these items on the roadmap does not imply current support.

## FUTURE — Doubly robust estimation

Progress toward methods combining treatment and outcome nuisance models,
including:

- AIPW;
- Double ML;
- doubly robust learners.

These methods should be evaluated against synthetic ground truth and not
treated as causal merely because a library implements them.

## FUTURE — Heterogeneous treatment effects

Introduce treatment-effect heterogeneity and CATE estimation progressively.

Expected areas include:

- effect modifiers;
- S-, T-, and X-learners;
- DR learners;
- causal forests where justified;
- PEHE and treatment-effect recovery on synthetic data;
- uncertainty and calibration considerations.

Production CATE estimation is not currently implemented.

## FUTURE — Uplift evaluation

Move from average effects toward evaluation of treatment ranking and targeting.

Expected capabilities include:

- uplift curves;
- Qini-style evaluation;
- AUUC;
- incremental conversions;
- policy-value evaluation.

Predictive ranking metrics alone should not determine causal model quality.

## FUTURE — Sensitivity and robustness

Add diagnostics for the assumptions on which causal conclusions depend.

Expected areas include:

- model misspecification;
- overlap failures;
- unmeasured-confounding sensitivity;
- robustness across estimator choices;
- uncertainty and interval coverage.

## FUTURE — Policy learning

Translate heterogeneous effects into treatment decisions.

Expected concerns include:

- treatment eligibility;
- policy value;
- capacity constraints;
- treatment costs;
- operational constraints;
- comparison with simple benchmark policies.

Effect estimation and treatment policy should remain conceptually separate.

## FUTURE — Economic optimization

Connect causal treatment decisions to business value.

Expected objectives include:

- incremental revenue;
- incremental profit;
- treatment cost;
- wasted treatment;
- campaign ROI;
- constrained resource allocation.

This stage addresses whether a causally better decision is also economically
better.

## FUTURE / DEFERRED — Production application architecture

Production application components will be introduced only when the product
workflow requires them.

Potential future concerns include:

- API delivery;
- persistent storage;
- object storage;
- background analysis execution;
- authentication and authorization;
- experiment and model lineage;
- deployment;
- observability.

No particular framework or infrastructure choice is committed by this roadmap.

## FUTURE — Causal monitoring

Production monitoring should distinguish:

- covariate drift: `P(X)`;
- treatment-policy drift: `P(T|X)`;
- outcome drift: `P(Y|T,X)`;
- treatment-effect drift: `τ(X)`.

Additional monitoring may include:

- treatment allocation;
- propensity distributions;
- overlap;
- data quality;
- ATE and CATE distributions;
- policy value.

These are future capabilities.

## FUTURE — Continuous experimentation and product validation

The mature system should support a feedback loop between causal analysis,
decision policy, economic outcomes, and new experimentation.

Long-term product validation should determine whether CausalLift:

- improves real intervention decisions;
- generates measurable incremental value;
- makes assumptions and uncertainty understandable;
- supports repeatable operational workflows;
- remains scientifically defensible as product complexity grows.
