import unittest
from task import conv_endian, my_datetime


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

    # conv_endian test examples
    def test_big_endian(self):
        self.assertEqual(conv_endian(954786, 'big'), '0E 91 A2')

    def test_default_endian(self):
        self.assertEqual(conv_endian(954786), '0E 91 A2')

    def test_negative_big_endian(self):
        self.assertEqual(conv_endian(-954786), '-0E 91 A2')

    def test_little_endian(self):
        self.assertEqual(conv_endian(954786, 'little'), 'A2 91 0E')

    def test_negative_little_endian(self):
        self.assertEqual(conv_endian(-954786, 'little'), '-A2 91 0E')

    def test_keyword_args(self):
        self.assertEqual(conv_endian(num=-954786, endian='little'), '-A2 91 0E')

    def test_invalid_endian(self):
        self.assertIsNone(conv_endian(num=-954786, endian='small'))

    # Additional tests for edge cases
    def test_zero(self):
        self.assertEqual(conv_endian(0), '00')

    def test_small_number(self):
        self.assertEqual(conv_endian(1), '01')

    def test_invalid_endian_typo(self):
        self.assertIsNone(conv_endian(954786, 'Big'))

    def test_invalid_endian_empty(self):
        self.assertIsNone(conv_endian(954786, ''))

    # datetime tests
    ## example cases
    def test_date_0(self):
        self.assertEqual(my_datetime(0), '01-01-1970')
    
    def test_date_sequential(self):
        self.assertEqual(my_datetime(123456789), '11-29-1973')
    
    def test_date_reverse(self):
        self.assertEqual(my_datetime(9876543210), '12-22-2282')
    
    def test_date_large(self):
        self.assertEqual(my_datetime(201653971200), '02-29-8360')

if __name__ == '__main__':
    unittest.main()
