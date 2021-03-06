"""
This is HW08 Written By Qi Zhao. This file contains following functions: date_arithmetic()-> Tuple[datetime, datetime, int]
file_reader(str, int, str, bool) -> Iterator[List[str]], class FileAnalyzer
"""
from typing import List, Tuple, Iterator, Dict
from datetime import datetime, time, timedelta
from prettytable import PrettyTable

def date_arithmetic() -> Tuple[datetime, datetime, int]:
    """ a function date_arithmetic to use Python’s datetime module to answer the following questions:
        What is the date three days after Feb 27, 2020?
        What is the date three days after Feb 27, 2019?
        How many days passed between Feb 1, 2019 and Sept 30, 2019?
    """
    three_days_after_02272020: datetime = datetime(2020,2,27) + timedelta(days=3)
    three_days_after_02272019: datetime = datetime(2019,2,27) + timedelta(days=3)
    days_passed_02012019_09302019: int = (datetime(2019,9,30) - datetime(2019,2,1)).days

    return three_days_after_02272020, three_days_after_02272019, days_passed_02012019_09302019
 
def file_reader(path: str, fields:int, sep=',', header=False) -> Iterator[List[str]]:
    """ file_reader() to read field-separated text files and yield a tuple with all of the values 
        from a single line in the file on each call to next()
    """
    try:
        fp = open(path,'r')
    except FileNotFoundError:
        raise
    with fp:
        line_count: int = 0
        for my_line in fp:
            line_count += 1
            my_line = my_line.strip('\n')
            my_list:list = [ item for item in my_line.split(',') ]
            if len(my_list) != fields:
                raise ValueError(f"{path} has {len(my_list)} fields on line {line_count} but expected {fields}")
            else:
                yield [ item for item in my_line.split(',') ]

class FileAnalyzer:
    """ FileAnalyzer that given a directory name, searches that directory for Python files """
    def __init__(self, directory: str) -> None:
        """ Your docstring should go here for the description of the method."""
        self.directory: str = directory # NOT mandatory!
        self.files_summary: Dict[str, Dict[str, int]] = dict() 

        self.analyze_files() # summerize the python files data

    def analyze_files(self) -> None:
        """ a method that populate the summarized data into self.files_summary"""
        pass # implement your code here

    def pretty_print(self) -> None:
        """ a method that print out the pretty table from the data stored in the self.files_summary."""
        pass # implement your code here