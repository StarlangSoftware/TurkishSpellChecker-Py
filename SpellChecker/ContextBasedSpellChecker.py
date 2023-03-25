from Corpus.Sentence import Sentence
from Dictionary.Word import Word
from MorphologicalAnalysis.FsmMorphologicalAnalyzer import FsmMorphologicalAnalyzer
from MorphologicalAnalysis.FsmParseList import FsmParseList
from NGram.NGram import NGram

from SpellChecker.Candidate import Candidate
from SpellChecker.NGramSpellChecker import NGramSpellChecker
from SpellChecker.Operator import Operator
from SpellChecker.SpellCheckerParameter import SpellCheckerParameter


class ContextBasedSpellChecker(NGramSpellChecker):
    __context_list: dict

    def __init__(self,
                 fsm: FsmMorphologicalAnalyzer,
                 nGram: NGram,
                 parameter: SpellCheckerParameter):
        """
        A constructor of {@link ContextBasedSpellChecker} class which takes a {@link FsmMorphologicalAnalyzer}, an {@link NGram}
        and a {@link SpellCheckerParameter} as inputs. Then, calls its super class {@link NGramSpellChecker} with given inputs.
        :param fsm: {@link FsmMorphologicalAnalyzer} type input.
        :param nGram: {@link NGram} type input.
        :param parameter: {@link SpellCheckerParameter} type input.
        """
        super().__init__(fsm,
                         nGram,
                         parameter)
        self.loadContextDictionaries()

    def loadContextDictionaries(self):
        """
        This method also loads context information from a file.
        """
        self.__context_list = {}
        input_file = self.getFile('context_list.txt')
        lines = input_file.readlines()
        for line in lines:
            items = line.strip().split("\t")
            if len(items) == 2:
                word = items[0]
                otherWords = items[1].split(" ")
                self.__context_list[word] = otherWords
        input_file.close()

    def candidateList(self, word: Word, sentence: Sentence) -> list:
        """
        Uses context information to generate candidates for a misspelled word.
        The candidates are the words that are in the context of the neighbouring words of the misspelled word.
        Uses the {@Link damerauLevenshteinDistance(String, String) method to calculate the distance between the misspelled word and
        the candidates and to determine whether the candidates are valid.
        :param word: the misspelled word
        :param sentence: the sentence containing the misspelled word
        :return: an ArrayList of valid candidates for the misspelled word
        """
        words = []
        candidates = set()
        valid_candidates = []
        for w in sentence.getWords():
            if w != word:
                words.append(w)
        for w in words:
            parses: FsmParseList = self.fsm.morphologicalAnalysis(Word.toCapital(w.getName()))
            if parses.size() > 0:
                root = parses.getParseWithLongestRootWord().getWord().getName()
                if self.__context_list.get(root) is not None:
                    for s in self.__context_list[root]:
                        candidates.add(Candidate(s, Operator.CONTEXT_BASED))
        for candidate in candidates:
            if len(candidate.getName()) < 5:
                distance = 1
            elif len(candidate.getName()) < 7:
                distance = 2
            else:
                distance = 3
            if self.damerauLevenshteinDistance(word.getName(), candidate.getName()) <= distance:
                valid_candidates.append(candidate)
        return valid_candidates

    def damerauLevenshteinDistance(self,
                                   first: str,
                                   second: str) -> int:
        """
        Calculates the Damerau-Levenshtein distance between two strings.
        This method also allows for the transposition of adjacent characters,
        which is not possible in a standard Levenshtein distance calculation.
        :param first: the first string
        :param second: the second string
        :return: the Damerau-Levenshtein distance between the two strings
        """
        if first is None or first == "":
            if second is None or second == "":
                return 0
            else:
                return len(second)
        if second is None or second == "":
            return len(first)
        first_length = len(first)
        second_length = len(second)
        distance_matrix = []
        for first_index in range(first_length + 1):
            distance_matrix.append([])
            for second_index in range(second_length + 1):
                distance_matrix[first_index].append(0)
        for first_index in range(first_length + 1):
            distance_matrix[first_index][0] = first_index
        for second_index in range(second_length + 1):
            distance_matrix[0][second_index] = second_index
        for first_index in range(1, first_length + 1):
            for second_index in range(1, second_length + 1):
                if first[first_index - 1] == second[second_index - 1]:
                    cost = 0
                else:
                    cost = 1
                distance_matrix[first_index][second_index] = min(min(distance_matrix[first_index - 1][second_index] + 1,
                                                                  distance_matrix[first_index][second_index - 1] + 1),
                                                              distance_matrix[first_index - 1][second_index - 1] + cost)
                if first_index == 1 or second_index == 1:
                    continue
                if first[first_index - 1] == second[second_index - 2] and first[first_index - 2] == second[
                    second_index - 1]:
                    distance_matrix[first_index][second_index] = min(distance_matrix[first_index][second_index],
                                                                  distance_matrix[first_index - 2][
                                                                      second_index - 2] + cost)
        return distance_matrix[first_length][second_length]
