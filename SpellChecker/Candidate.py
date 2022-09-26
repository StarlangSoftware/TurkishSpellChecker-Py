from Dictionary.Word import Word
from SpellChecker.Operator import Operator


class Candidate(Word):

    __operator: Operator

    def __init__(self,
                 candidate: str,
                 operator: Operator):
        super().__init__(candidate)
        self.__operator = operator

    def getOperator(self) -> Operator:
        return self.__operator
