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
        return sum(map(lambda suite: suite.passed, self.passed_suites), 0)

    @property
    def failed(self) -> int:
        return sum(map(lambda suite: suite.failed, self.failed_suites), 0)

    @property
    def all_suites(self) -> List[CfnGuardTestSuite]:
        return self.__suites

    @property
    def failed_suites(self) -> List[CfnGuardTestSuite]:
        return list(filter(lambda case: case.failed, self.__suites))

    @property
    def failed_suites_messages(self) -> List[str]:
        messages = []

        def extend(suite: CfnGuardTestSuite) -> None:
            messages.extend(suite.failed_test_cases_messages)

        list(map(extend, self.failed_suites))
        return messages

    @property
    def passed_suites(self) -> List[CfnGuardTestSuite]:
        return list(filter(lambda case: case.passed, self.__suites))
