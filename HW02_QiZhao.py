"""
This is HW03 Written By Qi Zhao. Write a Fraction class to represent Fraction calculation. Functions as plus minus
multiply divide and equal.
"""
from typing import Dict

class Fraction:
    """ Fraction class. In each Fraction class there will be attributes as: numerator and denominator 
        Class Functions as: plus, minus, times, divide, equal.
        Also include two special functions as __str__ and get_operator_and_result:
            The first function is to convert a Fraction instance to a string type.
            The second function is to get the operation name from a operator string and return the execution result.
    """
    __slot__ = ['numerator', 'denominator'] #predefine Fraction attributes
    
    def __init__(self, numerator: float, denominator: float) -> None:
        """ initialize the class and assign the value to each attributes """
        self.numerator = numerator
        self.denominator = denominator
    
    def plus(self, other: "Fraction") -> "Fraction":
        """ add two fractions and return the result as a Fraction instance 
            e.g: A.plus(B) = A+B
        """
        result_numerator: float = self.numerator*other.denominator + other.numerator*self.denominator #define the result's numerator
        result_denominator: float = self.denominator*other.denominator #define the result's denominator
        return Fraction(result_numerator, result_denominator) #return the result
    
    def minus(self, other: "Fraction") -> "Fraction":
        """ do minus calculation within two Fractions and return the value as a Fraction instance.
            e.g: A.minus(B) = A-B  
        """
        result_numerator: float = self.numerator*other.denominator - other.numerator*self.denominator
        result_denominator: float = self.denominator*other.denominator
        return Fraction(result_numerator, result_denominator)
    
    def times(self, other: "Fraction") -> "Fraction":
        """ do multiply calculation within two Fractions and return the multiplied value as a Fraction instance.
            e.g: A.times(B) = A*B 
        """
        result_numerator: float = self.numerator*other.numerator
        result_denominator: float = self.denominator*other.denominator
        return Fraction(result_numerator, result_denominator)
    
    def divide(self, other: "Fraction") -> "Fraction":
        """ do divide calculation within two Fractions and return the divided value as a Fraction instance.
            e.g: A.divide(B) = A/B 
        """
        result_numerator: float = self.numerator*other.denominator
        result_denominator: float = self.denominator*other.numerator
        return Fraction(result_numerator, result_denominator)
    
    def equal(self, other: "Fraction") -> bool:
        """ Return true if two Fraction instances have the same value.
            using the Class Function self.minus() to identify if two instances are the same.
            If they have the same value, then A.minus(B) equals to '0', which also means the numerator of the result is 0.
        """
        if self.minus(other).numerator == 0: # if two Fractions equal, the numerator of the minus result should be zero
            return True
        else:
            return False
    
    def __str__(self) -> str:
        """ Magic Function of Class Fraction!
            if any Fraction instances are required to convert to string types. Return the mathmatical description of the Fraction.
            e.g: f12 is a Fraction instance. str(f12) = '1/2'
        """
        return f"{int(self.numerator)}/{int(self.denominator)}"
    
    def get_operator_and_result(self, myop: str, other: "Fraction") -> "Fraction":
        """ get the operation sign from the user and then allocate to the specific function. Return the specific function that user wants.
            e.g: user input '+' 
                 return A+B
        """
        mydict: Dict = {'+':self.plus, '-':self.minus, '*':self.times, '==':self.equal} # define a operator reallocator map for assign the function name with the operator sign
        return mydict[myop](other) # execute the opeartion with the other Fraction
    
def test_suite() -> None:
    """ Some test cases of the Class Fraction. There are four test cases in this function.
    """
    f12: Fraction = Fraction(1, 2)
    f44: Fraction = Fraction(4, 4)
    f128: Fraction = Fraction(12, 8)
    f32: Fraction = Fraction(3, 2)
    print("-------- The test starts from here -----------")
    print(f"{f12} + {f12} = {f12.plus(f12)} [4/4]")
    print(f"{f44} - {f12} = {f44.minus(f12)} [4/8]")
    print(f"{f12} + {f44} = {f12.plus(f44)} [12/8]")
    print(f"{f12} / {f32} = {f12.divide(f32)} [2/6]")
    print(f"{f12} * {f128} = {f12.times(f128)} [12/16]")
    print(f"{f128} == {f32} is {f128.equal(f32)} [True]")
    print(f"{f12} + {f44} + {f128} = {f12.plus(f44).plus(f128)} [192/64]")
    print("-------------- The test ends -----------------")

def get_usr_fraction(myid: int) -> "Fraction":
    """ get the user's 'id'th fraction number instances.
        e.g: get_usr_fraction(1) = get Fraction 1 from user.
    """
    frac_numerator: float = float(input(f"Fraction {myid} numerator:"))
    frac_denominator: float = float(input(f"Fraction {myid} denominator:"))
    return Fraction(frac_numerator, frac_denominator)

def get_usr_operator() -> str:
    """ get user's operator sign. available sign is + - * / == 
        if invaild input detects ask user to input the operator again.
    """
    my_operator: str = input("Operation (+, -, *, /, ==):")
    if my_operator in ['+', '-', '*', '/', '==']:
        return my_operator
    else:
        print("Invalid Operator sign! Please select an operator from +, -, *, /, == ")
        return get_usr_operator()
    
def main() -> None:
    """ define the main function. First to ask user to input the Fraction 1's numerator and denominator and 
        then ask the operation symbol to define the operation. Then ask user to input the Fraction 2's numerator and denominator.
        Finally print the result.
    """
    frac_1: "Fraction" = get_usr_fraction(1) # get Fraction 1
    operator: str = get_usr_operator() # get Operator 
    frac_2: "Fraction" = get_usr_fraction(2) # get Fraction 2
    frac_result: "Fraction" = frac_1.get_operator_and_result(operator, frac_2) # execute the calculation and get result
    print(f"{frac_1} {operator} {frac_2} = {frac_result}") # print the result
    
if __name__ == '__main__':
    test_suite()
    main()