from Corpus.Sentence import Sentence
from Dictionary.Word import Word
from MorphologicalAnalysis.FsmMorphologicalAnalyzer import FsmMorphologicalAnalyzer
from NGram.NGram import NGram
from SpellChecker.Candidate import Candidate
from SpellChecker.Operator import Operator
from SpellChecker.SimpleSpellChecker import SimpleSpellChecker


class NGramSpellChecker(SimpleSpellChecker):
    __nGram: NGram
    __root_n_gram: bool
    __threshold: float

    def __init__(self,
                 fsm: FsmMorphologicalAnalyzer,
                 nGram: NGram,
                 rootNGram: bool):
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
        self.__root_n_gram = rootNGram
        self.__threshold = 0.0

    def checkAnalysisAndSetRootForWordAtIndex(self,
                                              sentence: Sentence,
                                              index: int) -> Word:
        """
        Checks the morphological analysis of the given word in the given index. If there is no misspelling, it returns
        the longest root word of the possible analyses.
        @param sentence Sentence to be analyzed.
        @param index Index of the word
        @return If the word is misspelled, null; otherwise the longest root word of the possible analyses.
        """
        if index < sentence.wordCount():
            fsm_parses = self.fsm.morphologicalAnalysis(sentence.getWord(index).getName())
            if fsm_parses.size() != 0:
                if self.__root_n_gram:
                    return fsm_parses.getParseWithLongestRootWord().getWord()
                else:
                    return sentence.getWord(index)
        return None

    def checkAnalysisAndSetRoot(self, word: str) -> Word:
        fsm_parses = self.fsm.morphologicalAnalysis(word)
        if fsm_parses.size() != 0:
            if self.__root_n_gram:
                return fsm_parses.getParseWithLongestRootWord().getWord()
            else:
                return Word(word)
        return None

    def setThreshold(self, threshold: float):
        self.__threshold = threshold

    def getProbability(self,
                       word1: str,
                       word2: str) -> float:
        return self.__nGram.getProbability(word1, word2)

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
        previous_root = None
        result = Sentence()
        root = self.checkAnalysisAndSetRootForWordAtIndex(sentence, 0)
        next_root = self.checkAnalysisAndSetRootForWordAtIndex(sentence, 1)
        for repeat in range(2):
            i = 0
            while i < sentence.wordCount():
                next_word = None
                previous_word = None
                next_next_word = None
                previous_previous_word = None
                word = sentence.getWord(i)
                if i > 0:
                    previous_word = sentence.getWord(i - 1)
                if i > 1:
                    previous_previous_word = sentence.getWord(i - 2)
                if i < sentence.wordCount() - 1:
                    next_word = sentence.getWord(i + 1)
                if i < sentence.wordCount() - 2:
                    next_next_word = sentence.getWord(i + 2)
                if self.forcedMisspellCheck(word, result) or \
                        self.forcedBackwardMergeCheck(word, result, previous_word):
                    i = i + 1
                    continue
                if self.forcedForwardMergeCheck(word, result, next_word):
                    i = i + 2
                    continue
                if self.forcedSplitCheck(word, result) or self.forcedShortcutCheck(word, result, previous_word):
                    i = i + 1
                    continue
                if root is None:
                    candidates = self.candidateList(word)
                    candidates.extend(self.mergedCandidatesList(previous_word, word, next_word))
                    candidates.extend(self.splitCandidatesList(word))
                    best_candidate = Candidate(word.getName(), Operator.NO_CHANGE)
                    best_root = word
                    best_probability = self.__threshold
                    for candidate in candidates:
                        if candidate.getOperator() == Operator.SPELL_CHECK or \
                                candidate.getOperator() == Operator.MISSPELLED_REPLACE:
                            root = self.checkAnalysisAndSetRoot(candidate.getName())
                        if candidate.getOperator() == Operator.BACKWARD_MERGE and previous_word is not None \
                                and previous_previous_word is not None:
                            root = self.checkAnalysisAndSetRoot(previous_word.getName() + word.getName())
                            previous_root = self.checkAnalysisAndSetRoot(previous_previous_word.getName())
                        if candidate.getOperator() == Operator.FORWARD_MERGE and next_word is not None \
                                and next_next_word is not None:
                            root = self.checkAnalysisAndSetRoot(word.getName() + next_word.getName())
                            next_root = self.checkAnalysisAndSetRoot(next_next_word.getName())
                        if previous_root is not None:
                            if candidate.getOperator() == Operator.SPLIT:
                                root = self.checkAnalysisAndSetRoot(candidate.getName().split(" ")[0])
                            previous_probability = self.__nGram.getProbability(previous_root.getName(), root.getName())
                        else:
                            previous_probability = 0.0
                        if next_root is not None:
                            if candidate.getOperator() == Operator.SPLIT:
                                root = self.checkAnalysisAndSetRoot(candidate.getName().split(" ")[1])
                            next_probability = self.__nGram.getProbability(root.getName(), next_root.getName())
                        else:
                            next_probability = 0.0
                        if max(previous_probability, next_probability) > best_probability:
                            best_candidate = candidate
                            best_root = root
                            best_probability = max(previous_probability, next_probability)
                    if best_candidate.getOperator() == Operator.FORWARD_MERGE:
                        i = i + 1
                    if best_candidate.getName() == Operator.BACKWARD_MERGE:
                        result.replaceWord(i - 1, Word(best_candidate.getName()))
                    else:
                        result.addWord(Word(best_candidate.getName()))
                    root = best_root
                else:
                    result.addWord(word)
                previous_root = root
                root = next_root
                next_root = self.checkAnalysisAndSetRootForWordAtIndex(sentence, i + 2)
                i = i + 1
            sentence = result
            if repeat < 1:
                result = Sentence()
                previous_root = None
                root = self.checkAnalysisAndSetRootForWordAtIndex(sentence, 0)
                next_root = self.checkAnalysisAndSetRootForWordAtIndex(sentence, 1)
        return result
