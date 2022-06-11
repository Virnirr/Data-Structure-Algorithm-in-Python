from __future__ import annotations
from pickle import NONE
# NodeList version of ADT Queue

from typing import Optional, List, Any

# Node class for use with Queue implemented with linked list
# NodeList is one of
# None or
# Node(value, rest), where rest is the rest of the list
class Node:
    def __init__(self, value: Any, rest: Optional[Node]):
        self.value = value      # value
        self.rest = rest        # NodeList

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Node):
            return self.value == other.value and self.rest == other.rest
        else:
            return False

    def __repr__(self) -> str:
        return ("Node({!r}, {!r})".format(self.value, self.rest))

# my queue
class Queue:
    def __init__(self, rear: Optional[Node] = None, front: Optional[Node] = None, num_items: int = 0):
        self.rear = rear    # rear NodeList
        self.front = front   # front NodeList
        self.num_items = num_items  # number of items in Queue

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Queue):
            return self.get_items() == other.get_items()
        else:
            return False

    def __repr__(self) -> str:
        return ("Queue({!r}, {!r})".format(self.rear, self.front))

    # get_items returns array (Python list) of items in Queue
    # first item in the list will be front of queue, last item is rear of queue
    def get_items(self) -> List:
        items: List = []
        front = self.front
        while front is not None:
            items.append(front.value)
            front = front.rest
        if self.rear is not None:
            rear_items = []
            rear: Optional[Node] = self.rear
            while rear is not None:
                rear_items.append(rear.value)
                rear = rear.rest
            rear_items.reverse()
            items.extend(rear_items)
        return items

    def is_empty(self) -> bool:
        """Returns true if the queue is empty and false otherwise
        Must be O(1)"""
        
        return self.num_items == 0

    def enqueue(self, item: Any) -> None:
        """enqueues item, adding it to the rear NodeList
        Must be O(1)"""

        temp = self.rear
        self.rear = Node(item, temp)
        self.num_items += 1

    def dequeue(self) -> Any:
        """dequeues item, removing first item from front NodeList
        If front NodeList is empty, remove items from rear NodeList
        and add to front NodeList until rear NodeList is empty
        If front NodeList and rear NodeList are both empty, raise IndexError
        Must be O(1) - general case"""

        if self.front is None and self.rear is None:
            raise IndexError

        if self.front is None:
            while self.rear is not None:
                temp = self.rear
                self.front = Node(temp.value, self.front)
                self.rear = temp.rest
    
        if self.front is not None:
            temp_dequeue_value = self.front.value
            self.front = self.front.rest
            self.num_items -= 1
        
        return temp_dequeue_value

    def size(self) -> int:
        """Returns the number of items in the queue
        Must be O(1)"""

        return self.num_items

