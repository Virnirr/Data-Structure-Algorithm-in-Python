import unittest
from stack_nodelist import *
        
class TestLab2(unittest.TestCase):

    def test_node_init(self) -> None:
        node1 = Node(1, None)
        self.assertEqual(node1.value, 1)
        self.assertEqual(node1.rest, None)

        node2 = Node(2, node1)
        self.assertEqual(node2.value, 2)
        self.assertEqual(node2.rest, node1)

    def test_node_eq(self) -> None:
        node1a = Node(1, None)
        node1b = Node(1, None)
        node2a = Node(2, node1a)
        node2b = Node(2, node1b)

        self.assertEqual(node1a, node1b)
        self.assertNotEqual(node1a, node2a)
        self.assertEqual(node2a, node2b)
        node1a = Node(3, None)
        self.assertNotEqual(node1a, node1b)

        self.assertFalse(node1a.__eq__(None))

    def test_node_repr(self) -> None:
        node = Node(2, Node(1, None))
        self.assertEqual(node.__repr__(), "Node(2, Node(1, None))")

    def test_stack_init(self) -> None:
        stack = Stack()
        self.assertEqual(stack.top, None)

        init_stack = Node(2, Node(1, None))
        stack = Stack(init_stack)
        self.assertEqual(stack.top, init_stack)

    def test_stack_eq(self) -> None:
        stack1 = Stack()
        stack2 = Stack()
        init_stack = Node(2, Node(1, None))
        stack4 = Stack(init_stack)
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack4)
        self.assertFalse(stack1.__eq__(None))

    def test_stack_repr(self) -> None:
        init_stack = Node(2, Node(1, None))
        stack = Stack(init_stack)
        self.assertEqual(stack.__repr__(), "Stack(Node(2, Node(1, None)))")

    def test_is_empty(self) -> None:
        stack = Stack()
        stack1 = Stack(Node(2, None))
        self.assertEqual(stack.is_empty(), True)
        self.assertEqual(stack1.is_empty(), False)

    def test_push(self) -> None:
        stack1 = Stack(Node(0, Node(1, None)))
        stack1.push(2)
        stack2 = Stack(Node(2, Node(0, Node(1, None))))
        self.assertEqual(stack1, stack2)
        self.assertEqual(stack1.size(), 3)

    def test_pop(self) -> None:
        stack1 = Stack(Node(1, Node(2, Node(3, None))))
        self.assertEqual(stack1.pop(), 1)
        self.assertEqual(stack1, Stack(Node(2, Node(3, None))))
        self.assertEqual(stack1.size(), 2)
        with self.assertRaises(IndexError):
            stack3 = Stack()
            stack3.pop()

    def test_peek(self) -> None:
        stack1 = Stack(Node(1, Node(2, Node(3, None))))
        self.assertEqual(stack1.peek(), 1)
        with self.assertRaises(IndexError):
            stack2 = Stack()
            stack2.peek()

    def test_size(self) -> None:
        stack = Stack(Node(1, Node(2, Node(3, Node(4, Node(5, None))))))
        self.assertEqual(stack.size(), 5)

# WRITE TESTS FOR STACK OPERATIONS - PUSH, POP, PEEK, etc.

if __name__ == '__main__': 
    unittest.main()
