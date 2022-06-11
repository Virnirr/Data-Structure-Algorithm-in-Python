from typing import Any, Tuple, List

class MyHashTable:

    def __init__(self, table_size: int = 11):
        self.table_size = table_size
        self.hash_table: List = [[] for _ in range(table_size)] # List of lists implementation
        self.num_items = 0
        self.num_collisions = 0

    def insert(self, key: int, value: Any) -> None:
        """Takes a key, and an item.  Keys are valid Python non-negative integers.
        If key is negative, raise ValueError exception
        The function will insert the key-item pair into the hash table based on the
        hash value of the key mod the table size (hash_value = key % table_size)"""

        if key < 0:
            raise ValueError

        hash_value = key % self.table_size
        
        # just append to the list of the hashed index if it's empty
        if self.hash_table[hash_value] == []:
            self.hash_table[hash_value].append((key, value))
            self.num_items += 1

        # check if the key is already in the current hashed index
        else:
            
            # zipping all the two tuples (key, value) from a hashed index
            # into two large tuples with (key), (values)
            unzip = lambda z: list(zip(*z))
            hash_nested = unzip(self.hash_table[hash_value])

            # check if key is in all of key of the hashed value
            if key in hash_nested[0]:   

                # loop through the length of the chained key, value pairs in the hashed table
                for i in range(len(self.hash_table[hash_value])):

                    # if the key does exist, then swap the (key, value) pair
                    if key in self.hash_table[hash_value][i]:
                        self.hash_table[hash_value][i] = (key, value)

            # if key doesn't exist, then append it to the end of the hash index array
            else:
                self.hash_table[hash_value].append((key, value))
                self.num_items += 1
                self.num_collisions += 1
        
        # if load factor becomes greater than 1.5, create a new hash_table
        # with size (2 * self.table_size) + 1 and then swap with hash_table
        if self.load_factor() > 1.5:

            # new table size
            self.table_size = (2 * self.table_size) + 1
            new_table: List = [[] for _ in range(self.table_size)]

            # hash in old hash value to new table using new table size 
            for hash in self.hash_table:
                
                # check if the value is empty or not
                if hash != []:

                    for key_new, value_new in hash:

                        # make the new_hash_value of the old key, value pair
                        new_hash_value = key_new % self.table_size

                        # check if the spot on the new hash value is empty and appned if it is
                        if new_table[new_hash_value] == []:
                            new_table[new_hash_value].append((key_new, value_new))

                        else:
                            new_table[new_hash_value].append((key_new, value_new))

                        # -------------Possibly do not need these---------------
                        # run if there's already key, value inside of the new hashed index
                        # else:
                        #     # zipping all the two tuples (key, value) into two large tuples with (key), (values)
                        #     new_unzip = lambda z: list(zip(*z))
                        #     new_hash_nested = new_unzip(new_table[new_hash_value])

                        #     # check if key is in all of key of the hashed value
                        #     if key_new in new_hash_nested[0]:
                        #         for i in range(len(new_table[new_hash_value])):

                        #             # if the key does exist, then swap the (key, value) pair
                        #             if key_new in new_table[new_hash_value][0]:
                        #                 new_table[new_hash_value] = (key_new, value_new)

                            # if key doesn't exist, then append it to the end of the hash index array

            # finally replace old table with new table
            self.hash_table = new_table

    def get_item(self, key: int) -> Any:
        """Takes a key and returns the item from the hash table associated with the key.
        If no key-item pair is associated with the key, the function raises a LookupError exception."""

        hash_value = key % self.table_size

        # check if the index of the hash value has any key equal to the key that was taken in
        for key_value in self.hash_table[hash_value]:

            # if the key exist, return the associated value
            if key_value[0] == key:
                return key_value[1]

        # if no key found, raise LookupError
        raise LookupError

    def remove(self, key: int) -> Tuple[int, Any]:
        """Takes a key, removes the key-item pair from the hash table and returns the key-item pair.
        If no key-item pair is associated with the key, the function raises a LookupError exception.
        (The key-item pair should be returned as a tuple)"""

        hash_value = key % self.table_size
        
        # check if the hash value has the input key
        for i in range(len(self.hash_table[hash_value])):

            # if the key exist in the hashed value index, then pop the (key, value) and return it
            if self.hash_table[hash_value][i][0] == key:
                self.num_items -= 1
                return self.hash_table[hash_value].pop(i)

        # raise LookupError if not found
        raise LookupError

    def load_factor(self) -> float:
        """Returns the current load factor of the hash table"""
        return self.num_items / len(self.hash_table)

    def size(self) -> int:
        """Returns the number of key-item pairs currently stored in the hash table"""
        return self.num_items

    def collisions(self) -> int:
        """Returns the number of collisions that have occurred during insertions into the hash table"""
        return self.num_collisions