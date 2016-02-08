import unittest
from app.fizzbuzz import FizzBuzz


class TestFizzbuzz(unittest.TestCase):

    def setUp(self):
        self.fizzbuzz = FizzBuzz()

    def tearDown(self):
        pass

    def test_Fizzbuzz_returns_fizz_from_3(self):
        self.assertEqual(self.fizzbuzz.value(3), "fizz")

    def test_Fizzbuzz_returns_fizz_from_5(self):
        self.assertEqual(self.fizzbuzz.value(5), "buzz")

    def test_Fizzbuzz_returns_fizz_from_15(self):
        self.assertEqual(self.fizzbuzz.value(15), "fizzbuzz")

    def test_Fizzbuzz_returns_4_from_4(self):
        self.assertEqual(self.fizzbuzz.value(4), 4)
