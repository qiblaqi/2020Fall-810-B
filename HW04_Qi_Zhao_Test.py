"""
This is HW04 unittest scripts. Written By Qi Zhao. Testing the following methods: count_vowels()

"""
import unittest

from HW04_Qi_Zhao import *

class TestHW03(unittest.TestCase):
    def test_count_vowels(self) -> None:
        self.assertEqual(count_vowels("Happy Holiday!"), 4)
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(count_vowels("ABC"), 1)
    
    def test_count_vowels(self) -> None:
        self.assertEqual(last_occurrence("a", "Bad apple and peach!"), 16)
        self.assertEqual(last_occurrence(" ","Happy Holiday!"), 5)
        self.assertEqual(last_occurrence("a", "Huge Element!"), None)
        
    def test_my_enumerate(self) -> None:
        my_seq_1: str = "Hello world!"
        my_seq_2: list = []
        self.assertEqual(list(my_enumerate(my_seq_1)), list(enumerate(my_seq_1)))
        self.assertEqual(list(my_enumerate(my_seq_2)), list(enumerate(my_seq_2)))
    
    def test_find_target(self) -> None:
        self.assertTrue(find_target(3, 3, 3, 1)==0)
        self.assertTrue(find_target(3, 3, 3, 2)==0)
        with self.assertRaises(ValueError):
            find_target(3, 5, 10, 20)

if __name__ == '__main__':
    unittest.main()