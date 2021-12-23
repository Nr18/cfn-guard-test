class CfnGuardRule:
    """
    Understands the outcome of a specific rule.

    A single cfn-guard rule contains the result of the evaluated rule. Each rule definition in the `expectations`
    section of the `<name>_tests.yaml` file results in a cfn-guard rule.
    """

    __name: str
    __expected: str
    __evaluated: str

    def __init__(self, name: str, expected: str, evaluated: str) -> None:
        self.__name = name
        self.__expected = expected
        self.__evaluated = evaluated

    @property
    def name(self) -> str:
        return self.__name

    @property
    def passed(self) -> bool:
        return self.__expected == self.__evaluated

    @property
    def failed(self) -> bool:
        return not self.passed

    @property
    def skipped(self) -> bool:
        return self.__expected == "SKIP" and self.passed

    def failed_message(self, suite_name: str, case_number: int, case_name: str) -> str:
        return (
            f'Rule {self.name} failed on #{case_number} "{case_name}" in {suite_name}'
        )
