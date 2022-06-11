from __future__ import annotations
from typing import List, Optional

class HuffmanNode:
    def __init__(self, char_ascii: int, freq: int, left: Optional[HuffmanNode] = None, right: Optional[HuffmanNode] = None):
        self.char_ascii = char_ascii    # stored as an integer - the ASCII character code value
        self.freq = freq                # the frequency associated with the node
        self.left = left                # Huffman tree (node) to the left!
        self.right = right              # Huffman tree (node) to the right


    # method used by class to know how to sort it, which uses the comes_before function
    def __lt__(self, other: HuffmanNode) -> bool:
        return comes_before(self, other)

def comes_before(a: HuffmanNode, b: HuffmanNode) -> bool:
    """Returns True if tree rooted at node a comes before tree rooted at node b, False otherwise"""

    # check if the frequency in a is greater than b
    if a.freq < b.freq:
        return True
    
    # else if the frequency are equal, check their ascii value
    elif a.freq == b.freq and a.char_ascii < b.char_ascii:
        return True

    return False

def combine(a: HuffmanNode, b: HuffmanNode) -> HuffmanNode:
    """Creates a new Huffman node with children a and b, with the "lesser node" on the left
    The new node's frequency value will be the sum of the a and b frequencies
    The new node's char value will be the lower of the a and b char ASCII values"""
    if a.freq > b.freq:
         new_HuffmanNode = HuffmanNode(min([a.char_ascii,b.char_ascii]), sum([a.freq, b.freq]), b, a)

    elif a.freq < b.freq:
        new_HuffmanNode = HuffmanNode(min([a.char_ascii,b.char_ascii]), sum([a.freq, b.freq]), a, b)
    
    else:
        new_HuffmanNode = HuffmanNode(min([a.char_ascii,b.char_ascii]), sum([a.freq, b.freq]), a, b)
    
    return new_HuffmanNode

def cnt_freq(filename: str) -> List:
    """Opens a text file with a given file name (passed as a string) and counts the
    frequency of occurrences of all the characters within that file
    Returns a Python List with 256 entries - counts are initialized to zero.
    The ASCII value of the characters are used to index into this list for the frequency counts"""

    occur = [0] * 256
    try:
        # read file and add 1 to any ASCII index when letter is found
        with open(filename, "rt") as txt_file:

            # read the text and add one to the index of the ASCII value when it appears
            txt = txt_file.read()
            for letter in txt:
                occur[ord(letter)] += 1
    except:
        raise FileNotFoundError

    return occur

def create_huff_tree(char_freq: List) -> Optional[HuffmanNode]:
    """Input is the list of frequencies (provided by cnt_freq()).
    Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree. Returns None if all counts are zero."""

    # if the counts are all zero, return None
    if max(char_freq) == 0:
        return None

    tree_list = []

    # building a list of HuffmanNode
    for i in range(256):
        if char_freq[i] != 0:
            tree_list.append(HuffmanNode(i, char_freq[i]))
    
    # check if the tree_list only has one non-zero value
    if len(tree_list) == 1:
        return tree_list[0]

    tree_list.sort()

    # combine and insert back the first two huffmannode of the sorted list
    while len(tree_list) >= 2:
        tree_list.append(combine(tree_list.pop(0), tree_list.pop(0)))
        tree_list.sort()

    return tree_list[0]

def create_code(node: Optional[HuffmanNode]) -> List:
    """Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation
    as the index into the array, with the resulting Huffman code for that character stored at that location.
    Characters that are unused should have an empty string at that location"""

    huff_list = [""] * 256

    _create_code(node, huff_list, "")

    return huff_list

def _create_code(node: Optional[HuffmanNode], huff_list: list, huff_str: str) -> None:
    '''Helper function for recursively creating huffman code of each character.
    Similar concept to inorder_list and preorder_list from lab5 (binary search tree)'''

    if node is not None:
        if node.left is None and node.right is None:
            huff_list[node.char_ascii] = huff_str
            return None

        _create_code(node.left, huff_list, huff_str + "0")
        _create_code(node.right, huff_list, huff_str + "1")


