from enum import Enum, auto


class Operator(Enum):

    NO_CHANGE = auto()
    MISSPELLED_REPLACE = auto()
    FORCED_MERGE = auto()
    FORCED_SPLIT = auto()
    SPLIT_WITH_SHORTCUT = auto()
    SPELL_CHECK = auto()
    SPLIT = auto()
    FORWARD_MERGE = auto()
    BACKWARD_MERGE = auto()
