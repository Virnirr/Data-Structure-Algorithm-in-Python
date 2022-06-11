import unittest
from  rec_list import *

# Starter test cases - write more!!

class TestRecList(unittest.TestCase):

    def test_equal(self) -> None:
        strlist = Node("xyz", Node("Abc", Node("49ers", None)))
        strlist2 = ""
        self.assertEqual(strlist == strlist2, False)

    def test_repr(self) -> None:
        strlist = Node("xyz", Node("Abc", Node("49ers", None)))
        self.assertEqual(repr(strlist), "Node('xyz', Node('Abc', Node('49ers', None)))")

    def test_first1(self) -> None:
        strlist = Node("xyz", Node("Abc", Node("49ers", None)))
        self.assertEqual(first_string(strlist),"49ers")

    def test_split1(self) -> None:
        strlist = Node("xyz", Node("Abc", Node("49ers", None)))
        self.assertEqual(split_list(strlist),(Node('Abc', None), Node('xyz', None), Node('49ers', None)))

    def test_split2(self) -> None:
        strlist = Node("Yellow", Node("abc", Node("$7.25", Node("lime", Node("42", Node("Ethan", None))))))
        self.assertEqual(split_list(strlist),(Node('abc', Node("Ethan", None)), Node('Yellow', Node("lime", None)), Node('$7.25', Node("42", None))))

    def test_split3(self) -> None:
        strlist = None
        self.assertEqual(split_list(strlist), (None, None, None))

if __name__ == "__main__":
        unittest.main()