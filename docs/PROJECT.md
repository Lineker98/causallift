# CausalLift Project

## North Star

CausalLift aims to support decisions where the value of an action depends on
its incremental causal effect.

The long-term reasoning chain is:

```text
business decision
→ causal question
→ causal model
→ identification
→ data requirements
→ estimation
→ diagnostics
→ robustness
→ heterogeneous effects
→ policy
→ economic optimization
→ deployment
→ monitoring
→ experimentation
→ product decision
```

The objective is not merely to estimate causal effects. It is to connect
credible causal evidence to better operational decisions.

## Product thesis

The core product question is:

> Which customers should receive an intervention to maximize incremental
> business value?

This requires separating three distinct problems:

- **Prediction:** who will convert?
- **Causality:** who will convert because of treatment?
- **Decision:** who should receive treatment given expected incremental benefit,
  cost, and operational constraints?

A predictive model can rank customers by conversion probability without
identifying who is actually influenced by treatment.

Causal estimation is therefore necessary but still insufficient: useful
treatment decisions must ultimately incorporate economics and operational
constraints.

## Initial commercial wedge

The initial commercial focus is marketing incrementality and treatment
optimization.

Candidate decisions include:

- campaign targeting;
- promotion targeting;
- discount allocation;
- other customer-level interventions where treatment has both expected benefit
  and cost.

Customer-facing value should eventually be expressed in operational and
economic terms such as:

- incremental conversions;
- incremental revenue;
- incremental profit;
- wasted treatment;
- campaign ROI;
- value of an optimized treatment policy.

These are product objectives, not current Phase 0 capabilities.

## Scientific principles

CausalLift treats causal inference as an identification problem before an
estimation problem.

A sophisticated estimator does not by itself establish causality.

Causal work should explicitly define, when applicable:

- unit of analysis;
- treatment;
- outcome;
- target population;
- time horizon;
- estimand;
- confounders;
- mediators;
- colliders;
- effect modifiers;
- identification assumptions;
- positivity or overlap assumptions.

The project distinguishes:

- association;
- prediction;
- causal identification;
- statistical estimation;
- experimental evidence;
- observational evidence;
- downstream decision value.

Important assumptions, estimands, and causal structures should become
versioned artifacts as the system matures.

## Engineering philosophy

CausalLift is developed as a production-oriented software project rather than
as a collection of notebooks.

Engineering principles include:

- one installable Python package unless a concrete requirement justifies
  otherwise;
- explicit interfaces and dependency flow;
- reproducible environments;
- tested reusable logic;
- domain logic independent of infrastructure where practical;
- explicit reproducibility-critical parameters;
- no hidden mutable configuration or random state;
- infrastructure added only when it solves a current problem;
- notebooks used for exploration rather than as the primary home of reusable
  logic.

The project deliberately avoids architecture introduced for résumé value or
anticipated scale.

## Technology, decision, economics, and product

CausalLift separates four questions.

### Technology

Can the causal effect be identified and estimated reliably enough for the
intended use?

### Decision

Can the estimate improve a concrete treatment or allocation decision?

### Economics

Does the resulting decision create incremental economic value after treatment
costs and constraints?

### Product

Can users operate the workflow reliably, understand its assumptions, and act
on its outputs?

Success in one layer does not imply success in the others.

## Current maturity

CausalLift is currently in Phase 0.

The repository has established:

- reproducible Python and dependency management;
- package and quality-tooling foundations;
- CI and pre-commit gates;
- explicit configuration and randomness conventions;
- a minimal randomized-treatment synthetic DGP;
- known potential-outcome ground truth;
- a first-principles difference-in-means estimator;
- automated recovery and causal-consistency tests.

The current implementation is a scientific and engineering foundation only.

It does not yet solve observational marketing incrementality, heterogeneous
treatment-effect estimation, treatment-policy optimization, or production
deployment.

Phase 0 still requires technical review and the formal phase-gate review before
being considered complete.