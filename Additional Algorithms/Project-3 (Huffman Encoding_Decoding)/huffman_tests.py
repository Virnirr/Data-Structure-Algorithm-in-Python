import unittest
from huffman import *

class TestList(unittest.TestCase):
    def test_cnt_freq(self) -> None:
        freqlist = cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0]
        self.assertListEqual(freqlist[97:104], anslist)
    
    def test_simple_create_huff_tree(self) -> None:
        none_tree = create_huff_tree(cnt_freq("test_none_file.txt"))
        one_tree = create_huff_tree(cnt_freq("test_single_file.txt"))
        self.assertEqual(none_tree, None)
        if one_tree is not None:
            self.assertEqual(one_tree.char_ascii, 97)
        if one_tree is not None:
            self.assertEqual(one_tree.freq, 5)

    def test_simple_create_header(self) -> None:
        none_tree = create_header(cnt_freq("test_none_file.txt"))
        self.assertEqual(none_tree, "")

        with self.assertRaises(FileNotFoundError):
            cnt_freq("No_file.txt")

    def test_combine(self) -> None:
        a = HuffmanNode(65, 1)
        b = HuffmanNode(66, 2)
        c = combine(a, b)
        if (c.left is not None) and (c.right is not None):
            self.assertEqual(c.left.char_ascii,65)
            self.assertEqual(c.left.freq, 1)
            self.assertEqual(c.right.char_ascii, 66)
            self.assertEqual(c.right.freq, 2)
            self.assertEqual(c.char_ascii, 65)
            self.assertEqual(c.freq, 3)
        else:   # pragma: no cover
            self.fail()
        c = combine(b, a)
        if (c.left is not None) and (c.right is not None):
            self.assertEqual(c.left.char_ascii,65)
            self.assertEqual(c.left.freq, 1)
            self.assertEqual(c.right.char_ascii, 66)
            self.assertEqual(c.right.freq, 2)
            self.assertEqual(c.char_ascii, 65)
            self.assertEqual(c.freq, 3)
        else:   # pragma: no cover
            self.fail()

    def test_create_huff_tree(self) -> None:
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        if hufftree is not None:
            self.assertEqual(hufftree.freq, 32)
            self.assertEqual(hufftree.char_ascii, 97)
            left = hufftree.left
            right = hufftree.right
            if (left is not None) and (right is not None):
                self.assertEqual(left.freq, 16)
                self.assertEqual(left.char_ascii, 97)
                self.assertEqual(right.freq, 16)
                self.assertEqual(right.char_ascii, 100)
            else: # pragma: no cover
                self.fail()
        else: # pragma: no cover
            self.fail()

    def test_create_header(self) -> None:
        freqlist = cnt_freq("file2.txt")
        self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2")

    def test_create_code(self) -> None:
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('d')], '1')
        self.assertEqual(codes[ord('a')], '0000')
        self.assertEqual(codes[ord('f')], '0001')

    def test_01_textfile(self) -> None:
        huffman_encode("file1.txt", "file1_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("file1_out.txt", "file1_soln.txt"))

    def test_02_textfile(self) -> None:
        huffman_encode("file2.txt", "file2_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("file2_out.txt", "file2_soln.txt"))

    def test_03_textfile(self) -> None:
        huffman_encode("declaration.txt", "declaration_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("declaration_out.txt", "declaration_soln.txt"))

    def test_04_textfile(self) -> None:
        huffman_encode("multiline.txt", "multiline_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("multiline_out.txt", "multiline_soln.txt"))

    def test_05_textfile(self) -> None:
        with self.assertRaises(FileNotFoundError):
            huffman_encode("checker.txt", "checker_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        with self.assertRaises(FileNotFoundError):
            compare_files("checker.txt", "checker.txt")

    def test_06_textfile(self) -> None:
        huffman_encode("test_single_file.txt", "test_single_file_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("test_single_file_out.txt", "test_single_file_soln.txt"))

    def test_07_textfile(self) -> None:
        huffman_encode("test_none_file.txt", "test_none_file_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("test_none_file_out.txt", "test_none_file_soln.txt"))

    # huffman_tests_partb.py
    def test_parse_header(self) -> None:
      header = "97 2 98 4 99 8 100 16 102 2"
      freqlist = parse_header(header)
      anslist = [0]*256
      anslist[97:104] = [2, 4, 8, 16, 0, 2, 0] 
      self.assertListEqual(freqlist[97:104], anslist[97:104])

    def test_decode_01(self) -> None:
      huffman_decode("file1_soln.txt", "file1_decode.txt")
      # detect errors by comparing your encoded file with a *known* solution file
      self.assertTrue(compare_files("file1.txt", "file1_decode.txt"))

    def test_decode_02(self) -> None:
      huffman_decode("declaration_soln.txt", "declaration_decode.txt")
      # detect errors by comparing your encoded file with a *known* solution file
      self.assertTrue(compare_files("declaration.txt", "declaration_decode.txt"))
      
    def test_decode_03(self) -> None:
        with self.assertRaises(FileNotFoundError):
            huffman_decode("checker.txt", "checker_out.txt")

    def test_decode_04(self) -> None:
        huffman_decode("test_single_file_soln.txt", "test_single_decode_file.txt")
        # detect errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("test_single_file.txt", "test_single_decode_file.txt"))

    def test_decode_05(self) -> None:
        huffman_decode("test_none_file_soln.txt", "test_non_decode_file.txt")
        # detect errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("test_none_file.txt", "test_none_decode_file.txt"))
        
# Compare files - takes care of CR/LF, LF issues
def compare_files(file1: str, file2: str) -> bool: # pragma: no cover
    match = True
    done = False
    with open(file1, "r") as f1:
        with open(file2, "r") as f2:
            while not done:
                line1 = f1.readline().strip()
                line2 = f2.readline().strip()
                if line1 == '' and line2 == '':
                    done = True
                if line1 != line2:
                    done = True
                    match = False
    return match


if __name__ == '__main__':
    unittest.main()