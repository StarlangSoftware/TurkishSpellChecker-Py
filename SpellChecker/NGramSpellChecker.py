from Corpus.Sentence import Sentence
from Dictionary.Word import Word
from MorphologicalAnalysis.FsmMorphologicalAnalyzer import FsmMorphologicalAnalyzer
from NGram.NGram import NGram

from SpellChecker.SimpleSpellChecker import SimpleSpellChecker


class NGramSpellChecker(SimpleSpellChecker):

    __nGram: NGram

    def __init__(self, fsm: FsmMorphologicalAnalyzer, nGram: NGram):
        """
        A constructor of NGramSpellChecker class which takes a FsmMorphologicalAnalyzer and an NGram as inputs. Then,
        calls its super class SimpleSpellChecker with given FsmMorphologicalAnalyzer and assigns given NGram to the
        nGram variable.

        PARAMETERS
        ----------
        fsm : FsmMorphologicalAnalyzer
            FsmMorphologicalAnalyzer type input.
        nGram : NGram
            NGram type input.
        """
        super().__init__(fsm)
        self.__nGram = nGram

    def spellCheck(self, sentence: Sentence) -> Sentence:
        """
        The spellCheck method takes a Sentence as an input and loops i times where i ranges from 0 to size of words in
        given sentence. Then, it calls morphologicalAnalysis method with each word and assigns it to the FsmParseList,
        if the size of FsmParseList is equal to the 0, it adds current word to the candidateList and assigns it to the
        candidates list.

        Later on, it loops through candidates list and calls morphologicalAnalysis method with each word and assigns it
        to the FsmParseList. Then, it gets the root from FsmParseList. For the first time, it defines a previousRoot by
        calling getProbability method with root, and for the following times it calls getProbability method with
        previousRoot and root. Then, it finds out the best probability and the corresponding candidate as best candidate
        and adds it to the result Sentence.

        If the size of FsmParseList is not equal to 0, it directly adds the current word to the result Sentence and
        finds the previousRoot directly from the FsmParseList.

        PARAMETERS
        ----------
        sentence : Sentence
            Sentence type input.

        RETURNS
        -------
        Sentence
            Sentence result.
        """
        previousRoot = None
        result = Sentence()
        for i in range(sentence.wordCount()):
            word = sentence.getWord(i)
            fsmParses = self.fsm.morphologicalAnalysis(word.getName())
            if fsmParses.size() == 0:
                candidates = self.candidateList(word)
                bestCandidate = word.getName()
                bestRoot = word
                bestProbability = 0.0
                for candidate in candidates:
                    fsmParses = self.fsm.morphologicalAnalysis(candidate)
                    root = fsmParses.getParseWithLongestRootWord().getWord()
                    if previousRoot is not None:
                        probability = self.__nGram.getProbability(previousRoot.getName(), root.getName())
                    else:
                        probability = self.__nGram.getProbability(root.getName())
                    if probability > bestProbability:
                        bestCandidate = candidate
                        bestRoot = root
                        bestProbability = probability
                previousRoot = bestRoot
                result.addWord(Word(bestCandidate))
            else:
                result.addWord(word)
                previousRoot = fsmParses.getParseWithLongestRootWord().getWord()
        return result
