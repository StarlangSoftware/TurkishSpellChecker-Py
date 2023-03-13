import unittest

from Corpus.Sentence import Sentence
from MorphologicalAnalysis.FsmMorphologicalAnalyzer import FsmMorphologicalAnalyzer
from NGram.NGram import NGram
from NGram.NoSmoothing import NoSmoothing

from SpellChecker.SpellCheckerParameter import SpellCheckerParameter
from SpellChecker.TrieBasedSpellChecker import TrieBasedSpellChecker


class TrieBasedSpellCheckerTest(unittest.TestCase):

    def test_SpellCheck(self):
        original = [Sentence("antibiyotik direnci bir mikroorganizmanın antibiyotiklerin etkilerine karşı durabilme yeteneğidir"),
                Sentence("bugünkü ortaöğretim sisteminin oluşumu Cumhuriyet döneminde gerçekleşmiştir"),
                Sentence("bilinçsizce dağıtılan kredilerin sorun yaratmayacağını düşünmelerinin nedeni bankaların büyüklüğünden kaynaklanıyordu"),
                Sentence("Yemen'de ekonomik durgunluk nedeniyle yeni bir insani kriz yaşanabileceği uyarısı yapıldı"),
                Sentence("hafif ticari araç bariyerlere çarptı"),
                Sentence("sırtıkara adındaki canlı , bir balıktır"),
                Sentence("siyah ayı , ayıgiller familyasına ait bir ayı türüdür"),
                Sentence("alışveriş için markete gitti"),
                Sentence("küçük bir yalıçapkını geçti"),
                Sentence("yeni yılın sonrasında vakalarda artış oldu"),
                Sentence("atomik saatin 10 mhz sinyali kalibrasyon hizmetlerinde referans olarak kullanılmaktadır"),
                Sentence("rehberimiz bu bölgedeki çıngıraklı yılan varlığı hakkında konuştu"),
                Sentence("bu haksızlık da unutulup gitmişti"),
                Sentence("4'lü tahıl zirvesi İstanbul'da gerçekleşti"),
                Sentence("10'luk sistemden 100'lük sisteme geçiş yapılacak"),
                Sentence("play-off maçlarına çıkacak takımlar belli oldu"),
                Sentence("bu son model cihaz 24 inç ekran büyüklüğünde ve 9 kg ağırlıktadır")]
        modified = [Sentence("antibiodik direnci bir mikrorkanismanın antibiyotiklerin etkilerine karşı durabilme yeteneğidir"),
                Sentence("bugünki ortögretim sisteminin oluşumu Cumhuriyet dönmeinde gerçekleşmiştir"),
                Sentence("billinçiszce dağıtılan kredilerin sorun yaratmayacağını düşünmelerinin nedeni bankaların büyüklüğünden kaynaklanıyordu"),
                Sentence("Yemen'de ekonomik durrğunlk nedeniyle yeni bir insani kriz yaşanabileceği uyaarisi yapıldı"),
                Sentence("hafif ricarii araç aryerlere çarptı"),
                Sentence("sırtı kara adındaki canlı , bir balıktır"),
                Sentence("siyahayı , ayıgiller familyasına ait bir ayı türüdür"),
                Sentence("alis veriş için markete gitit"),
                Sentence("kucuk bri yalı çapkını gecti"),
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
        trieBasedSpellChecker = TrieBasedSpellChecker(fsm, nGram, SpellCheckerParameter())
        for i in range(len(modified)):
            self.assertEqual(original[i].toString(), trieBasedSpellChecker.spellCheck(modified[i]).toString())


if __name__ == '__main__':
    unittest.main()
