import unittest
from task import conv_num


class TestCase(unittest.TestCase):

    def test_integer(self):
        self.assertEqual(conv_num("12345"), 12345)

    def test_float(self):
        self.assertEqual(conv_num("-123.45"), -123.45)

    def test_hex(self):
        self.assertEqual(conv_num("0xAD4"), 2772)

    def test_invalid(self):
        self.assertIsNone(conv_num("123A"))
    
    def test_negative_hex(self):
        self.assertEqual(conv_num("-0xAD4"), -2772)

    def test_empty_string(self):
        self.assertIsNone(conv_num(""))

    def test_multiple_decimal(self):
        self.assertIsNone(conv_num("12.3.45"))


if __name__ == '__main__':
    unittest.main()
