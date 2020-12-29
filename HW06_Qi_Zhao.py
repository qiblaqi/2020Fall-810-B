"""
This is HW06 Written By Qi Zhao. This file contains following functions: list_copy(l), list_intersect(l1, l2)
list_difference(l1, l2), remove_vowels(string: str) -> str, check_pwd(password: str) -> bool, 
And The DonutQueue class, reorder(lssss)
"""
from typing import List, Any, Tuple, Optional, DefaultDict
from collections import defaultdict

def list_copy(l: List[Any]) -> List[Any]:
    """ list_copy(l) that takes a list as a parameter and returns a copy of the list 
        using a list comprehension.  
    """
    return [ item for item in l ]

def list_intersect(l1: List[Any], l2: List[Any]) -> List[Any]:
    """ list_intersect(l1, l2) that takes two lists as  parameters and returns a new list 
        with the values that are included in both lists using a list comprehension.  
    """
    return [ item for item in l1 if item in l2]

def list_difference(l1: List[Any], l2: List[Any]) -> List[Any]:
    """ list_difference(l1, l2) that takes two lists as  parameters 
        and returns a new list with the values that are  in l1, but NOT in l2.  
    """
    return [ item for item in l1 if item not in l2 ]

def remove_vowels(string: str) -> str:
    """ remove_vowels(string) that given a string, splits the string on whitespace into words 
        and returns a new string that includes only the words that do NOT begin with vowels.
    """
    return " ".join([ item for item in string.split() if item[0].lower() not in ["a","e","i","o","u"] ])

def check_pwd(password: str) -> bool:
    """ check_pwd(password: str) -> bool that takes a string as a parameter and returns a boolean value.
        The password includes at least two upper case characters
                     includes at least one lower case characters
                     starts with at least one digit
    """
    lower_ch:list = []
    upper_ch:list = []
    for ch in password[1:]:
        if ch.islower():
            lower_ch.append(ch)
        elif ch.isupper():
            upper_ch.append(ch)
    if password[0].isdigit() and len(lower_ch)>=2 and len(upper_ch)>=2:
        return True
    return False

def reorder(l: List[Any]) -> List[Any]:
    """ reorder(l: List[Any]) -> List[Any]  that returns a copy of the argument sorted using a list and the algorithm discussed in class.
    """
    result: List = []
    index: int = 0
    for item in l:
        for index_sort, item_sort in enumerate(result):
            if item <= item_sort:
                index = index_sort
                break
            else:
                if index_sort == len(result)-1:
                    index = index_sort+1
                continue
        result.insert(index, item)
    return result    

class DonutQueue:
    """ DonutQueue class that tracks customers as they arrive at the donut shop.
        Customers are added to the queue so they can be served in the order they arrived 
        with the exception that priority customers are served before non-priority customers
    """ 
    def __init__(self):
        self.customer:DefaultDict[str: bool] = defaultdict()
        self.waiting_queue:List = []
        
    def arrive(self, name: str, vip: bool) -> None:
        """ create customer info List with name and priority label
        """
        self.customer[name]= vip
    
    def waiting(self) -> Optional[str]:
        """ add customer to the waitting queue and wait
        """
        vip_queue:List = []
        queue:List = []
        if len(self.customer) == 0:
            return None
        for name, vip in self.customer.items():
            if vip:
                vip_queue.append(name)
            else:
                queue.append(name)
        vip_queue.extend(queue)
        self.waiting_queue = vip_queue
        return ", ".join(vip_queue)
    
    def next_customer(self) -> Optional[str]:
        """ serve the next customer and return their name
        """
        name:str = ""
        if len(self.customer) == 0:
            return None
        self.waiting()
        name = self.waiting_queue.pop(0)
        self.customer.pop(name)
        return name
        