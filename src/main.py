import flet as ft
import math
from calculate import Calculator
from buttons import DigitButton, OperatorButton, ActionButton


class CalculatorApp(ft.Container):
    # application's root control (i.e. "view") containing all other controls
    def __init__(self):
        super().__init__()
        self.reset()
        self.memory_display = ft.Text(
            value="M", color=ft.Colors.WHITE, size=20, visible=False)
        self.result = ft.Text(value="0", color=ft.Colors.WHITE, size=20)

        self.bgcolor = ft.Colors.BLACK
        self.border_radius = ft.border_radius.all(20)
        self.padding = 20
        self.expand = 1
        self.clac = Calculator()
        self.calculate = self.clac.calculate
        self.content = self.ui()
        self.memory = 0

    def ui(self):
        ui = ft.Column(
            controls=[
                ft.Row(
                    expand=True,
                    controls=[
                        ft.Container(
                            content=self.memory_display,
                            padding=ft.padding.only(left=10, right=10),
                            alignment=ft.alignment.center_left,
                            border_radius=ft.border_radius.all(8),
                            width=40,
                        ),
                        ft.Container(
                            content=self.result,
                            padding=ft.padding.only(left=10, right=10),
                            alignment=ft.alignment.center_right,
                            bgcolor=ft.Colors.BLACK,
                            border_radius=ft.border_radius.all(8),
                            expand=True,
                        ),
                    ],
                    alignment="end"),
                ft.Row(
                    expand=True,
                    controls=[
                        ActionButton(
                            text="AC",
                            button_clicked=self.button_clicked,
                            action="clear",
                        ),
                        ActionButton(
                            text="MC",
                            button_clicked=self.button_clicked,
                            action="clear_memory",
                        ),
                        ActionButton(
                            text="MR",
                            button_clicked=self.button_clicked,
                            action="recall_memory",
                        ),
                        ActionButton(
                            text="M+",
                            button_clicked=self.button_clicked,
                            action="add_memory",
                        ),
                        ActionButton(
                            text="M-",
                            button_clicked=self.button_clicked,
                            action="subtract_memory",
                        ),
                    ]
                ),
                ft.Row(
                    expand=True,
                    controls=[
                        OperatorButton(
                            text="^",
                            button_clicked=self.button_clicked,
                            operations="pow",
                        ),
                        ActionButton(
                            text="√",
                            button_clicked=self.button_clicked,
                            action="sqrt",
                        ),
                        ActionButton(
                            text="+/-",
                            button_clicked=self.button_clicked,
                            action="negate",
                        ),
                        ActionButton(
                            text="%",
                            button_clicked=self.button_clicked,
                            action="percent",
                        ),

                        OperatorButton(
                            text="÷",
                            button_clicked=self.button_clicked,
                            operations="div",
                        ),
                    ]
                ),
                ft.Row(
                    expand=True,
                    controls=[
                        DigitButton(
                            text="π", button_clicked=self.button_clicked, value=math.pi, bgcolor=ft.Colors.BLUE_GREY_200, color=ft.Colors.BLACK, constant=True),
                        DigitButton(
                            text="7", button_clicked=self.button_clicked, value=7),
                        DigitButton(
                            text="8", button_clicked=self.button_clicked, value=8),
                        DigitButton(
                            text="9", button_clicked=self.button_clicked, value=9),
                        OperatorButton(
                            text="*", button_clicked=self.button_clicked, operations="mul"),
                    ]
                ),
                ft.Row(
                    expand=True,
                    controls=[
                        DigitButton(
                            text="e", button_clicked=self.button_clicked, value=math.e, bgcolor=ft.Colors.BLUE_GREY_200, color=ft.Colors.BLACK, constant=True),
                        DigitButton(
                            text="4", button_clicked=self.button_clicked, value=4),
                        DigitButton(
                            text="5", button_clicked=self.button_clicked, value=5),
                        DigitButton(
                            text="6", button_clicked=self.button_clicked, value=6),
                        OperatorButton(
                            text="-", button_clicked=self.button_clicked, operations="sub"),
                    ]
                ),
                ft.Row(
                    expand=True,
                    controls=[
                        ActionButton(
                            text="log", button_clicked=self.button_clicked, action="log"),
                        DigitButton(
                            text="1", button_clicked=self.button_clicked, value=1),
                        DigitButton(
                            text="2", button_clicked=self.button_clicked, value=2),
                        DigitButton(
                            text="3", button_clicked=self.button_clicked, value=3),
                        OperatorButton(
                            text="+", button_clicked=self.button_clicked, operations="add"),
                    ]
                ),
                ft.Row(
                    expand=True,
                    controls=[
                        ActionButton(
                            text="ln", button_clicked=self.button_clicked, action="ln"),
                        DigitButton(
                            text="0", expand=1, button_clicked=self.button_clicked, value=0
                        ),
                        DigitButton(
                            text=".", button_clicked=self.button_clicked, value="."),
                        ActionButton(
                            text="⌫", button_clicked=self.button_clicked, action="backspace"),
                        ActionButton(
                            text="=", button_clicked=self.button_clicked, action="calculate"),
                    ]
                ),
            ]
        )
        return ui

    def button_clicked(self, e):
        types = e.control.type
        if types == "digit":
            self.digit_button_clicked(e)
        elif types == "operator":
            self.operator_button_clicked(e)
        elif types == "action":
            self.action_button_clicked(e)
        else:
            raise ValueError("Invalid button type")
        self.update()

    def digit_button_clicked(self, e):
        value = e.control.value
        if self.result.value == "0" or self.new_operand == True or e.control.constant == True:
            self.result.value = str(value)
            self.new_operand = False
        else:
            self.result.value = self.result.value + str(value)
        pass

    def operator_button_clicked(self, e):
        self.operator = e.control.operations
        if self.operand1 != 0:
            self.result.value = self.format_number(
                self.calculate(
                    self.operand1, float(self.result.value), self.operator
                )
            )
        if self.result.value == "Error":
            self.operand1 = "0"
        else:
            self.operand1 = float(self.result.value)
        self.new_operand = True

        pass

    def action_button_clicked(self, e):
        action = e.control.action
        if action == "clear":
            self.result.value = "0"
            self.reset()
        elif action == "negate":
            self.result.value = str(
                self.format_number(
                    -1*float(self.result.value)
                )
            )
        elif action == "percent":
            self.result.value = str(
                self.format_number(
                    float(self.result.value) / 100
                )
            )
            self.reset()
        elif action == "calculate":
            self.result.value = self.format_number(
                self.calculate(
                    self.operand1, float(self.result.value), self.operator
                )
            )
            self.reset()
        elif action == "backspace":
            self.result.value = self.result.value[:-1]
            if self.result.value == "":
                self.result.value = "0"
        elif action == "sqrt":
            self.result.value = self.format_number(
                math.sqrt(float(self.result.value))
            )
        elif action == "log":
            self.result.value = self.format_number(
                math.log10(float(self.result.value))
            )
        elif action == "ln":
            self.result.value = self.format_number(
                math.log(float(self.result.value))
            )
        elif action == "clear_memory":
            self.memory = 0
            self.memory_display.visible = False
            self.update()
        elif action == "recall_memory":
            self.result.value = str(int(self.memory))
        elif action == "add_memory":
            self.memory += float(self.result.value)
            if self.memory != 0:
                self.memory_display.visible = True
        elif action == "subtract_memory":
            self.memory -= float(self.result.value)
            if self.memory != 0:
                self.memory_display.visible = True
        else:
            raise ValueError("Invalid action")
        if self.memory == 0:
            self.memory_display.visible = False

    def format_number(self, num):
        if num % 1 == 0:
            return int(num)
        else:
            return num

    def format_number(self, num):
        try:
            if isinstance(num, (int, float)):
                if num % 1 == 0:
                    return int(num)
                else:
                    return num
            else:
                return num
        except Exception as e:
            print(f"Error formatting number: {e}")
            return "Error"

    def reset(self):
        self.operator = "+"
        self.operand1 = 0
        self.new_operand = True


def main(page: ft.Page):
    page.title = "Calc App"
    page.bgcolor = "#6C6C6C"
    page.window.min_width = 500
    page.window.min_height = 350
    # create application instance
    calc = CalculatorApp()

    # add application's root control to the page
    page.add(calc)


ft.app(target=main)
