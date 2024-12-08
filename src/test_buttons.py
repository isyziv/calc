import unittest
from buttons import DigitButton, OperatorButton, ActionButton


class TestButtons(unittest.TestCase):
    def test_digit_button(self):
        button = DigitButton(text="5", button_clicked=None, value=5)
        self.assertEqual(button.type, "digit")
        self.assertEqual(button.value, 5)

    def test_operator_button(self):
        button = OperatorButton(text="+", button_clicked=None, operations="add")
        self.assertEqual(button.type, "operator")
        self.assertEqual(button.operations, "add")

    def test_action_button(self):
        button = ActionButton(text="AC", button_clicked=None, action="clear")
        self.assertEqual(button.type, "action")
        self.assertEqual(button.action, "clear")


if __name__ == "__main__":
    unittest.main()
