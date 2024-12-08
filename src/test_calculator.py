import unittest
from calculate import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        result = self.calculator.calculate(10, 5, "add")
        self.assertEqual(result, 15)

    def test_subtraction(self):
        result = self.calculator.calculate(10, 5, "sub")
        self.assertEqual(result, 5)

    def test_multiplication(self):
        result = self.calculator.calculate(10, 5, "mul")
        self.assertEqual(result, 50)

    def test_division(self):
        result = self.calculator.calculate(10, 5, "div")
        self.assertEqual(result, 2)

    def test_division_by_zero(self):
        result = self.calculator.calculate(10, 0, "div")
        self.assertEqual(result, "Error: Can not divide by zero!")

    def test_invalid_operator(self):
        result = self.calculator.calculate(10, 5, "unknown")
        self.assertEqual(result, "Invalid operator")


if __name__ == "__main__":
    unittest.main()
