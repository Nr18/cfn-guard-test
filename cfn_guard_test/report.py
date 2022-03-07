from typing import List

from cfn_guard_test.rule import CfnGuardRule
from cfn_guard_test.case import CfnGuardTestCase, ErrorTestCase
from cfn_guard_test.suites import CfnGuardTestSuites
from junit_xml import TestCase, TestSuite, to_xml_report_string


class CfnGuardReport:
    """
    Understands how to create reports
    """

    __suites: List[TestSuite]

    def __init__(self, suites: CfnGuardTestSuites):

        self.__suites = []

        for suite in suites.all_suites:
            self.__timestamp = suite.duration

            self.__suites.append(
                TestSuite(
                    name=suite.ruleset, test_cases=self.__get_all_test_cases(suite)
                )
            )

    @property
    def elapsed_sec(self) -> float:
        """
        Because we only have the time for the whole suite we will only return this once to the case.
        """
        timestamp = 0.0

        if self.__timestamp:
            timestamp = self.__timestamp
            self.__timestamp = 0.0

        return timestamp

    def __get_all_test_cases(self, suite):
        cases = []

        for case in suite.all_test_cases:
            if case.errors:
                cases.append(self.__create_error(case))

            for rule in case.all_rules:
                cases.append(self.__create_test_case(case=case, rule=rule))

        return cases

    def __create_error(self, error: ErrorTestCase) -> TestCase:
        test_case = TestCase(name=error.name, elapsed_sec=self.elapsed_sec)
        test_case.add_error_info(message=error.message, output=error.details)

        return test_case

    def __create_test_case(
        self, case: CfnGuardTestCase, rule: CfnGuardRule
    ) -> TestCase:
        test_case = TestCase(
            name=rule.name, classname=case.name, elapsed_sec=self.elapsed_sec
        )

        if rule.skipped:
            test_case.add_skipped_info(
                f'Rule {rule.name} was skipped on case #{case.number} "{case.name}"',
                output=case.details,
            )

        if rule.failed:
            test_case.add_failure_info(
                f'Rule {rule.name} failed on case #{case.number} "{case.name}"',
                output=case.details,
            )

        return test_case

    def write(self, path: str) -> None:
        with open(path, "w") as f:
            f.write(to_xml_report_string(self.__suites, prettyprint=True))