def create_header(freqs: List) -> str:
    """Input is the list of frequencies (provided by cnt_freq()).
    Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” """

    header_str = []

    if max(freqs) == 0:
        return ""
    
    for i in range(len(freqs)):
        if freqs[i] != 0:
            header_str.append(str(i))
            header_str.append(str(freqs[i]))
    
    return " ".join(header_str)

def huffman_encode(in_file: str, out_file: str) -> None:
    """Takes inout file name and output file name as parameters
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Take not of special cases - empty file and file with only one unique character"""

    try:
        with open(in_file, "r") as txt_file:
            # get frequency of the file of each character
            huff_man_char = cnt_freq(in_file)
            # create a huffman tree of the frequency of each character
            huff_man_tree = create_huff_tree(huff_man_char)
            # create header for the frequency
            huff_man_header = create_header(huff_man_char)
            # create combination of 0 and 1 of each respected characters from the huffman tree
            huff_man_encoded = create_code(huff_man_tree)

            # encode the file, putting it onto a list with code representing the exact huffman node for the character
            huff_encoded_str = []
            txt = txt_file.read()
            for letter in txt:
                huff_encoded_str.append(huff_man_encoded[ord(letter)])
    
    # if file not found
    except:
        raise FileNotFoundError

    with open(out_file, "w", newline='') as f:
        # "w" - write into file
        # "r" - read into file
        # "+" - read and write into file
        # write the header and the encoded onto an out_file
        f.write(huff_man_header)
        f.write("\n")
        f.write("".join(huff_encoded_str))
    
def huffman_decode(encoded_file:str, decode_file:str) -> None:
    '''Read your encoded_file (assuming that the format is correct) and output 
    decoded string format to your decode_file'''
    try:
        with open(encoded_file, "r") as f:
            # read first line of the decoding and make a frequency array/list
            header_line = f.readline()
            de_freq = parse_header(header_line)

            # checks for the number of non-zero frequency in the list
            num_non_zero_freq = len([i for i, e in enumerate(de_freq) if e != 0])

            # create a huffman tree and initialize the decoding output string
            huff_man_tree = create_huff_tree(de_freq)
            output_str = ""

            # if it's only a single string, then only add the character to the output string and the 
            # number of frequency associated with the character
            if num_non_zero_freq == 1 and huff_man_tree is not None:
                output_str = chr(huff_man_tree.char_ascii) * huff_man_tree.freq

            # run this if multiple non-zero frequency was found
            elif num_non_zero_freq > 1 and huff_man_tree is not None:

                # read the binary line (second line in file) assuming the file is in correct format
                binary_line = f.readline()

                # cur huffman tree node to check position of where your huffman node is at
                cur: Optional[HuffmanNode] = huff_man_tree

                for i in binary_line:
                    # if 0, go left
                    if cur is not None and i == "0":
                        cur = cur.left
                    # if 1 go right
                    if cur is not None and i == "1":
                        cur = cur.right
                    # if you get to the leaf node, then add the character to the output_str and go back to root node
                    if cur is not None and cur.left is None and cur.right is None:
                        # add char to output_str which will be appended to the out_file later
                        output_str += chr(cur.char_ascii)
                        # bring back to original tree root
                        cur = huff_man_tree
            # finally write the characters into a new file
            with open(decode_file, "w", newline='') as f:
                f.write(output_str)

    # if file not found
    except:
        raise FileNotFoundError

def parse_header(header_string:str) -> List:
    '''Given a header_string from your file, returns a array/list of frequency with associated
    ASCII values as the index of each frequency in a table of 256 index from 0-255'''

    header_list = header_string.split()
    decode_freq = [0] * 256

    for i in range(len(header_list)):

        if i % 2 != 0:
            header_index = int(header_list[i - 1])
            decode_freq[header_index] += int(header_list[i])

    return decode_freq