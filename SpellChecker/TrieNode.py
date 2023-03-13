from __future__ import annotations


class TrieNode:
    __children: dict
    __isWord: bool

    def __init__(self):
        """
        A constructor of {@link TrieNode} class which constructs a new TrieNode with an empty children HashMap
        """
        self.__children = {}
        self.__isWord = False

    def getChild(self, ch: str) -> TrieNode:
        """
        Returns the child TrieNode with the given character as its value.
        :param ch: The character value of the child TrieNode.
        :return: TrieNode with the given character value.
        """
        return self.__children.get(ch)

    def addChild(self, ch: str, child: TrieNode):
        self.__children[ch] = child

    def childrenToString(self) -> str:
        result = ""
        for ch in self.__children:
            result = result + ch
        return result

    def isWord(self) -> bool:
        """
        Returns whether the current TrieNode represents the end of a word.
        :return: true if the current TrieNode represents the end of a word, false otherwise.
        """
        return self.__isWord

    def setIsWord(self, isWord: bool):
        """
        Sets whether the current TrieNode represents the end of a word.
        :param isWord: true if the current TrieNode represents the end of a word, false otherwise.
        """
        self.__isWord = isWord
