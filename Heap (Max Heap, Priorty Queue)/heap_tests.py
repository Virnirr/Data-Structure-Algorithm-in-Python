import unittest
from heap import *

'''
Consider...
tests for negative integers
tests for strings, other comparable
'''
class TestHeap(unittest.TestCase):

    def test_enqueue_dequeue(self) -> None:  # test not done
        a = MinHeap()
        a.enqueue(12)
        a.enqueue(72)
        a.enqueue(22)
        a.enqueue(30)
        a.enqueue(25)
        a.enqueue(47)
        a.enqueue(53)
        a.enqueue(52)
        a.enqueue(123)
        a.enqueue(1)
        a.enqueue(1)
        a.enqueue(1)
        a.enqueue(1)
        self.assertEqual(a.contents(), [1, 1, 1, 52, 12, 1, 53, 72, 123, 30, 25, 47, 22])
        self.assertEqual(a.peek(), 1)
        self.assertEqual(a.dequeue(), 1)

    def test_empty_contents(self) -> None:
        test_heap = MinHeap(10)
        self.assertEqual(test_heap.contents(), [])

    def test_01_peek_and_dequeue_1_item(self) -> None:
        test_heap = MinHeap(10)
        test_heap.enqueue(25)
        self.assertEqual(test_heap.peek(), 25)
        self.assertEqual(test_heap.dequeue(), 25)

    def test_02_dequeue_2_item(self) -> None:
        test_heap = MinHeap(10)
        test_heap.enqueue(25)
        test_heap.enqueue(5)
        self.assertEqual(test_heap.dequeue(), 5)
        self.assertEqual(test_heap.dequeue(), 25)
        test_heap = MinHeap(10)
        test_heap.enqueue(5)
        test_heap.enqueue(25)
        self.assertEqual(test_heap.dequeue(), 5)
        self.assertEqual(test_heap.dequeue(), 25)

    def test_04_enqueue2(self) -> None:
        test_heap = MinHeap(6)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        with self.assertRaises(IndexError):
            test_heap.enqueue(10)

    def test_06_find_min1(self) -> None:
        test_heap = MinHeap()
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        test_heap.enqueue(10)
        self.assertEqual(test_heap.dequeue(), 2)
        self.assertEqual(test_heap.dequeue(), 5)

    def test_07_find_min3(self) -> None:
        test_heap = MinHeap()
        with self.assertRaises(IndexError):
            test_heap.dequeue()
        self.assertEqual(test_heap.size(),0)
        with self.assertRaises(IndexError):
            test_heap.peek()

    def test_08_del_min1(self) -> None:
        test_heap = MinHeap()
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.dequeue(), 2)
        self.assertEqual(test_heap.size(), 5)
        self.assertEqual(test_heap.contents(), [5, 6, 7, 8, 9])

    def test_10_heap_contents1(self) -> None:
        test_heap = MinHeap(8)
        test_heap.build_heap([3, 2, 1])
        self.assertEqual(test_heap.contents(), [1, 2, 3])

    def test_12_build_heap1(self) -> None:
        test_heap = MinHeap(8)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.contents(), [2, 5, 7, 6, 9, 8])

    def test_14_build_heap3(self) -> None:
        test_heap = MinHeap(1)
        test_heap.build_heap([3, 4, 5, 6, 7, 10, 8, 1, 2])
        self.assertEqual(test_heap.contents(), [1, 2, 5, 3, 7, 10, 8, 6, 4])

    def test_15_is_empty1(self) -> None:
        test_heap = MinHeap(5)
        self.assertTrue(test_heap.is_empty())
        test_heap.enqueue(10)
        self.assertFalse(test_heap.is_empty())
        test_heap.dequeue()
        self.assertTrue(test_heap.is_empty())        

    def test_16_is_full1(self) -> None:
        test_heap = MinHeap(5)
        test_heap.build_heap([1, 2, 3, 4, 5])
        self.assertTrue(test_heap.is_full())
        test_heap.dequeue()
        self.assertFalse(test_heap.is_full())
        test_heap.enqueue(10)
        self.assertTrue(test_heap.is_full())

    def test_17_get_heap_cap1(self) -> None:
        test_heap = MinHeap(7)
        self.assertEqual(test_heap.capacity(), 7)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.capacity(), 7)
        test_heap.enqueue(10)
        self.assertEqual(test_heap.capacity(), 7)
        test_heap = MinHeap()
        self.assertEqual(test_heap.capacity(), 50)

    def test_18_get_heap_size1(self) -> None:
        test_heap = MinHeap()
        self.assertEqual(test_heap.size(), 0)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.size(), 6)
        test_heap.enqueue(10)
        self.assertEqual(test_heap.size(), 7)

    def test_20_heap_sort_increase1(self) -> None:
        test_heap = MinHeap()
        list1 = [2, 9, 7, 6, 5, 8]
        test_heap.heap_sort_ascending(list1)
        self.assertEqual(list1, [2, 5, 6, 7, 8, 9])

    def test_heap_sort_yuuge(self) -> None:
        test_heap = MinHeap(1)
        my_list = [20, 10, 30, 50, 40, 100, 90,
                   60, 80, 70, 110, 120, 130, 140, 150, 5, 4, 3, 2, 1]
        test_heap.heap_sort_ascending(my_list)

        self.assertEqual(
            my_list, [1, 2, 3, 4, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150])
        
        self.assertEqual(test_heap.capacity(), 20)

    def test_heap_sort_yuuge2(self) -> None:
        test_heap = MinHeap(1)
        my_list = [20, 10, 30, 50, 40, 100, 90,
                   60, 80, 70, 110, 120, 130, 140, 150, 5, 4, 3, -2, -1]
        test_heap.heap_sort_ascending(my_list)

        self.assertEqual(
            my_list, [-2, -1, 3, 4, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150])

if __name__ == "__main__":
    unittest.main()
