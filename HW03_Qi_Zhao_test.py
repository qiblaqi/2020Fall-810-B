"""
This is HW03 unittest scripts. Written By Qi Zhao. Testing the following methods: __add__(), __sub__(), __mul__(), __truediv__(), __eq__().
and __ne__(self, other: "Fraction"): not equal __lt__(self, other: "Fraction"): less than __le__(self, other: "Fraction"): less than or equal to __gt__(self, other: "Fraction"): greater than __ge__(self, other: "Fraction"):
"""
import unittest

from HW03_Qi_Zhao import Fraction

class TestHW03(unittest.TestCase):
    def test_suite_hw02(self) -> None:
        """ imported test cases from HW02 test suite to test basic + - / * functions"""
        f12: Fraction = Fraction(1, 2)
        f44: Fraction = Fraction(4, 4)
        f128: Fraction = Fraction(12, 8)
        f32: Fraction = Fraction(3, 2)
        self.assertEqual(str(f12+f12),"4/4")
        self.assertEqual(str(f44-f12),"4/8")
        self.assertEqual(str(f12+f44),"12/8")
        self.assertEqual(str(f12/f32),"2/6")
        self.assertEqual(str(f12*f128),"12/16")
        self.assertEqual(str(f128==f32),"True")
        self.assertEqual(str(f12+f44+f128),"192/64")
    
    def test_not_equal(self) -> None:
        """ test not equal function from HW03 with 0/3!=1/3 is true; 1/12 != 3/36 is false, 0/12 != 0/36 is false"""
        self.assertTrue(Fraction(0,3) != Fraction(1,3))
        self.assertFalse(Fraction(1, 12) != Fraction(3, 36))
        self.assertFalse(Fraction(0, 12) != Fraction(0, 36))
    
    def test_less_than(self) -> None:
        """ test less than function from HW03 with 0/3<1/3 is true and 1/12 < 3/36 is false 0/12 < 0/36 is false """
        self.assertTrue(Fraction(0,3) < Fraction(1,3))
        self.assertFalse(Fraction(1, 12) < Fraction(3, 36))
        self.assertFalse(Fraction(0, 12) < Fraction(0, 36))
        
    def test_less_than_or_equal(self) -> None:
        """ test less than equal to function from HW03 with 0/3 <= 1/3 is true 1/12 <= 3/36 is true and 1/12 <= 0/36 is false """
        self.assertTrue(Fraction(0,3) <= Fraction(1,3))
        self.assertTrue(Fraction(1, 12) <= Fraction(3, 36))
        self.assertFalse(Fraction(1, 12) <= Fraction(0, 36))
    
    def test_greater_than(self) -> None:
        """ test greater than function with 0/3>1/3 is false and 1/12 > 3/36 is false and 1/12 > 0/36 is true """
        self.assertFalse(Fraction(0,3) > Fraction(1,3))
        self.assertFalse(Fraction(1, 12) > Fraction(3, 36))
        self.assertTrue(Fraction(1, 12) > Fraction(0, 36))
    
    def test_greater_than_or_equal(self) -> None:
        """ test greater than or equal to function with 0/3 >= 1/3 is false and 1/12 >= 3/36 is true 1/12 >= 0/36 is true """
        self.assertFalse(Fraction(0,3) >= Fraction(1,3))
        self.assertTrue(Fraction(1, 12) >= Fraction(3, 36))
        self.assertTrue(Fraction(1, 12) > Fraction(0, 36))
    
    def test_combine_calculation(self) -> None:
        """ test combination calculation between + - / * == != < <= > >= with 1/4+2/4 == 3/4, 0/2-0/2 != 2/2, 1/4 / 3/4 >= 1/5 """
        self.assertTrue(Fraction(1, 4)+Fraction(2, 4)==Fraction(3, 4))
        self.assertTrue(Fraction(0, 2)-Fraction(0, 2)!=Fraction(2, 2))
        self.assertTrue(Fraction(1, 4)/Fraction(3, 4)>=Fraction(1, 5))
        self.assertFalse(Fraction(1, 4)*Fraction(3, 4)<=Fraction(1, 25))
        
    def test_error_handling(self) -> None:
        """ test init Function and divide Function which can raise errors like ValueError or ZeroDivisionErrors """
        with self.assertRaises(ValueError):
            Fraction(2, 0) # it should raise a valueError as the denominator is 0
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 3)/Fraction(0, 3) # it should raise a ZeroDivisionError as Fraction B's value is 0
        
if __name__ == '__main__':
    unittest.main()