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

At P0-T07, the CausalLift package contained only package metadata.

There were no simulations, causal estimators, API services, persistence
components, or infrastructure settings requiring configuration aggregation.

P0-T08 was expected to introduce randomness behavior, and P0-T09 the first
synthetic randomized-treatment causal smoke test.

### Alternatives

- generic `config.py`;
- immediate `SimulationConfig`;
- untyped configuration dictionaries;
- Pydantic Settings;
- YAML or hierarchical configuration;
- environment-driven experiment parameters.

### Rationale

Explicit parameters were the smallest mechanism that kept dependencies visible,
typed, testable, and reproducible.

Introducing a configuration object at that point would have modeled
speculative requirements rather than solved an existing problem.

### Consequences

Stochastic components expose reproducibility parameters explicitly.

Simulation code introduces only the parameters required by its actual
data-generating process.

No configuration framework or dependency is required.

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

## P0-T08: Local NumPy Generator ownership

**Status:** Accepted

### Decision

Use NumPy `Generator` instances created locally with `default_rng(seed)`.

Top-level simulation boundaries accept explicit integer seeds. Lower-level
stochastic helpers receive the owned `Generator` when participating in the same
simulation run.

### Context

Causal simulations require deterministic reproducibility without hidden global
configuration or RNG state.

### Alternatives

- legacy `np.random.seed`;
- a module-global `Generator`;
- explicit `Generator(PCG64(seed))`;
- allowing every stochastic function to accept either a seed or an RNG.

### Rationale

Local ownership makes random state explicit, prevents interference between
tests and simulations, uses NumPy's current generator API, and avoids premature
random-stream abstractions.

### Consequences

NumPy is a runtime dependency.

Reproduction assumes the same explicit inputs, code, and locked dependency
environment rather than guaranteeing identical byte streams across arbitrary
future NumPy versions.

### Revisit when

Revisit this decision if the project requires:

- parallel simulation;
- deterministic child random streams;
- distributed execution;
- cross-version random-stream compatibility.