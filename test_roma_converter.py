import unittest
from roma_conventer import RomanNumeralConverter
class RomanNumeralConverterTest(unittest.TestCase):
    def setUp(self):
        print("Creating a new RomanNumeralConverter...")
        self.cvt = RomanNumeralConverter()

    def tearDown(self):
        print("Destroying the RomanNumeralConverter...")
        self.cvt = None

    def test_allDecimal(self):
        for key, value in self.cvt.digit_map.items():
            Result = self.cvt.convert_to_decimal(key)
            self.assertEqual(value, Result)

    def test_valZero(self):
        self.assertRaises(TypeError, self.cvt.convert_to_decimal, 0)

    def test_valError(self):
        self.assertRaises(ValueError, self.cvt.convert_to_decimal,"0")

    def test_longNumber(self):
        testnumbers = {'MMMMDCLXVI' : 4666,'MMMCXV' : 3115, 'MMMMCXXVI' : 4126, 'MMMCCCLXXXV' : 3385,'MMMMLCIX' : 4161}
        for roman, decimal in testnumbers.items():
            self.assertEqual(self.cvt.convert_to_decimal(roman), decimal)