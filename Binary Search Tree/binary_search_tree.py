from __future__ import annotations
import re
from queue_array import Queue
from typing import Optional, Any, Tuple, List


class TreeNode:
    def __init__(self, key: Any, data: Any, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

    def __eq__(self, other: object) -> bool:
        if isinstance(other, TreeNode):
            return (self.key == other.key
                    and self.data == other.data
                    and self.left == other.left
                    and self.right == other.right)
        else:
            return False

    def __repr__(self) -> str:
        return ("TreeNode({!r}, {!r}, {!r}, {!r})".format(self.key, self.data, self.left, self.right))


class BinarySearchTree:
    def __init__(self, root_node: Optional[TreeNode] = None):  # Returns empty BST
        self.root: Optional[TreeNode] = root_node

    # returns True if tree is empty, else False
    def is_empty(self) -> bool:
        return self.root == None

    # returns True if key is in a node of the tree, else False
    def search(self, key: Any) -> bool:

        # return False if node not found
        if self.is_empty():
            return False

        return self._search(self.root, key)

    # helper function to search for key recursively in the tree
    def _search(self, tnode: Optional[TreeNode], key: Any) -> bool:

        # base case if key was not foudn
        if tnode is None:
            return False

        # return True if node is found
        if tnode.key == key:
            return True
        
        if key < tnode.key:
            return self._search(tnode.left, key)

        return self._search(tnode.right, key)

    # Inserts new node w/ key and data
    # If an item with the given key is already in the BST,
    # the data in the tree will be replaced with the new data
    # Example creation of node: temp = TreeNode(key, data)
    # On insert, can assume key not already in BST
    def insert(self, key: Any, data: Any = None) -> None:

        new_tnode = TreeNode(key, data)

        if self.is_empty():
            self.root = new_tnode
        
        return self._insert(self.root, new_tnode)

    # helper function for insert
    def _insert(self, tnode: Optional[TreeNode], newNode: Optional[TreeNode]) -> None:
        
        # check left side of tree if the current key is greater than the newNode key
        if tnode is not None and newNode is not None:

            if tnode.key > newNode.key:

                # insert the newNode into the left side of the tree when the left side is empty
                if tnode.left is None:
                    tnode.left = newNode
                    return None
                
                # recursively call insert and to the left side of the tree if the left side is not empty
                return self._insert(tnode.left, newNode)

            # check right side of tree if the current key is less than the newNode key
            elif tnode.key < newNode.key:
                
                # insert the newNode into the right side of the tree when the right is empty
                if tnode.right is None:
                    tnode.right = newNode
                    return None

                # recursively called insert and to the right side of tree if the tree is not empty
                return self._insert(tnode.right, newNode)

            # check if the data that we called on is the same as newNode data. 
            # replace it if the data is the same.
            elif tnode.key == newNode.key:
                tnode.data = newNode.data
                return None
            

    # returns tuple with min key and associated data in the BST
    # returns None if the tree is empty

    def find_min(self) -> Optional[Tuple[Any, Any]]:

        return self._find_min(self.root)

    # helper function for find_min node
    def _find_min(self, tnode: Optional[TreeNode]) -> Optional[Tuple[Any,Any]]:
        
        if tnode is not None:
            if tnode.left is None:
                return (tnode.key, tnode.data)

            return self._find_min(tnode.left)
        
        # return None if there is no node in the tree or if it's empty
        return None

    # returns tuple with max key and associated data in the BST
    # returns None if the tree is empty
    def find_max(self) -> Optional[Tuple[Any, Any]]:

        return self._find_max(self.root)

    # helping function for find_max node
    def _find_max(self, tnode: Optional[TreeNode]) -> Optional[Tuple[Any, Any]]:
        
        if tnode is not None:
            if tnode.right is None:
                return (tnode.key, tnode.data)

            return self._find_max(tnode.right)
        
        # return None if there is no node in the tree or if it's empty
        return None

    # returns the height of the tree
    # if tree is empty, return None
    def tree_height(self) -> Optional[int]:
        
        if self.is_empty():
            return None

        return self._tree_height(self.root)

    def _tree_height(self, tnode: Optional[TreeNode]) -> int:

        if tnode is None:
            return -1

        return 1 + max(self._tree_height(tnode.left), self._tree_height(tnode.right))

    # returns Python list of BST keys representing inorder traversal of BST
    def inorder_list(self) -> List:

        my_list: List[Any] = []
        
        if self.is_empty():
            return my_list # empty list []

        self._inorder_list(self.root, my_list)
        return my_list
        
    def _inorder_list(self, tnode: Optional[TreeNode], orderedList: List[Any]) -> None:

        # return empty list when you reach None
        if tnode is None:
            return None

        self._inorder_list(tnode.left, orderedList)
        orderedList.append(tnode.key)
        self._inorder_list(tnode.right, orderedList)

        # ------------------Alternative code by creating a new list-----------------------
        # # check if it's leaf node
        # if tnode.right is None and tnode.left is None:
        #     return [tnode.key]

        # # check if there is a value in the left node and not right node
        # if tnode.left is not None and tnode.right is None:
            
        #     return self._inorder_list(tnode.left) + [tnode.key]

        # # check if there is a value in the right node and not the left node
        # if tnode.right is not None and tnode.left is None:
            
        #     return [tnode.key] + self._inorder_list(tnode.right)

        # # checks for root node and subtree node
        # return self._inorder_list(tnode.left) + [tnode.key] + self._inorder_list(tnode.right)
        
    # returns Python list of BST keys representing preorder traversal of BST
    def preorder_list(self) -> List:
        my_list: List[Any] = []
        
        if self.is_empty():
            return my_list # empty list []

        self._preorder_list(self.root, my_list)
        return my_list

    def _preorder_list(self, tnode: Optional[TreeNode], orderedList: List[Any]) -> None:

        if tnode is None:
            return None
        
        orderedList.append(tnode.key)
        self._preorder_list(tnode.left, orderedList)
        self._preorder_list(tnode.right, orderedList)
        
    # returns Python list of BST keys representing level-order traversal of BST
    # You MUST use your queue_array data structure from lab 3 to implement this method
    def level_order_list(self) -> List:
        q = Queue(25000)  # Don't change this!

        level_list: List[Any] = []

        if self.root is not None:

            if q.is_empty():
                q.enqueue(self.root)

            while not q.is_empty():
                temp = q.dequeue()
                if temp is not None:
                    level_list.append(temp.key)
                    q.enqueue(temp.left)
                    q.enqueue(temp.right)
            
        return level_list