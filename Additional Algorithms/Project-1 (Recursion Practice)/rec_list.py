from __future__ import annotations
from typing import Optional, Any, Tuple

# NodeList is
# None or
# Node(value, rest), where rest is the rest of the NodeList


class Node:
    def __init__(self, value: Any, rest: Optional[Node]):
        self.value = value
        self.rest = rest

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Node):
            return (self.value == other.value
                    and self.rest == other.rest
                    )
        else:
            return False

    def __repr__(self) -> str:
        return ("Node({!r}, {!r})".format(self.value, self.rest))

# a StrList is one of
# - None, or
# - Node(string, StrList)

# StrList -> string
# Returns first (as determined by Python compare) string in StrList
# If StrList is empty (None), return None
# Must be implemented recursively


def first_string(strlist: Optional[Node]) -> Optional[str]:

    if strlist is None:
        return None

    first = first_string(strlist.rest)

    if first is None or strlist.value < first:
        return strlist.value

    return first
# StrList -> (StrList, StrList, StrList)
# Returns a tuple with 3 new StrLists,
# the first one with strings from the input list that start with a vowel,
# the second with strings from the input list that start with a consonant,
# the third with strings that don't start with an alpha character
# Must be implemented recursively


def split_list(strlist: Optional[Node]) -> Tuple[Optional[Node], Optional[Node], Optional[Node]]:

    if strlist is not None:
        # lists recursion (used to compare each value in each Node)
        lists = split_list(strlist.rest)

        # vowel checking
        vowel = 'aeiou'

        # return value in first index of tuple to be vowel
        if strlist.value[0].isalpha() and strlist.value[0].lower() in vowel:
            return (Node(strlist.value, lists[0]), lists[1], lists[2])

        # return value in second index of tuple to be consonant
        elif strlist.value[0].isalpha():
            return (lists[0], Node(strlist.value, lists[1]), lists[2])

        # return value in third index of tuple to be non-alpha
        elif not strlist.value[0].isalpha():
            return (lists[0], lists[1], Node(strlist.value, lists[2]))

    return (None, None, None)
