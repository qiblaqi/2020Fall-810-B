"""
This is HW06 unittest scripts. Written By Qi Zhao. Testing the following methods and class: list_copy(l), list_intersect(l1, l2)
list_difference(l1, l2), remove_vowels(string: str) -> str, check_pwd(password: str) -> bool, 
And The DonutQueue class, reorder(l)
"""
import unittest

from HW06_Qi_Zhao import *

class P1toP5Test(unittest.TestCase):
    def test_list_copy(self) -> None:
        self.assertEqual(list_copy([]), [])
        self.assertEqual([1,2,3], [1,2,3])
        self.assertEqual(list_copy(["a","b","c"]), ["a","b","c"])
        
    def test_list_intersect(self) -> None:
        self.assertEqual(list_intersect([],[]), [])
        self.assertEqual(list_intersect([1,2,3],[2,3,4]), [2,3])
        self.assertEqual(list_intersect(["a","b","c"],["d","b","c"]), ["b","c"])
        self.assertEqual(list_intersect([1, 2, 3], [4, 5, 6]), [])
        
    def test_list_difference(self) -> None:
        self.assertEqual(list_difference([],[]), [])
        self.assertEqual(list_difference([1,2,3],[2,3,4]), [1])
        self.assertEqual(list_difference(["a","b","c"],["d","b","c"]), ["a"])
        self.assertEqual(list_difference([1,2,3],[4,5,6]), [1,2,3])
        
    def test_remove_vowels(self) -> None:
        self.assertTrue(remove_vowels("Amy is my favorite daughter") == "my favorite daughter")
        self.assertTrue(remove_vowels('Jan is my best friend') == "Jan my best friend")
        self.assertTrue(remove_vowels('') == "")
    
    def test_check_pwd(self) -> None:
        self.assertTrue(check_pwd("1abAB"))
        self.assertFalse(check_pwd("1aAB"))
        self.assertFalse(check_pwd("1abB"))
        self.assertFalse(check_pwd("abAB"))
        
    def test_reorder(self) -> None:
        self.assertEqual(reorder([1,5,3,3]), [1,3,3,5])
        self.assertEqual(reorder([1,5,3,3,1,7,2,1]), sorted([1,5,3,3,1,7,2,1]))
        
        
class DonutQueueTest(unittest.TestCase):
    def test_queue(self):
        dq = DonutQueue()
        self.assertIsNone(dq.next_customer())
        dq.arrive("Sujit", False)
        dq.arrive("Fei", False)
        dq.arrive("Prof JR", True)
        self.assertEqual(dq.waiting(), "Prof JR, Sujit, Fei")
        dq.arrive("Nanda", True)
        self.assertEqual(dq.waiting(), "Prof JR, Nanda, Sujit, Fei")
        self.assertEqual(dq.next_customer(), "Prof JR")
        self.assertEqual(dq.next_customer(), "Nanda")
        self.assertEqual(dq.next_customer(), "Sujit")
        self.assertEqual(dq.waiting(), "Fei")
        self.assertEqual(dq.next_customer(), "Fei")
        self.assertIsNone(dq.next_customer())

if __name__ == '__main__':
    unittest.main()