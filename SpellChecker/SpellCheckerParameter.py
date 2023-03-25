class SpellCheckerParameter:

    __threshold: float
    __deMiCheck: bool
    __rootNGram: bool
    __minWordLength: int
    __domain: str

    def __init__(self):
        """
        Constructs a SpellCheckerParameter object with default values.
        The default threshold is 0.0, the De-Mi check is enabled, the root ngram is enabled and
        the minimum word length is 4.
        """
        self.__threshold = 0.0
        self.__deMiCheck = True
        self.__rootNGram = True
        self.__minWordLength = 4
        self.__domain = ""

    def setThreshold(self, threshold: float):
        """
        Sets the threshold value used in calculating the n-gram probabilities.
        :param threshold: the threshold for the spell checker
        """
        self.__threshold = threshold

    def setDeMiCheck(self, deMiCheck: bool):
        """
        Enables or disables De-Mi check for the spell checker.
        :param deMiCheck: a boolean indicating whether the De-Mi check should be enabled (true) or disabled (false)
        """
        self.__deMiCheck = deMiCheck

    def setRootNGram(self, rootNGram: bool):
        """
        Enables or disables the root n-gram for the spell checker.
        :param rootNGram: a boolean indicating whether the root n-gram should be enabled (true) or disabled (false)
        """
        self.__rootNGram = rootNGram

    def setMinWordLength(self, minWordLength: int):
        """
        Sets the minimum length of words viable for spell checking.
        :param minWordLength: the minimum word length for the spell checker
        """
        self.__minWordLength = minWordLength

    def setDomain(self, domain: str):
        """
        Sets the _domain name to the specified value.
        :param domain: the new domain name to set for this object
        """
        self.__domain = domain

    def getThreshold(self) -> float:
        """
        Returns the threshold value used in calculating the n-gram probabilities.
        :return: the threshold for the spell checker
        """
        return self.__threshold

    def isDeMiCheck(self) -> bool:
        """
        Returns whether De-Mi check is enabled for the spell checker.
        :return: a boolean indicating whether De-Mi check is enabled for the spell checker
        """
        return self.__deMiCheck

    def isRootNGram(self) -> bool:
        """
        Returns whether the root n-gram is enabled for the spell checker.
        :return: a boolean indicating whether the root n-gram is enabled for the spell checker
        """
        return self.__rootNGram

    def getMinWordLength(self) -> int:
        """
        Returns the minimum length of words viable for spell checking.
        :return: the minimum word length for the spell checker
        """
        return self.__minWordLength

    def getDomain(self) -> str:
        """
        Returns the domain name
        :return: the domain name
        """
        return self.__domain
