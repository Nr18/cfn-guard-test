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
