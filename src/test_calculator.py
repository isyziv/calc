import unittest
from calculate import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # 測試基本加減乘除
    def test_addition(self):
        self.assertEqual(self.calc.calculate(10, 5, "add"), 15)

    def test_subtraction(self):
        self.assertEqual(self.calc.calculate(10, 5, "sub"), 5)

    def test_multiplication(self):
        self.assertEqual(self.calc.calculate(10, 5, "mul"), 50)

    def test_division(self):
        self.assertEqual(self.calc.calculate(10, 2, "div"), 5)

    def test_division_by_zero(self):
        self.assertEqual(self.calc.calculate(10, 0, "div"),
                         "Error: Can not divide by zero!")

    def test_power(self):
        self.assertEqual(self.calc.calculate(2, 3, "pow"), 8)

    # 測試非法操作符
    def test_invalid_operator(self):
        self.assertEqual(self.calc.calculate(
            10, 5, "invalid"), "Invalid operator")

    # 測試數字格式化
    def test_format_number_integer(self):
        self.assertEqual(self.calc.format_number(5.0), 5)

    def test_format_number_float(self):
        self.assertEqual(self.calc.format_number(5.5), 5.5)


if __name__ == "__main__":
    unittest.main()
