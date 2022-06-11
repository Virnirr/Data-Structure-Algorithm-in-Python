from typing import Any, List, Optional
from hash_quad import *
import string

class Concordance:

    def __init__(self) -> None:
        """ Starting size of hash table should be 191: self.concordance_table = HashTable(191) """
        self.stop_table: Optional[HashTable] = None          # hash table for stop words
        self.concordance_table: HashTable = HashTable(191)              # hash table for concordance

    def load_stop_table(self, filename: str) -> None:
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        
        try:
            with open(filename, "r") as txt_file:
                stop_word_list = txt_file.read().lower().split()
                self.stop_table = HashTable(191)
                for word in stop_word_list:
                    self.stop_table.insert(word, None)
        
        except:
            raise FileNotFoundError

    def load_concordance_table(self, filename: str) -> None:
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)

        Process of adding new line numbers for a word (key) in the concordance:
            If word is in table, get current value (list of line numbers), append new line number, insert (key, value)
            If word is not in table, insert (key, value), where value is a Python List with the line number
        If file does not exist, raise FileNotFoundError """

        try:
            with open(filename, "r") as txt_file:
                
                # enumerate or go through each line by line
                for i, line in enumerate(txt_file):
            
                    for letter in line:
                        if (letter in string.punctuation and letter != "-") or letter in string.digits:
                            line = line.replace(letter, "")

                        elif letter == "-":
                            line = line.replace(letter, " ")
                        
                        else:
                            line = line.replace(letter, letter.lower())
                    # place concordance into concordance table
                    concords = set(line.split())
                    for hash in concords:

                        if self.stop_table is not None:
                            in_stop_table = self.stop_table.in_table(hash.lower())
                
                        in_concordance_table = self.concordance_table.in_table(hash.lower())

                        if not in_concordance_table and not in_stop_table:
                            self.concordance_table.insert(hash, [i+1])

                        elif in_concordance_table and not in_stop_table:
                            concordance_index = self.concordance_table.get_index(hash.lower())
                            if concordance_index is not None:
                                self.concordance_table.hash_table[concordance_index][1].append(i+1)

        except:
            raise FileNotFoundError

    def write_concordance(self, filename: str) -> None:
        """ Write the concordance entries to the output file(filename)
        See sample output files for format. """

        ordered_cord = []

        for cord in self.concordance_table.hash_table:
            if cord is not None:
                ordered_cord.append(cord)
        
        ordered_cord.sort(key=lambda x: x[0])

        with open(filename, "w") as txt_file:
            
            for output in ordered_cord:
                txt_file.write(output[0] + ": " + " ".join([str(num) for num in output[1]])+"\n")
