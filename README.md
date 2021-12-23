# cfn-guard-test

[![License](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE.md)
[![Maintenance](https://img.shields.io/badge/Maintained-yes-green.svg)](https://github.com/Nr18/cfn-guard-test/graphs/commit-activity)
[![GitHub release](https://img.shields.io/github/release/Nr18/cfn-guard-test.svg)](https://github.com/Nr18/cfn-guard-test/releases/)
[![Continuous Integration](https://github.com/Nr18/cfn-guard-test/actions/workflows/ci.yml/badge.svg)](https://github.com/Nr18/cfn-guard-test/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/Nr18/cfn-guard-test/branch/main/graph/badge.svg?token=RMPJ8DBMKZ)](https://codecov.io/gh/Nr18/cfn-guard-test)

This tool allows you to easily run your [cfn-guard][cfn-guard] tests against your cfn-guard rules.

`cfn-guard-test` is a tool that converts various reports into the JUnit format.

## Installation

You can install the `cfn-guard-test` tool by running the following command:

```bash
pip install cfn_guard_test
```

### Installation in venv

Typically, you would want to run your dependencies isolated. You can install [cfn-guard-test][cfn-guard-test] in a `venv`
using the following commands:

```bash
python -m venv .venv
source .venv/bin/activate
pip install cfn_guard_test
```

## Usage

To use `cfn-guard-test` you just execute the following command:

```bash
cfn-guard-test
```

This will (by default) look for a test file in `tests/reports` and it there is a yaml file that matches the same name in
the `reports` folder. It will then validate the rules defined in the `reports` folder against the test definition.

You can get a more verbose output if you add one of the following commands:

```bash
cfn-guard-test -v
cfn-guard-test --verbose
```

If you use a different folder structure you can define the rules and test paths as followed:

```bash
cfn-guard-test \
  --rules-path reports \
  --test-path tests/reports
```

When you do not have the `cfn-guard` binary installed, and you need to supply an alternative path you can do that with
the following command:

```bash
cfn-guard-test \
  --cfn-guard-path "/my/custom/path/cfn-guard"
```

### Generate a JUnit XML Report

You can generate a JUnit XML Report using the `--junit-path` option. Once given it will generate a JUnit XML compatible
report at the given location. Example:

```bash
cfn-guard-test \
  --junit-path "reports/cfn-guard.xml"
```

[cfn-guard]: https://github.com/aws-cloudformation/cloudformation-guard "AWS CloudFormation Guard"
[cfn-guard-test]: https://github.com/Nr18/cfn-guard-test "CloudFormation Guard Test"
