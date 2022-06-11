import unittest
from sorts import *

class TestLab6(unittest.TestCase):

    def test_01_selection(self):
        nums = [23, 10, 49, 12]
        comps = selection_sort(nums)
        self.assertEqual(comps, 6)
        self.assertEqual(nums, [10, 12, 23, 49])

    def test_02_insertion(self):
        nums = [23, 10, 49, 31]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 4)
        self.assertEqual(nums, [10, 23, 31, 49])

    def test_03_selection_sort_sorts(self):
        sizes = [250, 500, 1000, 1500]
        for n in sizes:
            randoms = random.sample(range(1000000), n)
            expected = list(randoms)
            expected.sort()
            selection_sort(randoms)
            self.assertEqual(randoms, expected)

    def test_04_insertion_sort_sorts(self):
        sizes = [250, 500, 1000, 1500]
        for n in sizes:
            randoms = random.sample(range(1000000), n)
            expected = list(randoms)
            expected.sort()
            insertion_sort(randoms)
            self.assertEqual(randoms, expected)

    def test_05_selection_sort_number_of_comps(self):
        n = 100
        randoms = random.sample(range(1000000), n)
        comps = selection_sort(randoms)
        self.assertEqual(comps, 4950)

    def test_06_insertion_sort_number_of_comps(self):
        nums = []
        for i in range(50):
            nums.append(i*2)
            nums.append((50-i)*2-1)
        comps = insertion_sort(nums)
        self.assertEqual(comps, 2574)
        comps = insertion_sort(nums)
        self.assertEqual(comps, 99)
        nums.sort(reverse=True)
        comps = insertion_sort(nums)
        self.assertEqual(comps, 4950)

if __name__ == '__main__':
    unittest.main()
