from typing import Optional, Callable

import click

from cfn_guard_test.case import CfnGuardTestCase
from cfn_guard_test.report import CfnGuardReport
from cfn_guard_test.rule import CfnGuardRule
from cfn_guard_test.runner import CfnGuardRunner
from cfn_guard_test.suite import CfnGuardTestSuite
from cfn_guard_test.suites import CfnGuardTestSuites
from cfn_guard_test.reader import CfnGuardReader


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


def validate_writable_path(
    ctx: click.Context, _: click.Option, value: Optional[str]
) -> Optional[str]:

    try:
        if value:
            with open(value, "w") as fh:
                if not fh.writable():
                    raise Exception()
    except FileNotFoundError:
        raise click.ClickException(f"The given path is not writable: {value}")
    except Exception:
        raise click.ClickException(f"The given path is not writable: {value}")

    return value


@click.command()
@click.option("-r", "--rules-path", callback=resolve_paths)
@click.option("-t", "--test-path", callback=resolve_paths)
@click.option("--cfn-guard-path", callback=validate_cfn_guard_path)
@click.option("--junit-path", callback=validate_writable_path)
@click.option("-v", "--verbose", count=True)
def main(
    rules_path: str,
    test_path: str,
    cfn_guard_path: str,
    junit_path: Optional[str],
    verbose: int,
) -> None:
    """
    cfn-guard-test

    This tool allows you to easily run your cfn-guard tests against your cfn-guard rules.
    """
    click.echo("===== Analyzing Results =====")
    click.echo()

    suites = CfnGuardRunner(
        cfn_guard_path=cfn_guard_path,
        rules_path=rules_path,
        test_path=test_path,
        output_callback=resolve_output_callback(verbose),
    ).execute()

    if junit_path:
        CfnGuardReport(suites).write(junit_path)

    click.echo()
    click.echo(f"Errors {suites.errors}")
    click.echo(f"Failed {suites.failed}")
    click.echo(f"Passed {suites.passed}")
    click.echo()
    display_failures_errors(suites)


def display_failures_errors(suites: CfnGuardTestSuites) -> None:

    if suites.errors:
        click.echo(click.style("Errors:", bold=True))
        list(map(click.echo, suites.error_messages))
        click.echo()

    if suites.failed:
        click.echo(click.style("Failures:", bold=True))
        list(map(click.echo, suites.failure_messages))
        click.echo()

    if suites.errors or suites.failed:
        exit(1)


def resolve_output_callback(verbose) -> Optional[Callable[[str], None]]:
    return click.echo if verbose else None


if __name__ == "__main__":
    main()
