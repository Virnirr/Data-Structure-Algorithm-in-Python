from logging import raiseExceptions
import unittest
from queue_nodelist import *

class TestLab1(unittest.TestCase):

    def test_nodelist(self) -> None:
        q = Queue()
        self.assertEqual(q.rear, None)
        self.assertEqual(q.front, None)
        q.enqueue(1)
        self.assertEqual(q.rear, Node(1, None))
        self.assertEqual(q.front, None)
        q.enqueue(2)
        self.assertEqual(q.rear, Node(2, Node(1, None)))
        self.assertEqual(q.dequeue(),1)
        self.assertEqual(q.rear, None)
        self.assertEqual(q.front, Node(2, None))
        self.assertFalse(Node(1,None).__eq__(None))
        q2 = Queue()
        self.assertEqual(q2.is_empty(), True)
        with self.assertRaises(IndexError):
            q3 = Queue()
            q3.dequeue()

    def test_repr(self) -> None:
        q = Queue()
        q.enqueue(1)
        self.assertEqual(q.__repr__(), "Queue(Node(1, None), None)")

    def test_eq(self) -> None:
        q1 = Queue()
        q1.enqueue(1)
        q1.enqueue(2)
        q2 = Queue()
        q2.enqueue(1)
        q2.enqueue(2)
        self.assertEqual(q1, q2)
        self.assertFalse(q1.__eq__(None))
        q1.dequeue()
        q2.dequeue()
        self.assertEqual(q1, q2)

    def test_queue_simple(self) -> None:
        q = Queue()
        q.enqueue(1)
        self.assertEqual(q.size(), 1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)
        self.assertEqual(q.size(), 5)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.dequeue(), 4)
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.dequeue(), 5)

if __name__ == '__main__': 
    unittest.main()
