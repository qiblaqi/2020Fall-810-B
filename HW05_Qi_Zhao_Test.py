"""
This is HW05 unittest scripts. Written By Qi Zhao. Testing the following methods: reverse(s), 
substring(target: str, s: str),find_second(target: str, string: str)

"""
import unittest

from HW05_Qi_Zhao import *

class TestHW05(unittest.TestCase):
    def test_reverse(self) -> None:
        self.assertEqual(reverse("abc"), "abc"[::-1])
        self.assertEqual(reverse(""), ""[::-1])
        self.assertEqual(reverse(" "), " "[::-1])

    def test_substring(self) -> None: 
        self.assertEqual(substring("abc", "Hello abc!"), 6)
        self.assertEqual(substring("abcd", "Hello abc!"), -1)
        self.assertEqual(substring("", ""), 0)
        self.assertEqual(substring("", " "), 0)
        self.assertEqual(substring(" ", ""), -1)
        
    def test_find_second(self) -> None:
        self.assertEqual(find_second('iss', 'Mississppi'), 4)
        self.assertEqual(find_second('abba', 'abbabba'), 3)
        self.assertEqual(find_second(" ", "   "), 1)
        self.assertEqual(find_second('',''), -1)
        self.assertEqual(find_second("abcd", "Hello abc!"), -1)

if __name__ == '__main__':
    unittest.main()