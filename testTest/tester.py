import unittest

from fizzbuzz import *

class TestFizzBuzz(unittest.TestCase):
    def setUp(self) -> None:
        self.fb = FizzBuzz()

    def test_divisible_by_3(self):
        number = 6
        result = self.fb.divisibleBy3(number)
        self.assertTrue(result)

    def test_divisible_by_5(self):
        number = 10
        result = self.fb.divisibleBy5(number)
        self.assertTrue(result)

    def test_not_divisible_by_3(self):
        number = 4
        result = self.fb.divisibleBy3(number)
        self.assertFalse(result)

    def test_not_divisible_by_5(self):
        number = 11
        result = self.fb.divisibleBy5(number)
        self.assertFalse(result)

    def test_divisible_by_15(self):
        number = 30
        result = self.fb.divisibleBy15(number)
        self.assertTrue(result)

    def test_not_divisible_by_15(self):
        number = 31
        result = self.fb.divisibleBy15(number)
        self.assertFalse(result)

    def test_negative(self):
        number = -1
        result = self.fb.isNegative(number)
        self.assertTrue(result)

    def test_positive(self):
        number = 1
        result = self.fb.isNegative(number)
        self.assertFalse(result)

    def test_fizz(self):
        number = 33
        self.assertEqual(self.fb.play(number), "fizz")

    def test_buzz(self):
        number = 55
        self.assertEqual(self.fb.play(number), "buzz")

    def test_fizzbuzz(self):
        number = 45
        self.assertEqual(self.fb.play(number), "fizzbuzz")

    def test_non_fizzbuzz(self):
        number = 17
        self.assertEqual(self.fb.play(number), str(number))

    def test_integer(self):
        number = 3
        self.assertTrue(self.fb.isInteger(number))

    def test_non_integer(self):
        number = 4.5
        self.assertFalse(self.fb.isInteger(number))

if __name__ == "__main__":
	unittest.main()
