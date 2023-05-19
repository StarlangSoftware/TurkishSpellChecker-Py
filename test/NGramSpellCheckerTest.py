import unittest

from Corpus.Sentence import Sentence
from MorphologicalAnalysis.FsmMorphologicalAnalyzer import FsmMorphologicalAnalyzer
from NGram.NGram import NGram
from NGram.NoSmoothing import NoSmoothing

from SpellChecker.NGramSpellChecker import NGramSpellChecker
from SpellChecker.SpellCheckerParameter import SpellCheckerParameter


class NGramSpellCheckerTest(unittest.TestCase):

    def test_SpellCheck(self):
        original = [Sentence("demokratik cumhuriyet en kıymetli varlığımızdır"),
                Sentence("bu tablodaki değerler zedelenmeyecektir"),
                Sentence("vakfın geleneksel yılın sporcusu anketi yeni yaşını doldurdu"),
                Sentence("demokrasinin icadı bu ayrımı bulandırdı"),
                Sentence("dışişleri müsteşarı Öymen'in 1997'nin ilk aylarında Bağdat'a gitmesi öngörülüyor"),
                Sentence("büyüdü , palazlandı , devleti ele geçirdi"),
                Sentence("her maskenin ciltte kalma süresi farklıdır"),
                Sentence("yılın son ayında 10 gazeteci gözaltına alındı"),
                Sentence("iki pilotun kullandığı uçakta bir hostes görev alıyor"),
                Sentence("son derece kısıtlı kelimeler çerçevesinde kendilerini uzun cümlelerle ifade edebiliyorlar"),
                Sentence("minibüs durağı"),
                Sentence("noter belgesi"),
                Sentence("bu filmi daha önce görmemiş miydik diye sordu")]
        modified = [Sentence("demokratik cumhüriyet en kımetli varlıgımızdır"),
                Sentence("bu tblodaki değerler zedelenmeyecektir"),
                Sentence("vakfın geeneksel yılin spoşcusu ankşti yeni yeşını doldürdu"),
                Sentence("demokrasinin icşdı bu ayrmıı bulandürdı"),
                Sentence("dışişleri mütseşarı Öymen'in 1997'nin iljk aylğrında Bağdat'a gitmesi öngörülüyor"),
                Sentence("büyüdü , palazandı , devltei ele geçridi"),
                Sentence("her makenin cültte aklma sürdsi farlkıdır"),
                Sentence("yılın son ayında 10 gazteci gözlatına alündı"),
                Sentence("iki piotun kulçandığı uçkata bir hotes görçv alyıor"),
                Sentence("son deece kısütlı keilmeler çeçevesinde kendülerini uzuü cümllerle ifüde edbeiliyorlar"),
                Sentence("minibü durağı"),
                Sentence("ntoer belgesi"),
                Sentence("bu filmi daha önce görmemişmiydik diye sordu")]
        fsm = FsmMorphologicalAnalyzer()
        nGram = NGram("../ngram.txt")
        nGram.calculateNGramProbabilitiesSimple(NoSmoothing())
        nGramSpellChecker = NGramSpellChecker(fsm, nGram, SpellCheckerParameter())
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
                Sentence("bu haksızlık da unutulup gitmişti"),
                Sentence("4'lü tahıl zirvesi İstanbul'da gerçekleşti"),
                Sentence("10'luk sistemden 100'lük sisteme geçiş yapılacak"),
                Sentence("play-off maçlarına çıkacak takımlar belli oldu"),
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
                Sentence("bu haksızlıkda unutulup gitmişti"),
                Sentence("4 lı tahıl zirvesi İstanbul'da gerçekleşti"),
                Sentence("10 lük sistemden 100 lık sisteme geçiş yapılacak"),
                Sentence("play - off maçlarına çıkacak takımlar belli oldu"),
                Sentence("bu son model ciha 24inç ekran büyüklüğünde ve 9kg ağırlıktadır")]
        fsm = FsmMorphologicalAnalyzer()
        nGram = NGram("../ngram.txt")
        nGram.calculateNGramProbabilitiesSimple(NoSmoothing())
        nGramSpellChecker = NGramSpellChecker(fsm, nGram, SpellCheckerParameter())
        for i in range(len(modified)):
            self.assertEqual(original[i].toString(), nGramSpellChecker.spellCheck(modified[i]).toString())

    def test_ForcedChecks(self):
        original = [Sentence("yardımcı olur musunuz ?"),
                Sentence("buraya daha önce gelmemiş miydik ?"),
                Sentence("kutunun boyutları 0.2 m x 0.3 m x 0.5 m olacak"),
                Sentence("2 tb depolama alanına sahip 7200 rpm bir disk"),
                Sentence("anahtarlarımı Kadıköy'de bir lokantada unutmuşum"),
                Sentence("bütün suç Selma'da değil"),
                Sentence("Fransa'nın başkenti Paris'tir"),
                Sentence("Nişantaşı'ndan Kadıköy'e gitmek için metroya binip Üsküdar'da inmek gerekiyor"),
                Sentence("90'lı yıllarda ülkede çok büyük değişimler oldu"),
                Sentence("100'lük parçaları bir araya getirerek 100'lük bir resim oluşturduk"),
                Sentence("size konuyla ilgili bir e-posta gönderdim"),
                Sentence("meyve-sebze reyonundan bir kilo elma aldım")]
        modified = [Sentence("yardımcı olurmusunuz ?"),
                Sentence("buraya daha önce gelmemişmiydik ?"),
                Sentence("kutunun boyutları 0.2m x 0.3m x 0.5m olacak"),
                Sentence("2tb depolama alanına sahip 7200rpm bir disk"),
                Sentence("anahtarlarımı Kadıköyda bir lokantada unutmuşum"),
                Sentence("bütün suç Selmada değil"),
                Sentence("Fransanın başkenti Paristir"),
                Sentence("Nişantaşından Kadıköye gitmek için metroya binip Üsküdarda inmek gerekiyor"),
                Sentence("90 lü yıllarda ülkede çok büyük değişimler oldu"),
                Sentence("100 lık parçaları bir araya getirerek 100 lük bir resim oluşturduk"),
                Sentence("size konuyla ilgili bir e - posta gönderdim"),
                Sentence("meyve — sebze reyonundan bir kilo elma aldım")]
        fsm = FsmMorphologicalAnalyzer()
        nGram = NGram("../ngram.txt")
        nGram.calculateNGramProbabilitiesSimple(NoSmoothing())
        nGramSpellChecker = NGramSpellChecker(fsm, nGram, SpellCheckerParameter())
        for i in range(len(modified)):
            self.assertEqual(original[i].toString(), nGramSpellChecker.spellCheck(modified[i]).toString())

    def test_SpellCheckSurfaceForm(self):
        fsm = FsmMorphologicalAnalyzer()
        nGram = NGram("../ngram.txt")
        nGram.calculateNGramProbabilitiesSimple(NoSmoothing())
        parameter = SpellCheckerParameter()
        parameter.setRootNGram(False)
        nGramSpellChecker = NGramSpellChecker(fsm, nGram, parameter)
        self.assertEqual("noter hakkında", nGramSpellChecker.spellCheck(Sentence("noter hakkınad")).__str__())
        self.assertEqual("arçelik'in çamaşır", nGramSpellChecker.spellCheck(Sentence("arçelik'in çamşaır")).__str__())
        self.assertEqual("ruhsat yanında", nGramSpellChecker.spellCheck(Sentence("ruhset yanında")).__str__())


if __name__ == '__main__':
    unittest.main()
