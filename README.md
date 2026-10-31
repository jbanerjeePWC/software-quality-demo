# quality-madness-demo

Teaching material for short screen-recorded tutorials about Python environments,
linting (pylint), pre-commit, pytest and GitHub Actions CI.

The repository is a network of branches. Each branch is a ready-made stage for one
tutorial. Some branches contain deliberately bad code, and each of those has a matching
fixed branch, so `git diff <bad> <fixed>` shows only the fix.

Every branch has a `BRANCH.md` at its root with the commands to demonstrate and the
expected output, copied from a real verification run.

Only branches whose names start with `ci-` contain a GitHub Actions workflow, so pushing
any other branch triggers no CI run.

## Branches

The branch table is added once every branch is built and verified.
