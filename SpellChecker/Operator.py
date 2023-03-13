from enum import Enum, auto


class Operator(Enum):

    NO_CHANGE = auto()
    MISSPELLED_REPLACE = auto()
    SPELL_CHECK = auto()
    SPLIT = auto()
    FORWARD_MERGE = auto()
    BACKWARD_MERGE = auto()
    CONTEXT_BASED = auto()
    TRIE_BASED = auto()
