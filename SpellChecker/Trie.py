from SpellChecker.TrieNode import TrieNode


class Trie:

    __root_node: TrieNode

    def __init__(self):
        """
        A constructor of {@link Trie} class which constructs a new Trie with an empty root node
        """
        self.__root_node = TrieNode()

    def insert(self, word: str):
        """
        Inserts a new word into the Trie
        :param word: The word to be inserted
        """
        current_node = self.__root_node
        for i in range(len(word)):
            ch = word[i]
            if current_node.getChild(ch) is None:
                current_node.addChild(ch, TrieNode())
            current_node = current_node.getChild(ch)
        current_node.setIsWord(True)

    def search(self, word: str) -> bool:
        """
        Checks if a word is in the Trie
        :param word: The word to be searched for
        :return: true if the word is in the Trie, false otherwise
        """
        node = self.getTrieNode(word.lower())
        if node is None:
            return False
        else:
            return node.isWord()

    def startsWith(self, prefix: str) -> bool:
        """
        Checks if a given prefix exists in the Trie
        :param prefix: The prefix to be searched for
        :return: true if the prefix exists, false otherwise
        """
        if self.getTrieNode(prefix.lower()) is None:
            return False
        else:
            return True

    def getTrieNode(self, word: str) -> TrieNode:
        """
        Returns the TrieNode corresponding to the last character of a given word
        :param word: The word to be searched for
        :return: The TrieNode corresponding to the last character of the word
        """
        current_node = self.__root_node
        for i in range(len(word)):
            ch = word[i]
            if current_node.getChild(ch) is None:
                return None
            current_node = current_node.getChild(ch)
        return current_node
