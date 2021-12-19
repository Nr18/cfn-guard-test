from typing import List
from cfn_guard_test.test_case import TestCase


class TestSuite:
    """
    Understands a cfn-guard test suite.
    """

    __cases: List[TestCase]

    def __init__(self) -> None:
        self.__cases = []

    def case_result(self, case: TestCase) -> None:
        self.__cases.append(case)

    @property
    def passed(self) -> int:
        passed = 0

        for case in self.__cases:
            passed += case.passed

        return passed

    @property
    def failed(self) -> int:
        failed = 0

        for case in self.__cases:
            failed += case.failed

        return failed

    @property
    def failed_cases(self) -> List[TestCase]:
        return list(filter(lambda case: case.failed, self.__cases))
