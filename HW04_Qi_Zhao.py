"""
This is HW04 Written By Qi Zhao. This file contains following functions: count_vowels(seq), last_occurrence(target, sequence), 
my_enumerate(seq),random_integer_generator(minimum: int, maximum: int) -> Iterator[int]
"""
from typing import Any, Iterator, Sequence, Optional, Iterator
from random import randint
def count_vowels(s: str) -> int:
    """ this function counts the vowels in the given 's' string and return the number of it. And this function covert
        all the letters to lower case and count the number with the variable 'count'
    """
    the_vowels: list = ['a', 'e', 'i', 'o', 'u']
    count: int = 0
    for index in range(len(s)):
        if s[index].lower() in the_vowels:
            count += 1
    return count

def last_occurrence(target: Any, sequence: Sequence[Any]) -> Optional[int]:
    """ this function counts the last occurrence of the given target and return the index of the target 
        this function is using range(start, end, step) function to iterate from the end to the start of the given sequence.
        And find the 'first' occurrence in the for loop. Then return the index.
    """
    index: int = 0
    for index in range(len(sequence)-1,-1,-1):
        if target == sequence[index]:
            return index
    return None

def my_enumerate(seq: Sequence[Any]) -> Iterator[Any]:
    """ this function is similar to enumerate(), python's built-in function, which return the offset, object of the given sequence
    """
    index: int = 0
    for item in seq:
        yield index, item
        index += 1
        
def random_integer_generator(minimum: int, maximum: int) -> Iterator[int]:
    """ this function generates a random number of given range, from the minimum to the maximum number.
    """
    while True:
        yield randint(minimum, maximum)
    
def find_target(target: int, min_val: int, max_val: int, max_attemps: int) -> Optional[int]:
    """ this function will find the target by using the r_i_g(), if target was found then return how many times does it call the 
        r_i_g() before it was found and return None if the target isn't found in max_attemps.
    """
    if target < min_val or target > max_val:
        raise ValueError(f"the target is out range of the {min_val} to {max_val}")
    for times in range(max_attemps):
        findings: int = next(random_integer_generator(min_val, max_val))
        if target == findings:
            return times
    return None