import unittest
from task import conv_endian, my_datetime, conv_num


class TestCase(unittest.TestCase):

    # conv_num tests
    def test_integer(self):
        self.assertEqual(conv_num("12345"), 12345)

    def test_float(self):
        self.assertEqual(conv_num("-123.45"), -123.45)

    def test_float_no_left_digit(self):
        self.assertEqual(conv_num(".45"), 0.45)

    def test_float_no_right_digit(self):
        res = conv_num("123.")

        self.assertEqual(res, 123.0)
        self.assertIsInstance(res, float)

    def test_hex(self):
        self.assertEqual(conv_num("0xAD4"), 2772)

    def test_hex_upper_x_lower_digits(self):
        self.assertEqual(conv_num("0Xad4"), 2772)

    def test_negative_hex(self):
        self.assertEqual(conv_num("-0xAD4"), -2772)

    def test_invalid_hex(self):
        self.assertIsNone(conv_num("0xAZ4"))

    def test_invalid_alpha(self):
        self.assertIsNone(conv_num("12345A"))

    def test_multiple_decimal(self):
        self.assertIsNone(conv_num("12.3.45"))

    def test_none_input(self):
        self.assertIsNone(conv_num(None))

    def test_non_string_input(self):
        self.assertIsNone(conv_num(12345))

    def test_empty_string(self):
        self.assertIsNone(conv_num(""))

    def test_positive_integer(self):
        self.assertEqual(conv_num("+123"), 123)

    def test_positive_float(self):
        self.assertEqual(conv_num("+123.45"), 123.45)

    def test_positive_hex(self):
        self.assertEqual(conv_num("+0xFF"), 255)

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
    # example cases
    def test_date_0(self):
        self.assertEqual(my_datetime(0), '01-01-1970')

    def test_date_sequential(self):
        self.assertEqual(my_datetime(123456789), '11-29-1973')

    def test_date_reverse(self):
        self.assertEqual(my_datetime(9876543210), '12-22-2282')

    def test_date_large(self):
        self.assertEqual(my_datetime(201653971200), '02-29-8360')

    # edge cases
    def test_date_day_boundary(self):
        self.assertEqual(my_datetime(86399), '01-01-1970')
        self.assertEqual(my_datetime(86400), '01-02-1970')

    def test_date_year_rollover(self):
        self.assertEqual(my_datetime(31449600), '12-31-1970')
        self.assertEqual(my_datetime(31536000), '01-01-1971')

    def test_date_leap_day(self):
        self.assertEqual(my_datetime(68169600), '02-29-1972')

    def test_date_div400_leap(self):
        self.assertEqual(my_datetime(951782400), '02-29-2000')

    def test_date_century_not_leap(self):
        self.assertEqual(my_datetime(4107542400), '03-01-2100')


if __name__ == '__main__':
    unittest.main()
