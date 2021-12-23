import glob
import os
import subprocess
import time
from typing import Callable, Optional

from cfn_guard_test.suites import CfnGuardTestSuites
from cfn_guard_test.reader import CfnGuardReader


class CfnGuardRunner:
    """
    Understands how to execute cfn-guard.
    """

    def __init__(
        self,
        cfn_guard_path: str,
        rules_path: str,
        test_path: str,
        output_callback: Optional[Callable[[str], None]] = None,
    ):
        self.cfn_guard_path = cfn_guard_path
        self.rules_path = rules_path.rstrip("/")
        self.test_path = test_path.rstrip("/")
        self.output_callback = output_callback

    def __print(self, message: str) -> None:
        if self.output_callback:
            self.output_callback(message)

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

    def execute(self) -> CfnGuardTestSuites:
        suite = CfnGuardTestSuites()

        for rules_test_file, rules_file in self.__test_cases.items():
            start_time = time.time()
            self.__print(f"Running {rules_test_file}")
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
            end_time = time.time()
            CfnGuardReader(
                suite, rules_file, response.stdout, duration=end_time - start_time
            )

        return suite
