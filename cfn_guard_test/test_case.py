from typing import List
from cfn_guard_test.rule_result import RuleResult


class TestCase:
    """
    Understands a cfn-guard test case
    """

    __ruleset: str
    __name: str
    __number: int
    __rules: List[RuleResult]

    def __init__(self, ruleset: str, name: str, number: int) -> None:
        self.__ruleset = ruleset
        self.__name = name
        self.__number = number
        self.__rules = []

    def rule_result(self, rule: RuleResult) -> None:
        self.__rules.append(rule)

    @property
    def name(self) -> str:
        return self.__name

    @property
    def ruleset(self) -> str:
        return self.__ruleset

    @property
    def passed(self) -> int:
        rules = self.passed_rules
        return len(rules) if rules else 0

    @property
    def failed(self) -> int:
        rules = self.failed_rules
        return len(rules) if rules else 0

    @property
    def failed_rules(self) -> List[RuleResult]:
        return list(filter(lambda case: case.failed, self.__rules))

    @property
    def passed_rules(self) -> List[RuleResult]:
        return list(filter(lambda case: case.passed, self.__rules))
