# CausalLift Architectural Decisions

## 2026-09-17 — P0-T07: Explicit parameter flow before configuration objects

**Status:** Accepted

### Decision

Use explicit typed function parameters as the default mechanism for passing
domain, experiment, simulation, and reproducibility-critical configuration.

Do not introduce a generic configuration module, global configuration object,
or simulation configuration class at this stage.

Random seeds must enter stochastic operations explicitly rather than through
hidden package-level mutable state.

Keep domain and experiment configuration separate from infrastructure and
runtime settings.

### Context

At P0-T07, the CausalLift package contains only package metadata.

There are no simulations, causal estimators, API services, persistence
components, or infrastructure settings requiring configuration aggregation.

P0-T08 will introduce randomness behavior, and P0-T09 will introduce the first
synthetic randomized-treatment causal smoke test.

### Alternatives

- Generic `config.py`.
- Immediate `SimulationConfig`.
- Untyped configuration dictionaries.
- Pydantic Settings.
- YAML or hierarchical configuration.
- Environment-driven experiment parameters.

### Rationale

Explicit parameters are currently the smallest mechanism that keeps
dependencies visible, typed, testable, and reproducible.

Introducing a configuration object now would model speculative requirements
rather than solve an existing problem.

### Consequences

P0-T08 and subsequent stochastic components should expose reproducibility
parameters explicitly.

P0-T09 should introduce only the simulation parameters required by its actual
data-generating process.

No configuration framework or dependency is added.

### Risks

Function signatures may eventually become too large.

Repeated parameter plumbing may become noisy as simulations grow.

### Revisit when

Revisit this decision when:

- a cohesive parameter group is repeatedly passed together;
- the group has meaningful validation invariants;
- configuration must be persisted or versioned as a first-class artifact;
- infrastructure runtime settings actually exist;
- explicit parameter flow becomes materially harder to maintain.