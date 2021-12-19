class RuleResult:
    """
    Understands the outcome of a specific rule.
    """

    __rule: str
    __expected: str
    __evaluated: str

    def __init__(self, rule: str, expected: str, evaluated: str) -> None:
        self.__rule = rule
        self.__expected = expected
        self.__evaluated = evaluated

    @property
    def rule(self) -> str:
        return self.__rule

    @property
    def passed(self) -> bool:
        return self.__expected == self.__evaluated

    @property
    def failed(self) -> bool:
        return not self.passed
