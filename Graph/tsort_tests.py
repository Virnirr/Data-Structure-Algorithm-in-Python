import unittest
from tsort import *

class TestTsort(unittest.TestCase):
        
    def test_01(self) -> None:
        input = ['101', '102', '102', '103', '103', '315', '225', '315', '103', '357', '315', '357', '141', '102', '102', '225']
        expect = "141\n101\n102\n225\n103\n315\n357"
        actual:str = tsort(input)
        self.assertEqual(actual.strip(), expect)

    def test_02(self) -> None:
        input = ['blue', 'black', 'red', 'blue', 'red', 'green', 'green', 'blue', 'green', 'purple', 'purple', 'blue']
        expect = "red\ngreen\npurple\nblue\nblack"
        actual:str = tsort(input)
        self.assertEqual(actual.strip(), expect)

    def test_03(self) -> None:
        input = ['1', '2', '1', '9', '1', '8', '9', '8', '9', '10', '8', '11', '10', '11', '2', '3', '3', '11', '3', '4', '4', '7', '4', '5', '7', '5', '7', '13', '7', '6', '6', '14', '6', '12']
        expect = "1\n9\n10\n8\n2\n3\n4\n7\n6\n12\n14\n13\n5\n11"
        actual:str = tsort(input)
        self.assertEqual(actual.strip(), expect)

    def test_04(self) -> None:
        input = ['3', '8', '3', '10', '5', '11', '7', '8', '7', '11', '8', '9', '11', '2', '11', '9', '11', '10']
        expect = "7\n5\n11\n2\n3\n10\n8\n9"
        actual:str = tsort(input)
        self.assertEqual(actual.strip(), expect)

    def test_05(self) -> None:
        input = ['102', '225', '141', '102', '315', '357', '103', '357', '225', '315', '103', '315', '102', '103', '101', '102']
        expect = "101\n141\n102\n103\n225\n315\n357"
        actual:str = tsort(input)
        self.assertEqual(actual.strip(), expect)

    def test_06(self) -> None:
        input = 'v1 v2 v1 v3 v1 v4 v2 v4 v2 v5 v3 v6 v4 v3 v4 v6 v4 v7 v5 v4 v5 v7 v7 v6'
        input_list = input.split()
        expect = 'v1 v2 v5 v4 v7 v3 v6'
        expect = '\n'.join(expect.split())
        actual:str = tsort(input_list)
        self.assertEqual(actual.strip(), expect)

    def test_07(self) -> None:
        input = 'v1 v2 v3 v4 v5 v6 v7 v8 v9 v10'
        input_list = input.split()
        expect = 'v9 v10 v7 v8 v5 v6 v3 v4 v1 v2'
        expect = '\n'.join(expect.split())
        actual:str = tsort(input_list)
        self.assertEqual(actual.strip(), expect)

    def test_08(self) -> None:
        input = '1 2 1 3 2 3 8 2 2 4 4 7 5 4 5 7 6 7 2 7 3 5 1 5 2 6'
        input_list = input.split()
        expect = '8 1 2 6 3 5 4 7'
        expect = '\n'.join(expect.split())
        actual:str = tsort(input_list)
        self.assertEqual(actual.strip(), expect)

    def test_09(self) -> None:
        input = '4 7 5 4 5 7 6 7 2 7 3 5 1 5 2 6 1 2 1 3 2 3 8 2 2 4'
        input_list = input.split()
        expect = '8 1 2 3 5 4 6 7'
        expect = '\n'.join(expect.split())
        actual:str = tsort(input_list)
        self.assertEqual(actual.strip(), expect)

    def test_10(self) -> None:
        input: List[str] = []
        try:
            actual:str = tsort(input)
            self.fail()         # pragma: no cover
        except ValueError as e:
            self.assertEqual(str(e), "input contains no edges")

    def test_11(self) -> None:
        input = ['a', 'b', 'c', 'd', 'e']
        try:
            actual:str = tsort(input)
            self.fail()         # pragma: no cover
        except ValueError as e:
            self.assertEqual(str(e), "input contains an odd number of tokens")

    def test_12(self) -> None:
        input = 'a b b c c d c b'
        input_list = input.split()
        try:
            actual:str = tsort(input_list)
            self.fail()         # pragma: no cover
        except ValueError as e:
            self.assertEqual(str(e), "input contains a cycle")

    def test_13(self) -> None:
        input = 'a b b a'
        input_list = input.split()
        try:
            actual:str = tsort(input_list)
            self.fail()         # pragma: no cover
        except ValueError as e:
            self.assertEqual(str(e), "input contains a cycle")

if __name__ == "__main__":
    unittest.main()
