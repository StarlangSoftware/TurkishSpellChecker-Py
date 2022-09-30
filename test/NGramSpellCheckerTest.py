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
                Sentence("son derece kısıtlı kelimeler çerçevesinde kendilerini uzun cümlelerle ifade edebiliyorlar"),
                Sentence("minibüs durağı"),
                Sentence("noter belgesi"),
                Sentence("")]
        modified = [Sentence("demokratik cumhüriyet rn kımetli varlıgımızdır"),
                Sentence("bu tblodaki değerler zedelenmeyecektir"),
                Sentence("milliyet'in geeneksel yılin spoşcusu ankşti 43. yeşını doldürdu"),
                Sentence("demokrasinin icşdı buf ayrmıı bulandürdı"),
                Sentence("dışişleri mütseşarı Öymen'in 1997'nin iljk aylğrında Bağdat'a gitmesi öngörülüyor"),
                Sentence("büyüdü , palazandı , devltei eöe geçridi"),
                Sentence("her makenin cültte aklma sürdsi farlkıdır"),
                Sentence("yılın sno ayında 10 gazteci gözlatına alündı"),
                Sentence("iki piotun kulçandığı uçkata üir hotes görçv alyıor"),
                Sentence("son deece kısütlı keilmeler çeçevesinde kendülerini uzuü cümllerle ifüde edbeiliyorlar"),
                Sentence("minibü durağı"),
                Sentence("ntoer belgesi"),
                Sentence("")]
        fsm = FsmMorphologicalAnalyzer()
        nGram = NGram("../ngram.txt")
        nGram.calculateNGramProbabilitiesSimple(NoSmoothing())
        nGramSpellChecker = NGramSpellChecker(fsm, nGram, True)
        for i in range(len(modified)):
            self.assertEqual(original[i].toString(), nGramSpellChecker.spellCheck(modified[i]).toString())

    def test_SpellCheck2(self):
        original = [Sentence("yeni sezon başladı"),
                Sentence("sırtıkara adındaki canlı , bir balıktır"),
                Sentence("siyah ayı , ayıgiller familyasına ait bir ayı türüdür"),
                Sentence("yeni sezon başladı gibi"),
                Sentence("alışveriş için markete gitti"),
                Sentence("küçük bir yalıçapkını geçti"),
                Sentence("meslek odaları birliği yeniden toplandı"),
                Sentence("yeni yılın sonrasında vakalarda artış oldu"),
                Sentence("atomik saatin 10 mhz sinyali kalibrasyon hizmetlerinde referans olarak kullanılmaktadır"),
                Sentence("rehberimiz bu bölgedeki çıngıraklı yılan varlığı hakkında konuştu"),
                Sentence("bu son model cihaz 24 inç ekran büyüklüğünde ve 9 kg ağırlıktadır")]
        modified = [Sentence("yenisezon başladı"),
                Sentence("sırtı kara adındaki canlı , bir balıktır"),
                Sentence("siyahayı , ayıgiller familyasına ait bir ayı türüdür"),
                Sentence("yeni se zon başladı gibs"),
                Sentence("alis veriş için markete gitit"),
                Sentence("kucuk bri yalı çapkını gecti"),
                Sentence("mes lek odaları birliği yendien toplandı"),
                Sentence("yeniyılın sonrasında vakalarda artış oldu"),
                Sentence("atomik saatin 10mhz sinyali kalibrasyon hizmetlerinde referans olarka kullanılmaktadır"),
                Sentence("rehperimiz buı bölgedeki çıngıraklıyılan varlıgı hakkınd konustu"),
                Sentence("bu sno model ciha 24inç ekran büyüklüğünde ve 9kg ağırlıktadır")]
        fsm = FsmMorphologicalAnalyzer()
        nGram = NGram("../ngram.txt")
        nGram.calculateNGramProbabilitiesSimple(NoSmoothing())
        nGramSpellChecker = NGramSpellChecker(fsm, nGram, True)
        for i in range(len(modified)):
            self.assertEqual(original[i].toString(), nGramSpellChecker.spellCheck(modified[i]).toString())

    def test_SpellCheckSurfaceForm(self):
        fsm = FsmMorphologicalAnalyzer()
        nGram = NGram("../ngram.txt")
        nGram.calculateNGramProbabilitiesSimple(NoSmoothing())
        nGramSpellChecker = NGramSpellChecker(fsm, nGram, False)
        self.assertEqual("noter hakkında", nGramSpellChecker.spellCheck(Sentence("noter hakkınad")).__str__())
        self.assertEqual("arçelik'in çamaşır", nGramSpellChecker.spellCheck(Sentence("arçelik'in çamşaır")).__str__())
        self.assertEqual("ruhsat yanında", nGramSpellChecker.spellCheck(Sentence("ruhset yanında")).__str__())


if __name__ == '__main__':
    unittest.main()
