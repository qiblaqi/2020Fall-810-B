"""
This is HW07 Written By Qi Zhao. This file contains following functions: anagrams_lst(str1, str2), 
anagrams_dd(str1, str2), anagrams_cntr(str1: str, str2: str) -> bool, 
covers_alphabet(sentence: str) -> bool, web_analyzer(weblogs: List[Tuple[str, str]]) -> List[Tuple[str, List[str]]]
"""
from typing import List, Tuple, DefaultDict, Counter, Set
from collections import defaultdict, Counter

def anagrams_lst(str1: str, str2: str) -> bool:
    """ Implement (including automated unit tests) a function anagrams_lst(str1, str2)
        that returns True if str1 and str2 are anagrams, False if not.
    """
    return True if (sorted(list(str1)) == sorted(list(str2))) else False

def anagrams_dd(str1: str, str2: str) -> bool:
    """ anagrams_dd(str1, str2) that returns True if str1 and str2 are anagrams, False if not.
        with defaultdict implementation
    """
    dd:DefaultDict[str, int] = defaultdict(int)
    for ch in str1:
        dd[ch] += 1
    for ch in str2:
        dd[ch] -= 1
    for key, value in dd.items():
        if value == 0:
            continue
        else:
            return False
    return True

def anagrams_cntr(str1: str, str2: str) -> bool:
    """ anagrams_dd(str1, str2) that returns True if str1 and str2 are anagrams, False if not.
        with Counter implementation
    """
    c: Counter[str] = Counter(str1)
    for ch in str2:
        c[ch] -= 1
    for key, value in c.items():
        if value == 0:
            continue
        else:
            return False
    return True

def covers_alphabet(sentence: str) -> bool:
    """ covers_alphabet(sentence) that returns True if sentence includes at least one instance of 
        every character in the alphabet or False 
        using only Python sets.
    """
    alphabet: Set = set("abcdefghijklmnopqrstuvwxyz")
    if alphabet.issubset(set(sentence.lower())):
        return True
    else:
        return False
    
def web_analyzer(weblogs: List[Tuple[str, str]]) -> List[Tuple[str, List[str]]]:
    """ web_analyzer(weblogs),  along with automated tests, to create a summary of the weblogs with 
        each distinct site and a sorted list of names of distinct people who visited that site.
    """
    summary: DefaultDict[str, set] = defaultdict(set)
    for name, website in weblogs:
        summary[website].add(name)
    return [ (web,sorted(list(summary[web]))) for web in sorted(list(summary.keys())) ]