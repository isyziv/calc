import unittest
from buttons import DigitButton, OperatorButton, ActionButton


class TestButtons(unittest.TestCase):

    # 測試數字按鈕屬性
    def test_digit_button(self):
        button = DigitButton("1", None, value=1)
        self.assertEqual(button.type, "digit")
        self.assertEqual(button.text, "1")
        self.assertEqual(button.value, 1)
        self.assertFalse(button.constant)

    def test_constant_digit_button(self):
        button = DigitButton("π", None, value=3.14159, constant=True)
        self.assertEqual(button.type, "digit")
        self.assertEqual(button.text, "π")
        self.assertTrue(button.constant)

    # 測試運算符按鈕屬性
    def test_operator_button(self):
        button = OperatorButton("+", None, operations="add")
        self.assertEqual(button.type, "operator")
        self.assertEqual(button.text, "+")
        self.assertEqual(button.operations, "add")

    # 測試動作按鈕屬性
    def test_action_button(self):
        button = ActionButton("AC", None, action="clear")
        self.assertEqual(button.type, "action")
        self.assertEqual(button.text, "AC")
        self.assertEqual(button.action, "clear")

    # 測試按鈕類型驗證
    def test_invalid_button_type(self):
        with self.assertRaises(AssertionError):
            button = OperatorButton("X", None)
            button.type = "invalid"


if __name__ == "__main__":
    unittest.main()
