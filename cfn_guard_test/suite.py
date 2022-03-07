from typing import List
from cfn_guard_test.case import CfnGuardTestCase


class CfnGuardTestSuite:
    """
    Understands a cfn-guard test suite

    A single cfn-guard test suite can contain 1 or more cfn-guard test cases. A cfn-guard test suite contains are all
    cases defined in a single `<name>_tests.yaml`.
    """

    __name: str
    __cases: List[CfnGuardTestCase]

    def __init__(self, name: str, duration: float) -> None:
        self.__name = name
        self.__duration = duration
        self.__cases = []

    def add_test_case(self, case: CfnGuardTestCase) -> None:
        self.__cases.append(case)

    @property
    def ruleset(self) -> str:
        return self.__name

    @property
    def duration(self) -> float:
        return self.__duration

    @property
    def errors(self) -> int:
        rules = self.error_test_cases
        return len(rules) if rules else 0

    @property
    def passed(self) -> int:
        rules = self.passed_test_cases
        return len(rules) if rules else 0

    @property
    def failed(self) -> int:
        rules = self.failed_test_cases
        return len(rules) if rules else 0

    @property
    def all_test_cases(self) -> List[CfnGuardTestCase]:
        return self.__cases

    @property
    def error_test_cases(self) -> List[CfnGuardTestCase]:
        return list(filter(lambda case: case.errors, self.__cases))

    @property
    def failed_test_cases(self) -> List[CfnGuardTestCase]:
        return list(filter(lambda case: case.failed, self.__cases))

    @property
    def error_messages(self) -> List[str]:
        messages = []
        list(
            map(
                lambda case: messages.append(case.message + "\n\n" + case.details),
                self.error_test_cases,
            )
        )
        return messages

    @property
    def failed_test_cases_messages(self) -> List[str]:
        messages = []

        def extend(case: CfnGuardTestCase) -> None:
            messages.append(case.message)
            messages.extend(case.failed_rules_messages(suite_name=self.ruleset))

        list(map(extend, self.failed_test_cases))
        return list(filter(None, messages))

    @property
    def passed_test_cases(self) -> List[CfnGuardTestCase]:
        return list(filter(lambda case: case.passed, self.__cases))
