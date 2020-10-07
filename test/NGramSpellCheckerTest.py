import unittest

from Corpus.Sentence import Sentence
from MorphologicalAnalysis.FsmMorphologicalAnalyzer import FsmMorphologicalAnalyzer
from NGram.NGram import NGram
from NGram.NoSmoothing import NoSmoothing

from SpellChecker.NGramSpellChecker import NGramSpellChecker


class NGramSpellCheckerTest(unittest.TestCase):

    def test_SpellCheck(self):
        original = [Sentence("demokratik cumhuriyet en kıymetli varlığımızdır"),
                Sentence("bu tablodaki değerler zedelenmeyecektir"),
                Sentence("milliyet'in geleneksel yılın sporcusu anketi 43. yaşını doldurdu"),
                Sentence("demokrasinin icadı bu ayrımı bulandırdı"),
                Sentence("dışişleri müsteşarı Öymen'in 1997'nin ilk aylarında Bağdat'a gitmesi öngörülüyor"),
                Sentence("büyüdü , palazlandı , devleti ele geçirdi"),
                Sentence("her maskenin ciltte kalma süresi farklıdır"),
                Sentence("yılın son ayında 10 gazeteci gözaltına alındı"),
                Sentence("iki pilotun kullandığı uçakta bir hostes görev alıyor"),
                Sentence("son derece kısıtlı kelimeler çerçevesinde kendilerini uzun cümlelerle ifade edebiliyorlar")]
        modified = [Sentence("demokratik cumhüriyet en kımetli varlıgımızdır"),
                Sentence("bu tblodaki değerlğr zedelenmeyecüktir"),
                Sentence("milliyet'in geeneksel yılın spoşcusu ankşti 43. yeşını doldürdu"),
                Sentence("demokrasinin icşdı bu ayrmıı bulandürdı"),
                Sentence("dışişleri mütseşarı Öymen'in 1997'nin ilk aylğrında Bağdat'a gitmesi öngörülüyor"),
                Sentence("büyüdü , palazandı , devltei ele geçridi"),
                Sentence("her makenin cültte kalma sürdsi farlkıdır"),
                Sentence("yılın sno ayında 10 gazteci gözlatına alündı"),
                Sentence("iki piotun kulçandığı uçkata üir hotes görçv alyıor"),
                Sentence("son deece kısütlı keilmeler çeçevesinde kendülerini uzuü cümllerle ifüde edbeiliyorlar")]
        fsm = FsmMorphologicalAnalyzer("../turkish_dictionary.txt", "../turkish_misspellings.txt",
                                       "../turkish_finite_state_machine.xml")
        nGram = NGram("../ngram.txt")
        nGram.calculateNGramProbabilitiesSimple(NoSmoothing())
        nGramSpellChecker = NGramSpellChecker(fsm, nGram)
        for i in range(len(modified)):
            self.assertEqual(original[i].toString(), nGramSpellChecker.spellCheck(modified[i]).toString())


if __name__ == '__main__':
    unittest.main()
