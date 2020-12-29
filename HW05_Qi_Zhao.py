"""
This is HW05 Written By Qi Zhao. This file contains following functions: reverse(s), substring(target: str, s: str),
find_second(target: str, string: str)
"""
from typing import Iterator, IO

def reverse(s: str) -> str:
    """ this function reverse the given string s and return the new reversed one.
    """ 
    if s.__len__ == 0:
        return s
    new_s: str = ""
    for index in range(len(s)-1, -1, -1):
        new_s += s[index]
    return new_s

def substring(target: str, s: str) -> int:
    """ this function find the target substring in the s string and return the index of the substring location.
        return -1 if the target is not in the substring s
    """
    if target == "":
        return 0
    if s == "" and target != "":
        return -1
    for index in range(0, len(s), len(target)):
        if target == s[index: index+len(target)]:
            return index
    return -1

def find_second(target: str, string: str) -> int:
    """ this function find the second occurrence of target in the string.
        return -1 if the target is not in the sub string
    """
    return string.find(target, string.find(target)+1)

def get_lines(path: str) -> Iterator[int]:
    """ opens a file from path for reading and returns one line from the file at a time.
        would raise a FileNotFound exception if the file can't be opened for reading. 
    """
    try:
        fp:IO = open(path,'r')
    except FileNotFoundError:
        raise
    else:
        with fp:
            my_line:str = ""
            for line in fp.readlines():
                my_line += line[:-1]
                if  my_line.startswith("<"):
                    if my_line.find(">")!=-1:
                        yield my_line[0:my_line.find(">")+1]
                        my_line = ""
                    elif my_line.endswith("\\"):
                        my_line = my_line[:-1]
                        continue
                else :
                    my_line = ""
                    continue            