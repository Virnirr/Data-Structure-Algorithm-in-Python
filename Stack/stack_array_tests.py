import unittest
from stack_array import Stack
        
class TestLab2(unittest.TestCase):

    def test_init(self) -> None:
        stack = Stack(5)
        self.assertEqual(stack.items, [None]*5)
        self.assertEqual(stack.capacity, 5)

        stack = Stack(5, [1, 2])
        self.assertEqual(stack.items[0:2], [1, 2])
        self.assertEqual(stack.capacity, 5)

        with self.assertRaises(IndexError):
            Stack(5, [1, 2, 3, 4, 5, 6])

    def test_eq(self) -> None:
        stack1 = Stack(5)
        stack2 = Stack(5)
        stack3 = Stack(10)
        stack4 = Stack(5,[1, 2])
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack3)
        self.assertNotEqual(stack1, stack4)
        self.assertFalse(stack1.__eq__(None))

    def test_repr(self) -> None:
        stack = Stack(5, [1, 2])
        self.assertEqual(stack.__repr__(), "Stack(5, [1, 2])")
    
    def test_is_empty(self) -> None:
        stack = Stack(5, [])
        stack2 = Stack(5, [1,2])
        self.assertEqual(stack.is_empty(), True)
        self.assertFalse(stack2.is_empty(), False)

    def test_is_full(self) -> None:
        stack = Stack(5, [1,2,3,4,5])
        stack2 = Stack(5, [1,2,3])
        self.assertEqual(stack.is_full(), True)
        self.assertEqual(stack2.is_full(), False)

    def test_push(self) -> None:
        stack = Stack(5, [1,2,3])
        stack2 = Stack(5, [1,2,3,4,5])
        stack.push(4)
        stack.push(5)
        self.assertEqual(stack.items, stack2.items)
        with self.assertRaises(IndexError):
            stack3 = Stack(5, [6,7,8,9,10])
            stack3.push(11)

    def test_pop(self) -> None:
        stack = Stack(5, [1,2,3,4,5])
        self.assertEqual(stack.pop(), 5)
        with self.assertRaises(IndexError):
            stack3 = Stack(5, [])
            stack3.pop()

    def test_peek(self) -> None:
        stack = Stack(5, [1,2,3,4,5])
        self.assertEqual(stack.peek(), 5)
        with self.assertRaises(IndexError):
            stack2 = Stack(5, [])
            stack2.peek()

    def test_size(self) -> None:
        stack1 = Stack(5, [1,2,3,4])
        stack2 = Stack(5, [])
        self.assertEqual(stack1.size(), 4)
        self.assertEqual(stack2.size(), 0)




# WRITE TESTS FOR STACK OPERATIONS - PUSH, POP, PEEK, etc.

if __name__ == '__main__': 
    unittest.main()
