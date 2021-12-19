from typing import List
import subprocess
import os
import pytest

from unittest.mock import patch, MagicMock
from click.testing import CliRunner
from cfn_guard_test import main


@pytest.mark.parametrize(
    "payload, parameters, rule_exists, test_file, rule_file, expected_exit_code",
    [
        # Test 0
        ("skipped_rule.txt", [], True, "rules/iam_tests.yaml", "rules/iam.guard", 0),
        # Test 1
        ("skipped_rule.txt", [], False, "rules/iam_tests.yaml", "rules/iam.guard", 0),
        # Test 2
        (
            "skipped_rule.txt",
            ["--cfn-guard-path", "cfn-guard-fake"],
            False,
            "rules/iam_tests.yaml",
            "rules/iam.guard",
            1,
        ),
        # Test 3
        (
            "skipped_rule.txt",
            ["--cfn-guard-path", "cfn-guard"],
            True,
            "rules/iam_tests.yaml",
            "rules/iam.guard",
            0,
        ),
        # Test 4
        (
            "skipped_rule.txt",
            ["--rules-path", "my-rules"],
            True,
            "my-rules/iam_tests.yaml",
            "my-rules/iam.guard",
            0,
        ),
        # Test 5
        (
            "skipped_rule.txt",
            ["--rules-path", "my-rules", "--test-path", "my-rules"],
            True,
            "my-rules/iam_tests.yaml",
            "my-rules/iam.guard",
            0,
        ),
        # Test 6
        (
            "skipped_rule.txt",
            ["--rules-path", "my-rules", "--test-path", "my-tests"],
            True,
            "my-tests/iam_tests.yaml",
            "my-rules/iam.guard",
            0,
        ),
        # Test 7
        (
            "passing_rule.txt",
            [],
            True,
            "rules/iam_tests.yaml",
            "rules/iam.guard",
            0,
        ),
        # Test 8
        (
            "failed_rule.txt",
            [],
            True,
            "rules/iam_tests.yaml",
            "rules/iam.guard",
            1,
        ),
        # Test 9
        ("empty.txt", [], True, "rules/iam_tests.yaml", "rules/iam.guard", 0),
        # Test 10
        (
            "invalid_case_name.txt",
            [],
            True,
            "rules/iam_tests.yaml",
            "rules/iam.guard",
            0,
        ),
        # Test 11
        (
            "invalid_case_number.txt",
            [],
            True,
            "rules/iam_tests.yaml",
            "rules/iam.guard",
            0,
        ),
        # Test 12
        (
            "invalid_case_number_and_name.txt",
            [],
            True,
            "rules/iam_tests.yaml",
            "rules/iam.guard",
            0,
        ),
    ],
)
@patch("cfn_guard_test.cfn_guard_runner.subprocess.run")
@patch("cfn_guard_test.cfn_guard_runner.glob.glob")
@patch("cfn_guard_test.cfn_guard_runner.os.path.isfile")
def test_invoke(
    mock_isfile: MagicMock,
    mock_glob: MagicMock,
    mock_run: MagicMock,
    payload_path: str,
    payload: str,
    parameters: List,
    rule_exists: bool,
    test_file: str,
    rule_file: str,
    expected_exit_code: int,
) -> None:
    mock_glob.return_value = [test_file]
    mock_isfile.return_value = rule_exists

    with open(f"{payload_path}/{payload}", "rb") as fh:
        mock_stdout = MagicMock()
        mock_stdout.stdout = fh.read()
        mock_run.return_value = mock_stdout

    runner = CliRunner()
    result = runner.invoke(main, parameters)
    assert result.exit_code == expected_exit_code

    if expected_exit_code == 0:
        mock_isfile.assert_called_with(rule_file)
        name = os.path.basename(test_file).split("_tests.yaml")[0]
        mock_glob.assert_called_with(test_file.replace(name, "*"))

        if rule_exists:
            mock_run.assert_called_with(
                [
                    "cfn-guard",
                    "test",
                    "--rules-file",
                    rule_file,
                    "--test-data",
                    test_file,
                ],
                stdout=subprocess.PIPE,
            )
