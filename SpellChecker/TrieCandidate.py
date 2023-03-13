from SpellChecker.Candidate import Candidate
from SpellChecker.Operator import Operator


class TrieCandidate(Candidate):

    __current_index: int
    __current_penalty: float

    def __init__(self,
                 word: str,
                 current_index: int,
                 current_penalty: float):
        """
        Constructs a TrieCandidate object.
        :param word: the candidate word
        :param current_index: the current index of the candidate word
        :param current_penalty: the currentPenalty associated with the candidate word
        """
        super().__init__(word, Operator.TRIE_BASED)
        self.__current_index = current_index
        self.__current_penalty = current_penalty

    def getCurrentIndex(self) -> int:
        """
        Returns the current index of the candidate word.
        :return: the current index of the candidate word
        """
        return self.__current_index

    def getCurrentPenalty(self) -> float:
        """
        Returns the currentPenalty value associated with the candidate word.
        :return: the currentPenalty value associated with the candidate word
        """
        return self.__current_penalty

    def nextIndex(self):
        """
        Increments the current index of the candidate word by 1.
        """
        self.__current_index = self.__current_index + 1
