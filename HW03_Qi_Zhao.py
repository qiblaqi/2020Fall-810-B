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
    __slots__ = ['numerator', 'denominator'] #predefine Fraction attributes
    
    def __init__(self, numerator: float, denominator: float) -> None:
        """ initialize the class and assign the value to each attributes """
        self.numerator = numerator
        if denominator == 0:
            raise ValueError("The denominator cant be zero!")
        else:
            self.denominator = denominator
    
    def __add__(self, other: "Fraction") -> "Fraction":
        """ add two fractions and return the result as a Fraction instance 
            e.g: A.plus(B) = A+B
        """
        result_numerator: float = self.numerator*other.denominator + other.numerator*self.denominator #define the result's numerator
        result_denominator: float = self.denominator*other.denominator #define the result's denominator
        return Fraction(result_numerator, result_denominator) #return the result
    
    def __sub__(self, other: "Fraction") -> "Fraction":
        """ do minus calculation within two Fractions and return the value as a Fraction instance.
            e.g: A.minus(B) = A-B  
        """
        result_numerator: float = self.numerator*other.denominator - other.numerator*self.denominator
        result_denominator: float = self.denominator*other.denominator
        return Fraction(result_numerator, result_denominator)
    
    def __mul__(self, other: "Fraction") -> "Fraction":
        """ do multiply calculation within two Fractions and return the multiplied value as a Fraction instance.
            e.g: A.times(B) = A*B 
        """
        result_numerator: float = self.numerator*other.numerator
        result_denominator: float = self.denominator*other.denominator
        return Fraction(result_numerator, result_denominator)
    
    def __truediv__(self, other: "Fraction") -> "Fraction":
        """ do divide calculation within two Fractions and return the divided value as a Fraction instance.
            e.g: A.divide(B) = A/B 
        """
        if other.numerator == 0:
            raise ZeroDivisionError("Can't divide by 0!")
        result_numerator: float = self.numerator*other.denominator
        result_denominator: float = self.denominator*other.numerator
        return Fraction(result_numerator, result_denominator)
    
    def __eq__(self, other: "Fraction") -> bool:
        """ Return true if two Fraction instances have the same value.
            using the Class Function self.minus() to identify if two instances are the same.
            If they have the same value, then A.minus(B) equals to '0', which also means the numerator of the result is 0.
        """
        if (self-other).numerator == 0: # if two Fractions equal, the numerator of the minus result should be zero
            return True
        else:
            return False
    
    def __str__(self) -> str:
        """ Magic Function of Class Fraction!
            if any Fraction instances are required to convert to string types. Return the mathmatical description of the Fraction.
            e.g: f12 is a Fraction instance. str(f12) = '1/2'
        """
        return f"{int(self.numerator)}/{int(self.denominator)}"
    
    def __ne__(self, other: "Fraction") -> bool:
        """ Return true if two Fraction instances dont have the same value.
            using the Class Function '==' if A!=B then return True. Otherwise return False.
        """
        return not(self==other)
    
    def __lt__(self, other: "Fraction") -> bool:
        """ Return true if Fraction A (self) instance is less than Fraction B (other).
            using the Class Function '-' if A<B then (A-B).numerator is less than 0 then return True
            Otherwise (A-B).numerator is greater or equal to 0 return False.
        """
        if (self-other).numerator < 0:
            return True
        else:
            return False
        
    def __le__(self, other: "Fraction") -> bool:
        """ Return true if Fraction A (self) instance is less than or equal to Fraction B (other).
            using the Class Function '-' if A<B then (A-B).numerator is less than or equal to 0 then return True
            Otherwise (A-B).numerator is greater than 0 return False.
        """
        if (self-other).numerator <= 0:
            return True
        else:
            return False
        
    def __gt__(self, other: "Fraction") -> bool:
        """ Return true if Fraction A (self) instance is greater than Fraction B (other).
            using the Class Function '<=' if A>B then (A<=B) is False then return True
            Otherwise return False.
        """
        return not(self<=other)
    
    def __ge__(self, other: "Fraction") -> bool:
        """ Return true if Fraction A (self) instance is greater or equal to Fraction B (other).
            using the Class Function '<' if A>=B then (A<B) is False then return True
            Otherwise return False.
        """
        return not(self<other)