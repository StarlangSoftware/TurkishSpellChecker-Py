# SpellChecker

Yazım denetleyici, verilen metindeki yazım hatalarını bulup düzelten Nlptoolkit bilşenidir. Her kelime için hatayı tespit edip olası doğru adaylar arasından seçim yapar. Bu bileşen iki farklı yazım denetleyici içermektedir. Bunlar basit yazım denetleyici (simple spell checker) ve n-karakter yazım denetleyicidir (ngram spell checker).

Basit yazım denetleyici, basit geri dönüştürücü ile benzer bir yöntem kullanır. Girdideki her kelime için her karakter gezilip bu karakter olası bütün karakterlerle değiştirilerek mümkün olabilecek bütün kelimeler oluşturulur ve bunlardan biçimbilimsel olarak çözümlemenebilenlerden bir tanesi rassal olarak seçilir.

N-karakter yazım denetleyici, benzer şekilde n-karakter geri dönüştürücü ile aynı mantığı kullanmaktadır. Önce, basit yazım denetleyicide olduğu gibi kelimeler için aday listeleri hazırlanır. Daha sonra ise n-karakter modelinden bu adaylar için olasılıklar hesaplanarak, her kelime için olasılığı en yüksek olan aday çıktı olarak verilir.
