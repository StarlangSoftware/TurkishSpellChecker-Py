Turkish Spell Checker
============

This tool is a spelling checker for Modern Turkish. It detects spelling errors and corrects them appropriately, through its list of misspellings and matching to the Turkish dictionary.

Video Lectures
============

[<img src="https://github.com/StarlangSoftware/TurkishSpellChecker/blob/master/video.jpg" width="50%">](https://youtu.be/wKwTKv6Jlo0)

For Developers
============

You can also see [Cython](https://github.com/starlangsoftware/TurkishSpellChecker-Cy), [Java](https://github.com/starlangsoftware/TurkishSpellChecker), [C++](https://github.com/starlangsoftware/TurkishSpellChecker-CPP), [Swift](https://github.com/starlangsoftware/TurkishSpellChecker-Swift), [Js](https://github.com/starlangsoftware/TurkishSpellChecker-Js), or [C#](https://github.com/starlangsoftware/TurkishSpellChecker-CS) repository.

## Requirements

* [Python 3.7 or higher](#python)
* [Git](#git)

### Python 

To check if you have a compatible version of Python installed, use the following command:

    python -V
    
You can find the latest version of Python [here](https://www.python.org/downloads/).

### Git

Install the [latest version of Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Pip Install

	pip3 install NlpToolkit-SpellChecker

## Download Code

In order to work on code, create a fork from GitHub page. 
Use Git for cloning the code to your local or below line for Ubuntu:

	git clone <your-fork-git-link>

A directory called SpellChecker will be created. Or you can use below link for exploring the code:

	git clone https://github.com/starlangsoftware/TurkishSpellChecker-Py.git

## Open project with Pycharm IDE

Steps for opening the cloned project:

* Start IDE
* Select **File | Open** from main menu
* Choose `DataStructure-PY` file
* Select open as project option
* Couple of seconds, project will be downloaded. 

Detailed Description
============

+ [Creating SpellChecker](#creating-spellchecker)
+ [Spell Correction](#spell-correction)

## Creating SpellChecker

SpellChecker finds spelling errors and corrects them in Turkish. There are two types of spell checker available:

* `SimpleSpellChecker`
    
    * To instantiate this, a `FsmMorphologicalAnalyzer` is needed. 
        
            fsm = FsmMorphologicalAnalyzer()
            spellChecker = SimpleSpellChecker(fsm)   
     
* `NGramSpellChecker`,
    
    * To create an instance of this, both a `FsmMorphologicalAnalyzer` and a `NGram` is required. 
    
    * `FsmMorphologicalAnalyzer` can be instantiated as follows:
        
            fsm = FsmMorphologicalAnalyzer()
    
    * `NGram` can be either trained from scratch or loaded from an existing model.
        
        * Training from scratch:
                
                corpus = Corpus("corpus.txt");
                ngram = NGram(corpus.getAllWordsAsArrayList(), 1)
                ngram.calculateNGramProbabilities(LaplaceSmoothing())
                
        *There are many smoothing methods available. For other smoothing methods, check [here](https://github.com/olcaytaner/NGram).*       
        * Loading from an existing model:
     
                ngram = NGram("ngram.txt")

	*For further details, please check [here](https://github.com/starlangsoftware/NGram).*        
            
    * Afterwards, `NGramSpellChecker` can be created as below:
        
            spellChecker = NGramSpellChecker(fsm, ngram)
     

## Spell Correction

Spell correction can be done as follows:

    sentence = Sentence("Dıktor olaç yazdı")
    corrected = spellChecker.spellCheck(sentence)
    print(corrected)
    
Output:

    Doktor ilaç yazdı
