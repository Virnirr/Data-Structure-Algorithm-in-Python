import unittest
import perm_lex

# Starter test cases - write more!

class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex(self) -> None:
        self.assertEqual(perm_lex.perm_gen_lex('ab'),['ab','ba'])

    def test_perm_gen_lex01(self) -> None:
        self.assertEqual(perm_lex.perm_gen_lex(''),[])
    
    def test_perm_gen_lex02(self) -> None:
        self.assertEqual(perm_lex.perm_gen_lex('a'),['a'])
    
    def test_perm_gen_lex03(self) -> None:
        plist = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
        self.assertEqual(perm_lex.perm_gen_lex('abc'), plist)

if __name__ == "__main__":
        unittest.main()
