import unittest
from sep_chain_ht import *

class TestList(unittest.TestCase):

   def test_insert1(self) -> None:
      hash1 = MyHashTable()
      hash1.insert(11, "a") 
      hash1.insert(3, "b")
      self.assertEqual(hash1.size(), 2)
      with self.assertRaises(ValueError):
         hash1.insert(-5, "c")

   def test_get1(self) -> None:
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      hash1.insert(3, "b")
      self.assertEqual(hash1.get_item(3), 'b')
      self.assertEqual(hash1.get_item(11), 'a')
      
   def test_get2(self) -> None:
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      with self.assertRaises(LookupError):
            hash1.get_item(6)

   def test_remove1(self) -> None:
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      self.assertEqual(hash1.remove(11), (11, 'a'))
      self.assertEqual(hash1.size(), 0)

   def test_load_factor1(self) -> None:
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      hash1.insert(3, "b")
      hash1.insert(1, "c")
      hash1.insert(8, "d")
      hash1.insert(4, "e")
      hash1.insert(5, "f")
      hash1.insert(1, "g")
      hash1.insert(2, "h")
      self.assertEqual(hash1.load_factor(), 1.4)

   def test_collisions2(self) -> None:
      hash1 = MyHashTable(5)
      hash1.insert(11, "a") 
      hash1.insert(3, "b") 
      hash1.insert(1, "c") 
      hash1.insert(8, "d") 
      hash1.insert(4, "e") 
      hash1.insert(5, "f")
      hash1.insert(1, "g") 
      hash1.insert(2, "h")
      self.assertEqual(hash1.collisions(), 2)
   
   def test_load_factor2(self) -> None:
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      hash1.insert(3, "b")
      hash1.insert(1, "c")
      hash1.insert(8, "d")
      hash1.insert(4, "e")
      hash1.insert(5, "f")
      hash1.insert(1, "g")
      hash1.insert(2, "h")
      hash1.insert(41, "k")
      hash1.insert(3, "p")
      hash1.insert(11, "g")
      self.assertEqual(hash1.num_items, 8)
      self.assertEqual(hash1.get_item(11), "g")
      self.assertEqual(hash1.get_item(3), "p")
      self.assertAlmostEqual(hash1.load_factor(), 8/11)

   def test_remove(self) -> None:
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      hash1.insert(3, "b")
      hash1.insert(1, "c")
      hash1.insert(8, "d")
      hash1.insert(4, "e")
      hash1.insert(5, "f")
      hash1.insert(1, "g")
      hash1.insert(2, "h")
      hash1.insert(41, "k")
      hash1.insert(3, "p")
      hash1.insert(11, "g")
      with self.assertRaises(LookupError):
            hash1.remove(100)

if __name__ == '__main__': 
   unittest.main()


