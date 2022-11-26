class SpellCheckerParameter:

    __threshold: float
    __deMiCheck: bool
    __rootNGram: bool

    def __init__(self):
        self.__threshold = 0.0
        self.__deMiCheck = True
        self.__rootNGram = True

    def setThreshold(self, threshold: float):
        self.__threshold = threshold

    def setDeMiCheck(self, deMiCheck: bool):
        self.__deMiCheck = deMiCheck

    def setRootNGram(self, rootNGram: bool):
        self.__rootNGram = rootNGram

    def getThreshold(self) -> float:
        return self.__threshold

    def isDeMiCheck(self) -> bool:
        return self.__deMiCheck

    def isRootNGram(self) -> bool:
        return self.__rootNGram
