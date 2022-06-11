import unittest
from bears import *

# Starter test cases - write more!

class TestAssign1(unittest.TestCase):
    def test_bear_01(self) -> None:
        self.assertTrue(bears(250))

    def test_bear_02(self) -> None:
        self.assertTrue(bears(42))

    def test_bear_03(self) -> None:
        self.assertFalse(bears(53))

    def test_bear_04(self) -> None:
        self.assertFalse(bears(41))

if __name__ == "__main__":
    unittest.main()
