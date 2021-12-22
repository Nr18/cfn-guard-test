from typing import List
from cfn_guard_test.suite import CfnGuardTestSuite


class CfnGuardTestSuites:
    """
    Understands a cfn-guard test suites.

    A cfn-guard test suites can contain 1 or more cfn-guard test suite. This is a wrapper on the highest level.
    """

    __suites: List[CfnGuardTestSuite]

    def __init__(self) -> None:
        self.__suites = []

    def add_test_suite(self, case: CfnGuardTestSuite) -> None:
        self.__suites.append(case)

    @property
    def passed(self) -> int:
        passed = 0

        for suite in self.__suites:
            passed += suite.passed

        return passed

    @property
    def failed(self) -> int:
        failed = 0

        for suite in self.__suites:
            failed += suite.failed

        return failed

    @property
    def failed_suites(self) -> List[CfnGuardTestSuite]:
        return list(filter(lambda case: case.failed, self.__suites))
