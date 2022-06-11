from __future__ import annotations
from typing import Optional, Any, List

class Node:
    """Node for use with doubly-linked list"""
    def __init__(self, item: Any):
        self.item = item  # item held by Node
        self.next: Node = self  # reference to next Node, init to this Node
        self.prev: Node = self  # reference to previous Node, init to this Node

class OrderedList:
    """A doubly-linked ordered list of integers, 
    from lowest (head of list, sentinel.next) to highest (tail of list, sentinel.prev)"""
    def __init__(self) -> None:
        """Use only a sentinel Node. No other instance variables"""
        self.sentinel: Node = Node(None)    # Empty linked list, just sentinel Node
        self.sentinel.next = self.sentinel  # Initialize next to sentinel
        self.sentinel.prev = self.sentinel  # Initialize prev to sentinel

    def __eq__(self, other: object) -> bool:
        lists_equal = True
        if not isinstance(other, OrderedList):
            lists_equal = False
        else:
            s_cur = self.sentinel.next
            o_cur = other.sentinel.next
            while s_cur != self.sentinel and o_cur != other.sentinel:
                if s_cur.item != o_cur.item:
                    lists_equal = False
                s_cur = s_cur.next
                o_cur = o_cur.next
            if s_cur != self.sentinel or o_cur != other.sentinel:
                lists_equal = False
        return lists_equal

    def is_empty(self) -> bool:
        """Returns back True if OrderedList is empty"""
        return self.sentinel.next == self.sentinel and self.sentinel.prev == self.sentinel

    def add(self, item: Any) -> None:
        """Adds an item to OrderedList, in the proper location based on ordering of items
        from lowest (at head of list) to highest (at tail of list)
        If item is already in list, do not add again (no duplicate items)"""

        if self.is_empty():
            first = self.sentinel.next = Node(item)
            first.next = self.sentinel
            first.prev = self.sentinel
        
        cur = self.sentinel.next
        new_node = Node(item)

        # if the item is greater than cur.item
        if item > cur.item:
            
            # iterating through the doubly linked list and setting ucr to cur.next 
            while cur.next != self.sentinel and item > cur.item:
                cur = cur.next

            # adding item to the end of the linked list
            if item != cur.item and item > cur.item:
                new_node.next = self.sentinel
                new_node.prev = cur
                cur.next = new_node
                self.sentinel.prev = new_node
            
            # adding item to the middle of the linked list
            elif item != cur.item and item < cur.item:
                new_node.next = cur
                new_node.prev = cur.prev
                cur.prev.next = new_node
                cur.prev = new_node

        # adding item to the front of the doubly linked list
        elif item != cur.item and item < cur.item:
            new_node.next = cur
            new_node.prev = self.sentinel
            cur.prev = new_node
            self.sentinel.next = new_node
            

    def remove(self, item: Any) -> bool:
        """Removes an item from OrderedList. If item is removed (was in the list) returns True
        If item was not removed (was not in the list) returns False"""

        if self.is_empty():
            return False

        cur = self.sentinel.next

        # iterating through the doubly linked list and setting ucr to cur.next 
        while cur.next != self.sentinel and item > cur.item:
            cur = cur.next

        # removing something from the front of the doubly linked list
        if item == cur.item:
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            return True
        
        return False

    def index(self, item: Any) -> Optional[int]:
        """Returns index of an item in OrderedList (assuming head of list is index 0).
        If item is not in list, return None"""

        if self.is_empty():
            return None
        
        cur = self.sentinel.next
        counter = 0

        # iterating through the doubly linked list and setting ucr to cur.next 
        while cur.next != self.sentinel and item > cur.item:
            cur = cur.next
            counter += 1

        # removing something from the front of the doubly linked list
        if item == cur.item:
            return counter
        
        return None

    def pop(self, index: int) -> Any:
        """Removes and returns item at index (assuming head of list is index 0).
        If index is negative or >= size of list, raises IndexError"""

        if self.is_empty() or index <= -1 or index >= self.size():
            raise IndexError
        
        cur = self.sentinel.next
        counter = 0

        # iterating through the doubly linked list and setting ucr to cur.next 
        while cur.next != self.sentinel and  counter < index:
            cur = cur.next
            counter += 1

        if counter == index:
            temp_item = cur.item
            cur.prev.next = cur.next
            cur.next.prev = cur.prev

        return temp_item

    def search(self, item: Any) -> bool:
        """Searches OrderedList for item, returns True if item is in list, False otherwise - USE RECURSION"""
        return self._search(self.sentinel.next, item)
    
    def _search(self, node: Node, item: Any) -> bool:
        
        if node is self.sentinel:
            return False

        if node.item == item:
            return True

        return self._search(node.next, item)

    def python_list(self) -> List:
        """Return a Python list representation of OrderedList, from head to tail
        For example, list with integers 1, 2, and 3 would return [1, 2, 3]"""

        p_list = []

        cur = self.sentinel.next

        while cur != self.sentinel:
            p_list.append(cur.item)
            cur = cur.next

        return p_list

    def python_list_reversed(self) -> List:
        """Return a Python list representation of OrderedList, from tail to head, USING RECURSION
        For example, list with integers 1, 2, and 3 would return [3, 2, 1]"""

        return self._python_list_reversed(self.sentinel.next)

    def _python_list_reversed(self, node: Node) -> List:

        p_list_reversed: List[Any] = []
        
        # base case when node is self.sentinel in memory again
        if node is self.sentinel:
            return p_list_reversed

        # p_list_reversed.extend(self._python_list_reversed(node.next))

        # recursive call of the function to the next node value
        rest = self._python_list_reversed(node.next)
        
        # p_list_reversed.append(node.item)

        # return case that adds the rest of the case with the node.item
        return rest + [node.item]
        

    def size(self) -> int:
        """Returns number of items in the OrderedList - USE RECURSION"""
        return self._size(self.sentinel.next)
        
    def _size(self, node: Node) -> int:

        if node is self.sentinel:
            return 0

        return 1 + self._size(node.next)

o1 = OrderedList()

o1.add(5)