from re import S
from typing import Any, List

class MinHeap:

    def __init__(self, capacity: int = 50):
        """Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created."""
        self.heap: List = [0]*(capacity+1)     # index 0 not used for heap
        self.num_items = 0                     # empty heap

    def enqueue(self, item: Any) -> None:
        """inserts "item" into the heap
        Raises IndexError if there is no room in the heap"""

        if self.is_full():
            raise IndexError
        
        self.num_items += 1
        self.heap[self.num_items] = item

        # current index
        cur_index = self.num_items

        if self.num_items > 1:
            self.perc_up(cur_index)

    def peek(self) -> Any:
        """returns root of heap (highest priority) without changing the heap
        Raises IndexError if the heap is empty"""

        if self.is_empty():
            raise IndexError

        return self.heap[1]

    def dequeue(self) -> Any:
        """returns item at root (highest priority) - removes it from the heap and restores the heap property
           Raises IndexError if the heap is empty"""

        if self.is_empty():
            raise IndexError

        temp_value = self.heap[1]

        self.heap[1] = self.heap[self.num_items]
        self.heap[self.num_items] = 0
        self.num_items -= 1

        self.perc_down(1)

        return temp_value

    def contents(self) -> List:
        """returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)
        If heap is empty, returns empty list []"""

        if self.is_empty():
            return []

        return self.heap[1:self.size() + 1]

    def build_heap(self, alist: List) -> None:
        """Discards the items in the current heap and builds a heap from
        the items in alist using the bottom up method.
        If the capacity of the current heap is less than the number of
        items in alist, the capacity of the heap will be increased to accommodate the items in alist"""

        if self.capacity() < len(alist):
            self.heap = [0] * (len(alist) + 1)

        else:
            self.heap = [0] * (self.capacity() + 1)

        for i in range(len(alist)):
            self.heap[i+1] = alist[i]
        
        self.num_items = len(alist)

        index = self.num_items // 2
        for i in range(index, 0, -1):
            self.perc_down(i)

    def is_empty(self) -> bool:
        """returns True if the heap is empty, false otherwise"""
        return self.num_items == 0

    def is_full(self) -> bool:
        """returns True if the heap is full, false otherwise"""
        return self.num_items == self.capacity()

    def capacity(self) -> int:
        """This is the maximum number of a entries the heap can hold, which is
        1 less than the number of entries that the array allocated to hold the heap can hold"""
        return len(self.heap) - 1
    
    def size(self) -> int:
        """the actual number of elements in the heap, not the capacity"""

        if self.is_empty():
            return 0

        return self.num_items


    def perc_down(self,i: int) -> None:
        """where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        cur = i
        while ((cur * 2) <= self.num_items and (self.heap[cur] > self.heap[cur * 2])) or ((cur * 2 + 1) <= self.num_items and self.heap[cur] > self.heap[cur * 2 + 1]):
            
            # check if it's less than both and then check for min of both.
            if (cur * 2 + 1) <= self.num_items and self.heap[cur] > self.heap[cur * 2 + 1]:
                
                if self.heap[cur] >= self.heap[cur * 2] and self.heap[cur] >= self.heap[cur * 2 + 1]:
                    
                    min_value = min(self.heap[cur * 2], self.heap[cur * 2 + 1])
                    min_index = self.heap.index(min_value)
                    temp_min = self.heap[min_index]
                    self.heap[min_index] = self.heap[cur]
                    self.heap[cur] = temp_min
                    
                    # change cur index to the index that was swapped
                    cur = min_index
                
                elif self.heap[cur] >= self.heap[cur * 2 + 1]:
                    temp_second = self.heap[cur * 2 + 1]
                    self.heap[cur * 2 + 1] = self.heap[cur]
                    self.heap[cur] = temp_second
                    # change cur index to the index that was swapped
                    cur = cur * 2 + 1
            
            elif self.heap[cur] >= self.heap[cur * 2]:

                temp_first = self.heap[cur * 2]
                self.heap[cur * 2] = self.heap[cur]
                self.heap[cur] = temp_first

                # change cur index to the index that was swapped
                cur = cur * 2


    def perc_up(self,i: int) -> None:
        """where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""

        cur_index = i
    
        while cur_index > 1 and self.heap[cur_index] < self.heap[cur_index//2]:
            
            # swap until the value is greater than the parent or the index is 1 (root node)
            temp_item = self.heap[cur_index//2]
            self.heap[cur_index//2] = self.heap[cur_index] 
            self.heap[cur_index] = temp_item
            cur_index = cur_index//2

    def heap_sort_ascending(self, alist: List) -> None:
        """perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, and mutate (change contents of) alist to put the items in ascending order"""

        if self.capacity() < len(alist):
            self.heap = [0] * (len(alist) + 1)

        else:
            self.heap = [0] * (len(self.heap))
        
        self.num_items = 0

        for i in range(len(alist)):
            self.enqueue(alist[i])

        for i in range(len(alist)):
            alist[i] = self.dequeue()