import unittest
from hash_quad import *

class TestList(unittest.TestCase):

    def test_05_quad_wrap_around(self):
        table = HashTable(211)

        for i in range(10, 101):
            table.insert(chr(i), 10*i)

        key = chr(1) + 'E'
        table.insert(key, ['cat']) # Hashes to 100, goes to 101
        self.assertTrue(table.in_table(key))
        self.assertEqual(table.get_index(key), 101)
        self.assertEqual(table.get_value(key), ['cat'])
       
        key = chr(2) + '&'
        table.insert(key, ['dog']) # Hashes to 100, goes to 104
        self.assertTrue(table.in_table(key))
        self.assertEqual(table.get_index(key), 104)
        self.assertEqual(table.get_value(key), ['dog'])
       
        key = chr(3) + chr(7)
        table.insert(key, ['elephant']) # Hashes to 100, goes to 109
        self.assertTrue(table.in_table(key))
        self.assertEqual(table.get_index(key), 109)
        self.assertEqual(table.get_value(key), ['elephant'])        

        key = chr(0) + 'd'
        table.insert(key, ['mouse']) # Hashes to 100, goes to 116
        self.assertTrue(table.in_table(key))
        self.assertEqual(table.get_index(key), 116)
        self.assertEqual(table.get_value(key), ['mouse'])        

    def test_06_quad_wrap_around_rehash(self):
        table = HashTable(10)

        key = chr(32)
        table.insert(key, ['cat']) # Hashes to 2, goes to 2
        self.assertTrue(table.in_table(key))
        self.assertEqual(table.get_index(key), 2)
        self.assertEqual(table.get_value(key), ['cat'])
        self.assertEqual(table.get_num_items(), 1)
        self.assertEqual(table.get_load_factor(), 1/10)

        key = chr(42)
        table.insert(key, ['dog']) # Hashes to 2, goes to 3
        self.assertTrue(table.in_table(key))
        self.assertEqual(table.get_index(key), 3)
        self.assertEqual(table.get_value(key), ['dog'])
        self.assertEqual(table.get_num_items(), 2)
        self.assertEqual(table.get_load_factor(), 2/10)

        key = chr(52)
        table.insert(key, ['elephant']) # Hashes to 2, goes to 6
        self.assertTrue(table.in_table(key))
        self.assertEqual(table.get_index(key), 6)
        self.assertEqual(table.get_value(key), ['elephant'])
        self.assertEqual(table.get_num_items(), 3)
        self.assertEqual(table.get_load_factor(), 3/10)

        key = chr(62)
        table.insert(key, ['mouse']) # Hashes to 2, goes to 1
        self.assertTrue(table.in_table(key))
        self.assertEqual(table.get_index(key), 1)
        self.assertEqual(table.get_value(key), ['mouse'])
        self.assertEqual(table.get_num_items(), 4)
        self.assertEqual(table.get_load_factor(), 4/10)

        key = chr(72)
        table.insert(key, ['lion']) # Hashes to 2, goes to 8
        self.assertTrue(table.in_table(key))
        self.assertEqual(table.get_index(key), 8)
        self.assertEqual(table.get_value(key), ['lion'])
        self.assertEqual(table.get_num_items(), 5)
        self.assertEqual(table.get_load_factor(), 5/10)

        key = chr(82)
        table.insert(key, ['tiger']) # Hashes to 2, goes to 19
        self.assertTrue(table.in_table(key))
        self.assertEqual(table.get_index(key), 19)
        self.assertEqual(table.get_value(key), ['tiger'])
        self.assertEqual(table.get_num_items(), 6)
        self.assertEqual(table.get_load_factor(), 6/21)

if __name__ == '__main__':
   unittest.main()