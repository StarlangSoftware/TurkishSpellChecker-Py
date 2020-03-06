# SpellChecker

Yazım denetleyici, verilen metindeki yazım hatalarını bulup düzelten Nlptoolkit bilşenidir. Her kelime için hatayı tespit edip olası doğru adaylar arasından seçim yapar. Bu bileşen iki farklı yazım denetleyici içermektedir. Bunlar basit yazım denetleyici (simple spell checker) ve n-karakter yazım denetleyicidir (ngram spell checker).

Basit yazım denetleyici, basit geri dönüştürücü ile benzer bir yöntem kullanır. Girdideki her kelime için her karakter gezilip bu karakter olası bütün karakterlerle değiştirilerek mümkün olabilecek bütün kelimeler oluşturulur ve bunlardan biçimbilimsel olarak çözümlemenebilenlerden bir tanesi rassal olarak seçilir.

N-karakter yazım denetleyici, benzer şekilde n-karakter geri dönüştürücü ile aynı mantığı kullanmaktadır. Önce, basit yazım denetleyicide olduğu gibi kelimeler için aday listeleri hazırlanır. Daha sonra ise n-karakter modelinden bu adaylar için olasılıklar hesaplanarak, her kelime için olasılığı en yüksek olan aday çıktı olarak verilir.

For Developers
============
You can also see either [Java](https://github.com/olcaytaner/TurkishSpellChecker) 
or [C++](https://github.com/olcaytaner/TurkishSpellChecker-CPP) repository.
## Requirements

* [Python 3.7 or higher](#python)
* [Git](#git)

### Python 

To check if you have a compatible version of Python installed, use the following command:

    python -V
    
You can find the latest version of Python [here](https://www.python.org/downloads/).

### Git

Install the [latest version of Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Download Code

In order to work on code, create a fork from GitHub page. 
Use Git for cloning the code to your local or below line for Ubuntu:

	git clone <your-fork-git-link>

A directory called SpellChecker will be created. Or you can use below link for exploring the code:

	git clone https://github.com/olcaytaner/TurkishSpellChecker-Py.git

## Open project with Pycharm IDE

Steps for opening the cloned project:

* Start IDE
* Select **File | Open** from main menu
* Choose `DataStructure-PY` file
* Select open as project option
* Couple of seconds, dependencies will be downloaded. 


## Compile

**From IDE**

After being done with the downloading and Maven indexing, select **Build Project** option from **Build** menu. After compilation process, user can run DataStructure.
