from typing import List, Any, Optional

class HashTable:

    def __init__(self, table_size: int):            # can add additional attributes
        self.table_size = table_size                # initial table size
        self.hash_table: List = [None]*table_size   # hash table
        self.num_items = 0                          # empty hash table

    def insert(self, key: str, value: Any) -> None:
        """ Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is any object (e.g. Python List).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is is in the table, the new value replaces the existing value.
        When used with the concordance, value is a Python List of line numbers.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1)."""

        index = self.horner_hash(key)

        # just put the index equal to the (key, value) if it's None
        if self.hash_table[index] is None:
            self.hash_table[index] = (key, value)
            self.num_items += 1

        # replace if it's already there
        elif self.hash_table[index][0] == key:
            self.hash_table[index] = (key, value)

        # quadratic probing
        else:
            probe_index = 1

            # standard hashed index used to calculate the index of new quadratic probing each time
            # to have a constant and standard beginning index to probe through 
            standard_index = self.horner_hash(key)
            # check if the current hash index is either not None or doesn't have the old key.
            # don't run the while loop if it's None or it has the old hash key
            while self.hash_table[index] is not None and self.hash_table[index][0] != key:
                index = (standard_index + (probe_index ** 2)) % self.table_size
                probe_index += 1

            self.hash_table[index] = (key, value)
            self.num_items += 1
        
        # create new table if the old table's load factor becomes greater than 0.5
        if self.get_load_factor() > 0.5:
            
            self.table_size = (2 * self.table_size) + 1
            new_hash_table: List = [None]*self.table_size

            for key_value in self.hash_table:

                if key_value is not None:
                    old_hash_key = key_value[0]
                    old_hash_value = key_value[1]
                    new_index = self.horner_hash(old_hash_key)

                    # just put the index equal to the (key, value) if it's None or replace if it's already there
                    if new_hash_table[new_index] is None:
                        new_hash_table[new_index] = (old_hash_key, old_hash_value)
                    
                    # quadratic probing for new table, when inserting old values
                    else:
                        new_probe_index = 1

                        # standard hashed index used to calculate the index of new quadratic probing each time
                        # to have a constant and standard beginning index to probe through 
                        new_standard_index = self.horner_hash(old_hash_key)
                        # check if the current hash index is either not None or doesn't have the old key.
                        # don't run the while loop if it's None or it has the old hash key
                        while new_hash_table[new_index] is not None and new_hash_table[new_index][0] != old_hash_key:
                            new_index =  (new_standard_index + (new_probe_index ** 2)) % self.table_size
                            new_probe_index += 1

                        new_hash_table[new_index] = (old_hash_key, old_hash_value)

            # switch to new table
            self.hash_table = new_hash_table

    def horner_hash(self, key: str) -> int:
        """ Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification."""
        
        hash_value = 0
        min_n_value = min(len(key), 8)

        # h(str) = ∑ (from i = 0 to n - 1): ord(str[i]) ∗ 31^(n-1-i) where n = the minimum of len(str) and 8
        # i is the index of the characters that are hashed
        for i in range(min_n_value):
            hash_value += (ord(key[i]) * (31**(min_n_value-1-i)))

        return hash_value % self.get_table_size()

    def in_table(self, key: str) -> bool:
        """ Returns True if key is in an entry of the hash table, False otherwise. Must be O(1)."""
        index = self.horner_hash(key)

        if self.hash_table[index] is None:
            return False

        if self.hash_table[index][0] == key:
            return True

        # var to keep track of many times to do quadratic probing
        probe_index = 1

        # standard hashed index used to calculate the index of new quadratic probing each time
        # to have a constant and standard beginning index to probe through 
        standard_index = self.horner_hash(key)

        # qudartic probing until it finds the key or the index is None
        while self.hash_table[index] is not None:
            index = (standard_index + (probe_index ** 2)) % self.table_size
            
            if self.hash_table[index] is not None and self.hash_table[index][0] == key:
                return True

            probe_index += 1

        return False

    def get_index(self, key: str) -> Optional[int]:
        """ Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None. Must be O(1)."""

        index = self.horner_hash(key)

        if self.hash_table[index] is None:
            return None

        if self.hash_table[index][0] == key:
            return index

        # var to keep track of many times to do quadratic probing
        probe_index = 1

        # standard hashed index used to calculate the index of new quadratic probing each time
        # to have a constant and standard beginning index to probe through 
        standard_index = self.horner_hash(key)

        # qudartic probing until it finds the key or the index is None
        while self.hash_table[index] is not None:
            index = (standard_index + (probe_index ** 2)) % self.table_size
            
            if self.hash_table[index] is not None and self.hash_table[index][0] == key:
                return index

            probe_index += 1

        return None

    def get_all_keys(self) -> List:
        """ Returns a Python list of all keys in the hash table."""

        key_list = []
        for hash in self.hash_table:
            if hash is not None:
                key_list.append(hash[0])

        return key_list

    def get_value(self, key: str) -> Any:
        """ Returns the value (for concordance, list of line numbers) associated with the key.
        If key is not in hash table, returns None. Must be O(1)."""
    
        index = self.horner_hash(key)

        if self.hash_table[index] is None:
            return None

        if self.hash_table[index][0] == key:
            return self.hash_table[index][1]

        # var to keep track of many times to do quadratic probing
        probe_index = 1

        # standard hashed index used to calculate the index of new quadratic probing each time
        # to have a constant and standard beginning index to probe through 
        standard_index = self.horner_hash(key)

        # qudartic probing until it finds the key or the index is None
        while self.hash_table[index] is not None:
            index = (standard_index + (probe_index ** 2)) % self.table_size
            
            if self.hash_table[index] is not None and self.hash_table[index][0] == key:
                return self.hash_table[index][1]

            probe_index += 1

        return None

    def get_num_items(self) -> int:
        """ Returns the number of entries (words) in the table. Must be O(1)."""
        return self.num_items

    def get_table_size(self) -> int:
        """ Returns the size of the hash table."""
        return self.table_size

    def get_load_factor(self) -> float:
        """ Returns the load factor of the hash table (entries / table_size)."""
        return self.get_num_items() / self.get_table_size()