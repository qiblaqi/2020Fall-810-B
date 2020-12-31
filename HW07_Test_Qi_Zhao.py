"""
This is HW07 unittest scripts. Written By Qi Zhao. Testing the following methods and class: anagrams_lst(str1, str2), 
anagrams_dd(str1, str2), anagrams_cntr(str1: str, str2: str) -> bool, 
covers_alphabet(sentence: str) -> bool, web_analyzer(weblogs: List[Tuple[str, str]]) -> List[Tuple[str, List[str]]]
"""
import unittest

from HW07_Qi_Zhao import *

class HW07Test(unittest.TestCase):
    def test_anagrams_lst(self) -> None:
        self.assertTrue(anagrams_lst("dormitory", "dirtyroom"))
        self.assertTrue(anagrams_lst("iceman", "cinema"))
        self.assertTrue(anagrams_lst("", ""))
        self.assertFalse(anagrams_lst("iceman", "cinemaa"))
        
    def test_anagrams_dd(self) -> None:
        self.assertTrue(anagrams_dd("dormitory", "dirtyroom"))
        self.assertTrue(anagrams_dd("iceman", "cinema"))
        self.assertTrue(anagrams_dd("", ""))
        self.assertFalse(anagrams_dd("iceman", "cinemaa"))
        
    def test_anagrams_cntr(self) -> None:
        self.assertTrue(anagrams_cntr("dormitory", "dirtyroom"))
        self.assertTrue(anagrams_cntr("iceman", "cinema"))
        self.assertTrue(anagrams_cntr("", ""))
        self.assertFalse(anagrams_cntr("iceman", "cinemaa"))
        
    def test_covers_alphabet(self) -> None:
        self.assertTrue(covers_alphabet("AbCdefghiJklomnopqrStuvwxyz"))
        self.assertTrue(covers_alphabet("We promptly judged antique ivory buckles for the next prize"))
        self.assertFalse(covers_alphabet("xyz"))
        self.assertFalse(covers_alphabet(""))
        self.assertTrue(covers_alphabet("abcdefghijklmnopqrstuvwxyz"))
        self.assertTrue(covers_alphabet("aabbcdefghijklmnopqrstuvwxyzzabc"))
        self.assertTrue(covers_alphabet("The quick brown fox jumps over the lazy dog"))
        
    def test_web_analyzer(self) -> None:
        weblogs: List[Tuple[str, str]] = [
            ('Nanda', 'google.com'), ('Maha', 'google.com'), 
            ('Fei', 'python.org'), ('Maha', 'google.com'), 
            ('Fei', 'python.org'), ('Nanda', 'python.org'), 
            ('Fei', 'dzone.com'), ('Nanda', 'google.com'), 
            ('Maha', 'google.com'), ]

        summary: List[Tuple[str, List[str]]] = [
            ('dzone.com', ['Fei']), 
            ('google.com', ['Maha', 'Nanda']), 
            ('python.org', ['Fei', 'Nanda']), ]

        self.assertEqual(web_analyzer(weblogs), summary)
        
if __name__ == '__main__':
    unittest.main()