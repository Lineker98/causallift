# CausalLift Architecture

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

### Randomness and reproducibility

Stochastic operations must not depend on hidden global random state.

The current convention is:

- the caller supplies an explicit integer seed;
- the component owning the stochastic operation owns its local random state;
- lower-level helpers receive random state explicitly when necessary;
- imports must not mutate process-wide random state.

The concrete random-number implementation belongs to P0-T08.

### Infrastructure and runtime settings

Infrastructure settings are separate from causal and experiment parameters.

Examples include future:

- database connection settings;
- object-storage settings;
- credentials;
- deployment-specific API settings.

Infrastructure settings should be resolved at application or infrastructure
boundaries and passed inward through explicit interfaces.

Domain and simulation code should not directly depend on environment variables,
`.env` files, FastAPI settings objects, PostgreSQL configuration, or
cloud-provider configuration.

CausalLift currently has no runtime-settings subsystem because no concrete
runtime-settings requirement exists yet.