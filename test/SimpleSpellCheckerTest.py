import unittest

from Corpus.Sentence import Sentence
from MorphologicalAnalysis.FsmMorphologicalAnalyzer import FsmMorphologicalAnalyzer

from SpellChecker.SimpleSpellChecker import SimpleSpellChecker


class SimpleSpellCheckerTest(unittest.TestCase):

    def test_SpellCheck(self):
        fsm = FsmMorphologicalAnalyzer()
        simpleSpellChecker = SimpleSpellChecker(fsm)
        input = open("../misspellings.txt")
        lines = input.readlines()
        for line in lines:
            items = line.strip().split(" ")
            misspelled = items[0]
            corrected = items[1]
            self.assertEqual(corrected, simpleSpellChecker.spellCheck(Sentence(misspelled)).toString())


if __name__ == '__main__':
    unittest.main()
