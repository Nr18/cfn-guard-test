from typing import Optional

import click

from cfn_guard_test.cfn_guard_runner import CfnGuardReportRunner
from cfn_guard_test.test_case import TestCase
from cfn_guard_test.test_suite import TestSuite
from cfn_guard_test.cfn_guard_reader import CfnGuardReportReader


def validate_cfn_guard_path(
    ctx: click.Context, _: click.Option, value: Optional[str]
) -> str:
    if not value or ctx.resilient_parsing:
        return "cfn-guard"

    if value.split("/")[-1] != "cfn-guard":
        raise click.ClickException(
            "When a custom cfn-guard path is given it needs to end on cfn-guard."
        )

    return value


def resolve_paths(ctx: click.Context, _: click.Option, value: Optional[str]) -> str:
    if not value:
        return ctx.params.get("rules_path", "rules")

    return value


@click.command()
@click.option("-r", "--rules-path", callback=resolve_paths)
@click.option("-t", "--test-path", callback=resolve_paths)
@click.option("--cfn-guard-path", callback=validate_cfn_guard_path)
def main(rules_path: str, test_path: str, cfn_guard_path: str) -> None:
    """
    cfn-guard-test

    This tool allows you to easily run your cfn-guard tests against your cfn-guard rules.
    """
    runner = CfnGuardReportRunner(
        cfn_guard_path=cfn_guard_path, rules_path=rules_path, test_path=test_path
    )
    suite = runner.execute()

    print("===== Analyzing Results =====")
    print()

    for case_with_failures in suite.failed_cases:
        for failed_rule in case_with_failures.failed_rules:
            print(
                f'Rule {failed_rule.rule} failed in "{case_with_failures.name}" in {case_with_failures.ruleset}'
            )

    print()
    print(f"Passed {suite.passed}")
    print(f"Failed {suite.failed}")
    print()

    if suite.failed:
        exit(1)


if __name__ == "__main__":
    main()
