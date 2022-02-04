import builtins
from typing import List
import subprocess
import os
import pytest

from unittest.mock import patch, MagicMock, mock_open, call
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
            "passing_rule.txt",
            ["--verbose"],
            True,
            "rules/iam_tests.yaml",
            "rules/iam.guard",
            0,
        ),
        # Test 9
        (
            "failed_rule.txt",
            [],
            True,
            "rules/iam_tests.yaml",
            "rules/iam.guard",
            1,
        ),
        # Test 10
        ("empty.txt", [], True, "rules/iam_tests.yaml", "rules/iam.guard", 1),
        # Test 11
        (
            "invalid_case_name.txt",
            [],
            True,
            "rules/iam_tests.yaml",
            "rules/iam.guard",
            1,
        ),
        # Test 12
        (
            "invalid_case_number.txt",
            [],
            True,
            "rules/iam_tests.yaml",
            "rules/iam.guard",
            1,
        ),
        # Test 13
        (
            "invalid_case_number_and_name.txt",
            [],
            True,
            "rules/iam_tests.yaml",
            "rules/iam.guard",
            1,
        ),
    ],
)
@patch("cfn_guard_test.runner.subprocess.run")
@patch("cfn_guard_test.runner.glob.glob")
@patch("cfn_guard_test.runner.os.path.isfile")
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


@patch("cfn_guard_test.runner.subprocess.run")
@patch("cfn_guard_test.runner.glob.glob")
@patch("cfn_guard_test.runner.os.path.isfile")
def test_invoke_cfn_guard_failure(
    mock_isfile: MagicMock, mock_glob: MagicMock, mock_run: MagicMock
) -> None:
    mock_glob.return_value = ["rules/iam_tests.yaml"]
    mock_isfile.return_value = True

    mock_stdout = MagicMock()
    mock_stdout.stdout = bytes(
        "Error processing Parser Error when parsing Unable to process data in file...",
        "utf-8",
    )
    mock_run.return_value = mock_stdout

    runner = CliRunner()
    result = runner.invoke(main, [])
    assert result.exit_code == 1
    assert "Unable to read the output when testing 'rules/iam.guard'!" in result.stdout
    assert (
        "Error processing Parser Error when parsing Unable to process data in file..."
        in result.stdout
    )


@pytest.mark.parametrize(
    "payload, expected_exit_code",
    [
        ("2passing_rules", 0),
        ("empty", 1),
        ("failed_rule", 1),
        ("invalid_case_name", 1),
        ("invalid_case_number", 1),
        ("invalid_case_number_and_name", 1),
        ("passing_rule", 0),
        ("skipped_rule", 0),
    ],
)
@patch("cfn_guard_test.runner.subprocess.run")
@patch("cfn_guard_test.runner.glob.glob")
@patch("cfn_guard_test.runner.os.path.isfile")
@patch("cfn_guard_test.runner.time")
def test_junit(
    mock_time: MagicMock,
    mock_isfile: MagicMock,
    mock_glob: MagicMock,
    mock_run: MagicMock,
    payload_path: str,
    payload: str,
    expected_exit_code: int,
) -> None:
    mock_glob.return_value = ["rules/iam_tests.yaml"]
    mock_isfile.return_value = True
    mock_time.time.side_effect = [0.0, 0.5]

    with open(f"{payload_path}/{payload}.txt", "rb") as fh:
        mock_stdout = MagicMock()
        mock_stdout.stdout = fh.read()
        mock_run.return_value = mock_stdout

    mock_write = mock_open()
    with patch.object(builtins, "open", mock_write, create=True):
        runner = CliRunner()
        result = runner.invoke(main, ["--junit-path", "my-report-path/cfn-guard.xml"])
        assert result.exit_code == expected_exit_code

    mock_write.assert_called_with("my-report-path/cfn-guard.xml", "w")

    with open(f"{payload_path}/{payload}.xml", "rb") as fh:
        mock_write.return_value.write.assert_called_once_with(fh.read().decode("utf-8"))


def test_junit_non_writable_path() -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["--junit-path", "my-report-path/cfn-guard.xml"])
    assert result.exit_code == 1


def test_junit_non_writable_file() -> None:
    mock_write = mock_open()

    mock_write.return_value.writable.return_value = False

    with patch.object(builtins, "open", mock_write, create=True):
        runner = CliRunner()
        result = runner.invoke(main, ["--junit-path", "my-report-path/cfn-guard.xml"])
        assert result.exit_code == 1
