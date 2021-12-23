import re
from typing import Optional, List

from cfn_guard_test.case import CfnGuardTestCase
from cfn_guard_test.suites import CfnGuardTestSuites
from cfn_guard_test.suite import CfnGuardTestSuite
from cfn_guard_test.rule import CfnGuardRule


class CfnGuardReader:
    """
    Understands how to read the output of cfn-guard.
    """

    __suites: CfnGuardTestSuites
    __rule_name: str
    __duration: float

    def __init__(
        self, suites: CfnGuardTestSuites, rule_name: str, report: bytes, duration: float
    ):
        self.__suites = suites
        self.__rule_name = rule_name
        self.__duration = duration

        self.__suite = CfnGuardTestSuite(
            name=self.__rule_name, duration=self.__duration
        )
        self.__suites.add_test_suite(self.__suite)

        sections = report.decode("utf-8").split("\n\n")
        list(map(lambda section: self.__parse_section(section), sections))

    def __parse_section(self, test_case: str) -> None:
        if not test_case.strip():
            return None

        case_number = self.__get_case_number(test_case)
        case_name = self.__get_case_name(test_case)

        if case_number and case_name:
            case = CfnGuardTestCase(name=case_name, number=case_number)
            list(map(case.add_rule, self.__get_rule_results(test_case)))

            self.__suite.add_test_case(case)

    @staticmethod
    def __get_case_number(test_case) -> Optional[int]:
        match = re.search(r"Test Case #([0-9]+)", test_case, re.MULTILINE)
        return int(match.group(1)) if match else None

    @staticmethod
    def __get_case_name(test_case: str) -> Optional[str]:
        match = re.search(r"Name: \"(.*)\"", test_case, re.MULTILINE)
        return match.group(1) if match else None

    @staticmethod
    def __get_rule_results(test_case) -> List[CfnGuardRule]:
        results = []
        matches = re.finditer(
            r"    (.*): Expected = ([A-Z]+), Evaluated = ([A-Z]+)",
            test_case,
            re.MULTILINE,
        )

        for matchNum, match in enumerate(matches, start=1):
            rule = match.groups(matchNum)
            results.append(CfnGuardRule(rule[0], rule[1], rule[2]))

        return results
