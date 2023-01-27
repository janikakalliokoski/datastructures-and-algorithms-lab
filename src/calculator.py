from calculator_io import calculator_io
from shunting_yard import (InvalidInputError,
                           MisMatchedParenthesesError, ShuntingYard)


class Calculator:
    def __init__(self, io=calculator_io):
        self.io = io
        self.postfix_notation = ""

    def start(self):
        while True:
            expression = self.io.read("Give an expression, exit for exit: ")
            if expression == "exit":
                self.io.write("Exiting...")
                break
            self.postfix_notation = ShuntingYard(expression).parse_expression()
            self.io.write(self.postfix_notation)
