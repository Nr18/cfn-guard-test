from typing import List
from cfn_guard_test.rule import CfnGuardRule


class CfnGuardTestCase:
    """
    Understands a cfn-guard test case

    A single cfn-guard test case can contain 1 ore more rules that are evaluated. Each definition in the
    `<name>_tests.yaml` file results in a cfn-guard test case.
    """

    __name: str
    __number: int
    __rules: List[CfnGuardRule]

    def __init__(self, name: str, number: int) -> None:
        self.__name = name
        self.__number = number
        self.__rules = []

    def add_rule(self, rule: CfnGuardRule) -> None:
        self.__rules.append(rule)

    @property
    def name(self) -> str:
        return self.__name

    @property
    def number(self) -> int:
        return self.__number

    @property
    def passed(self) -> int:
        rules = self.passed_rules
        return len(rules) if rules else 0

    @property
    def failed(self) -> int:
        rules = self.failed_rules
        return len(rules) if rules else 0

    @property
    def all_rules(self) -> List[CfnGuardRule]:
        return self.__rules

    @property
    def failed_rules(self) -> List[CfnGuardRule]:
        return list(filter(lambda case: case.failed, self.__rules))

    def failed_rules_messages(self, suite_name: str) -> List[str]:
        messages: List[str] = []

        def extend(rule: CfnGuardRule) -> None:
            messages.append(
                rule.failed_message(
                    suite_name=suite_name, case_number=self.number, case_name=self.name
                )
            )

        list(map(extend, self.failed_rules))
        return messages

    @property
    def passed_rules(self) -> List[CfnGuardRule]:
        return list(filter(lambda case: case.passed, self.__rules))
