# CausalLift

CausalLift is a causal decisioning project focused initially on marketing incrementality and treatment optimization.

Its core decision question is:

> Which customers should receive an intervention to maximize incremental business value?

The project explicitly distinguishes three different problems:

- **Prediction:** who is likely to convert?
- **Causality:** who will convert because of the treatment?
- **Decision:** who should be treated given expected incremental benefit, cost, and operational constraints?

## Project status

The project is currently in:

**Phase 0 — Engineering Foundation and Repository Setup**

The repository is intentionally minimal at this stage.

Runtime configuration, dependency management, source-code structure, testing, CI/CD, containers, and other engineering components will be introduced through their dedicated project tasks rather than being added prematurely.

## Repository conventions

### Branching

`main` is the only long-lived branch.

Development should normally occur on short-lived branches created from `main`.

Recommended naming:

- `feat/<short-description>` — new functionality
- `fix/<short-description>` — bug fixes
- `chore/<short-description>` — maintenance or engineering work
- `docs/<short-description>` — documentation changes

Branches should remain small and focused and be merged back into `main` after the relevant work has been reviewed and validated.

A permanent `develop` branch is intentionally not used unless future project complexity provides a concrete reason for introducing one.

### Commits

Commits should represent small, coherent changes.

Commit messages should describe the intent of the change clearly.

Typical prefixes are:

- `feat:`
- `fix:`
- `chore:`
- `docs:`
- `test:`
- `refactor:`

These prefixes are a repository convention, not currently enforced by tooling.

### Local pre-commit hooks

Install the Git pre-commit hook once after cloning the repository:

```bash
uv run pre-commit install 
```

Run all configured hoos manually with 

```bash
uv run pre-commit run --all-files
```

The pre-commit workflow intentionally runs only fast deterministic checks. The full test and type-checking gates remain separate commands.


## Version-control policy

Files that define or explain the project should normally be versioned, including:

- source code;
- tests;
- documentation;
- project configuration;
- reproducible scripts;
- small deterministic or synthetic test fixtures;
- dependency lockfiles when dependency management is introduced.

Files that are machine-specific, sensitive, temporary, or reproducibly generated should normally not be versioned, including:

- virtual environments;
- Python and tool caches;
- local environment-variable files;
- secrets and credentials;
- IDE-specific local state;
- logs;
- raw or private datasets;
- generated artifacts.

The `.gitignore` file contains the current repository-level exclusions.

## Getting started

The project uses Python 3.12 and `uv` for Python runtime and dependency management.

Clone the repository and enter its root directory:

```bash
git clone git@github.com:Lineker98/causallift.git
cd causallift
uv sync --locked
uv run pre-commit install