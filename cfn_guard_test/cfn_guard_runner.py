import glob
import os
import subprocess

from cfn_guard_test.test_suite import TestSuite
from cfn_guard_test.cfn_guard_reader import CfnGuardReportReader


class CfnGuardReportRunner:
    """
    Understands how to execute cfn-guard.
    """

    def __init__(self, cfn_guard_path: str, rules_path: str, test_path: str):
        self.cfn_guard_path = cfn_guard_path
        self.rules_path = rules_path
        self.test_path = test_path

    @property
    def __test_cases(self) -> dict:
        rule_sets = {}
        tests = glob.glob(f"{self.test_path}/*_tests.yaml")

        for test in tests:
            test_name = os.path.basename(test)
            rule_name = test_name.split("_")[0]

            if os.path.isfile(f"{self.rules_path}/{rule_name}.guard"):
                rule_sets[test] = f"{self.rules_path}/{rule_name}.guard"

        return rule_sets

    def execute(self) -> TestSuite:
        suite = TestSuite()

        for rules_test_file, rules_file in self.__test_cases.items():
            response = subprocess.run(
                [
                    self.cfn_guard_path,
                    "test",
                    "--rules-file",
                    rules_file,
                    "--test-data",
                    rules_test_file,
                ],
                stdout=subprocess.PIPE,
            )
            CfnGuardReportReader(suite, rules_file, response.stdout)

        return suite
