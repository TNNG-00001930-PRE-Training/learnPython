import unittest
from nikhil_kothale.Test_cases.testcase.test_program import concatenate_strings, slice_string, format_string, manipulate_string

class TestStringOpeartions(unittest.TestCase):

    def test_concatenate_strings(self):
        self.assertEqual(concatenate_strings("Hello, ", "World!"), "Hello, World!")
        self.assertEqual(concatenate_strings("Python", " is awesome"), "Python is awesome")
        self.assertEqual(concatenate_strings("", "Empty"), "Empty")
        self.assertEqual(concatenate_strings("123 ", "are good"), "123 are good")


    
    def test_slice_string(self):
        self.assertEqual(slice_string("Hello, World!", 2, 5), "llo")
        self.assertEqual(slice_string("Python", 0, 5), "Pytho")
        self.assertEqual(slice_string("Programming", 3, 10), "grammin")
        self.assertEqual(slice_string("Testing", 0, 7), "Testing")
        self.assertEqual(slice_string("Negative", -4, -1), "tiv")



    def test_format_string(self):
        self.assertEqual(format_string("Alice", 30), "My name is Alice and I am 30 years old")
        self.assertEqual(format_string("Bob", 25), "My name is Bob and I am 25 years old")
        self.assertEqual(format_string("", 40), "My name is  and I am 40 years old")
        self.assertEqual(format_string("John Doe", 35), "My name is John Doe and I am 35 years old")


    def test_manipulate_string(self):
        self.assertEqual(manipulate_string("   Hello, World!   "), ("   HELLO, WORLD!   ", "   hello, world!   ", "Hello, World!", "   Hi, World!   "))
        self.assertEqual(manipulate_string("UPPERCASE"), ("UPPERCASE", "uppercase", "UPPERCASE", "UPPERCASE"))
        self.assertEqual(manipulate_string("lowercase"), ("LOWERCASE", "lowercase", "lowercase", "lowercase"))



if __name__ == '__main__':
    unittest.main()