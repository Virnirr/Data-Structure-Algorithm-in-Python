# Start of unittest - add to completely test functions in exp_eval!

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):

    def test_postfix_eval_01a(self) -> None:
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    def test_postfix_eval_01b(self) -> None:
        self.assertAlmostEqual(postfix_eval("8 1 >>"), 4)
        self.assertAlmostEqual(postfix_eval("8 1 <<"), 16)

    def test_postfix_eval_01c(self) -> None:
        self.assertAlmostEqual(postfix_eval("8 2 **"), 64)

    def test_postfix_eval_01d(self) -> None:
        self.assertAlmostEqual(postfix_eval("18.5 -2 *"), -37)
        self.assertAlmostEqual(postfix_eval("-18.52 -0.78 +"), -19.3)

    def test_postfix_eval_01e(self) -> None:
        self.assertAlmostEqual(postfix_eval("5 4 2 / +"), 7)

    def test_postfix_eval_01f(self) -> None:
        self.assertAlmostEqual(postfix_eval("5 1 2 + 4 ** + 3 -"), 83)
    
    def test_postfix_eval_01g(self) -> None:
        self.assertAlmostEqual(postfix_eval("10 5 // 2 5 * +"), 12)

    def test_postfix_eval_01h(self) -> None:
        self.assertAlmostEqual(postfix_eval("25"), 25)

    def test_postfix_eval_02(self) -> None:
        try:
            postfix_eval("blah")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03a(self) -> None:
        try:
            postfix_eval("4 +")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_03b(self) -> None:
        try:
            postfix_eval("")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self) -> None:
        try:
            postfix_eval("1 2 3 +")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_postfix_eval_05_a(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            self.assertEqual(postfix_eval("0 0 /"), 0)

    def test_postfix_eval_05_b(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            self.assertEqual(postfix_eval("0 0 //"), 0)
    
    def test_postfix_eval_06(self) -> None:
        try:
            postfix_eval("4 5")
            self.fail()      # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_postfix_eval_07(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            self.assertAlmostEqual(postfix_eval("12 1.2 * 10 10 - / 6 - 3.7 ** 2 / 5 / 3 - 23 + 1.1 / 2.2 + 2.4 5 / - 1 - 1.6 10 / 9 / 2.8 * 3 - 6.2 4 / 12.8 2 * 1.1 / 4.4 3.2 1.1 5.2 / 9.9 * - / - + - + -2 +"), 16)
    
    def test_postfix_eval_08_a(self) -> None:
        try:
            postfix_eval("8.80 1.1 >>")
            self.fail()      # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")
    
    def test_postfix_eval_08_b(self) -> None:
        try:
            postfix_eval("8.80 1.1 <<")
            self.fail()      # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    def test_infix_to_postfix_01a(self) -> None:
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")
        self.assertEqual(infix_to_postfix("32 >> 2 >> 1"), "32 2 >> 1 >>")

    def test_infix_to_postfix_01b(self) -> None:
        self.assertEqual(infix_to_postfix("32 >> 2 << 1"), "32 2 >> 1 <<")

    def test_infix_to_postfix_01c(self) -> None:
        self.assertEqual(infix_to_postfix("3 ** 2 ** 2"), "3 2 2 ** **")

    def test_infix_to_postfix_02(self) -> None:
        self.assertEqual(infix_to_postfix("( 5 - 3 ) * 4"), "5 3 - 4 *")
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3"), "3 4 2 * 1 5 - 2 3 ** ** / +")

    def test_infix_to_postfix_03(self) -> None:
        self.assertEqual(infix_to_postfix("70 - -3 * 10"), "70 -3 10 * -")

    def test_infix_to_postfix_04(self) -> None:
        self.assertEqual(infix_to_postfix("70.52 - 3.5 * 10.05"), "70.52 3.5 10.05 * -")

    def test_infix_to_postfix_05(self) -> None:
        self.assertEqual(infix_to_postfix("-70.52 - 3.5 * 10.05"), "-70.52 3.5 10.05 * -")

    def test_infix_to_postfix_06(self) -> None:
        try:
            infix_to_postfix("70.52 - 3.5 * 10.05 $")
            self.fail()      # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_infix_to_postfix_breakmulti(self) -> None:
        self.assertEqual(infix_to_postfix('3 * 4 ** 5 + 6'), '3 4 5 ** * 6 +')

    def test_prefix_to_postfix(self) -> None:
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")

    def test_prefix_to_postfix_02(self) -> None:
        try:
            prefix_to_postfix("$ - 3 / 2 1 - / 4 5 6")
            self.fail()      # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

if __name__ == "__main__":
    unittest.main()
