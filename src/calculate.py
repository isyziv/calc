class Calculator:
    def __init__(self):
        self.operations = {
            "add": self.add,
            "sub": self.subtract,
            "mul": self.multiply,
            "div": self.divide,
            "pow": self.pow,
        }

    def calculate(self, operand1, operand2, operator):
        if operator in self.operations:
            try:
                result = self.operations[operator](operand1, operand2)
                return self.format_number(result)
            except ValueError as e:
                return str(e)
        else:
            return "Invalid operator"

    @staticmethod
    def format_number(value):
        return value

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Error: Can not divide by zero!")
        return x / y

    def pow(self, x, y):
        return x ** y


if __name__ == "__main__":
    calculator = Calculator()
    print(calculator.calculate(10, 5, "+"))  # 15
    print(calculator.calculate(10, 0, "/"))  # Error: Can not divide by zero!
