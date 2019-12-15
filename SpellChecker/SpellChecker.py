from abc import abstractmethod

from Corpus.Sentence import Sentence


class SpellChecker:

    """
    The spellCheck method which takes a {@link Sentence} as an input.

    PARAMETERS
    ----------
    sentence : Sentence
        Sentence type input.

    RETURNS
    -------
    Sentence
        Sentence result.
    """
    @abstractmethod
    def spellCheck(self, sentence: Sentence) -> Sentence:
        pass
