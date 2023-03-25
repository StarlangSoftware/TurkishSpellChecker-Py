from Dictionary.Word import Word
from SpellChecker.Operator import Operator


class Candidate(Word):

    __operator: Operator

    def __init__(self,
                 candidate: str,
                 operator: Operator):
        """
        Constructs a new Candidate object with the specified candidate and operator.
        :param candidate: The word candidate to be checked for spelling.
        :param operator: The operator to be applied to the candidate in the spell checking process.
        """
        super().__init__(candidate)
        self.__operator = operator

    def getOperator(self) -> Operator:
        """
        Returns the operator associated with this candidate.
        :return: The operator associated with this candidate.
        """
        return self.__operator
