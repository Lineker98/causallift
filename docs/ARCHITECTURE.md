# CausalLift Architecture

## Current implementation

CausalLift currently uses one installable Python package:

```text
src/causallift/
```

Current reusable causal simulation code lives under:

```text
src/causallift/simulations/
```

The current implementation contains:

- explicit randomness utilities;
- a randomized-treatment synthetic DGP;
- a first-principles difference-in-means estimator.

The repository does not yet contain production APIs, persistence, background
workers, orchestration, model tracking, deployment infrastructure, or other
application components that have not been justified by current requirements.

## Configuration strategy

CausalLift separates:

1. domain and experiment parameters;
2. infrastructure and runtime settings.

These concerns must not be mixed.

### Domain and experiment parameters

Reproducibility-critical parameters should be explicit inputs to the code that
uses them.

Current conventions:

- prefer typed function arguments over configuration objects;
- prefer keyword-only arguments when they improve call-site clarity;
- expose reproducibility-critical parameters at the public boundary of an
  operation;
- avoid hidden module-level mutable configuration;
- avoid generic configuration dictionaries when a typed interface is practical;
- introduce a configuration value object only when a real cohesive parameter
  group exists.

If a configuration value object becomes justified, it should normally be:

- domain-specific;
- typed;
- immutable when practical;
- located with the domain that owns it;
- independent of web and infrastructure frameworks.

A frozen standard-library dataclass is the preferred default when such an
object is actually needed.

## Randomness and reproducibility

Top-level simulation boundaries receive explicit integer seeds and create
isolated NumPy `Generator` instances locally.

Internal stochastic functions should receive an existing `Generator` when they
belong to the same simulation run rather than creating or reseeding their own
random state.

Global RNG state such as `np.random.seed(...)` and module-level mutable random
generators is prohibited.

Deterministic reproduction assumes the same explicit inputs, code, and locked
dependency environment.

The project does not promise identical random streams across arbitrary future
NumPy versions.

## Infrastructure and runtime settings

Infrastructure settings are separate from causal and experiment parameters.

Examples of future infrastructure settings may include:

- database connection information;
- object-storage configuration;
- credentials;
- deployment-specific application settings.

If introduced, infrastructure settings should be resolved at application or
infrastructure boundaries and passed inward through explicit interfaces.

Domain and simulation code should not directly depend on environment variables,
`.env` files, web-framework settings objects, database configuration, or cloud
provider configuration.

CausalLift currently has no runtime-settings subsystem because no concrete
runtime-settings requirement exists.

## Deliberately deferred architecture

The current repository does not require a production application architecture.

Components such as APIs, databases, object storage, background jobs,
authentication, deployment infrastructure, or experiment tracking should be
introduced only when a concrete product workflow requires them.

The current architectural preference remains to evolve a modular monolith
before considering distributed or microservice architecture.