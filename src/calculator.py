from calculator_io import calculator_io
from shunting_yard import (InvalidInputError,
                           MisMatchedParenthesesError, ShuntingYard)
from evaluator import Evaluate

class BColors:
    OKCYAN = '\033[96m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class Calculator:
    def __init__(self, io=calculator_io):
        self.io = io
        self.postfix_notation = ""

    def start(self):
        while True:
            given_expression = self.io.read("Give an expression, exit for exit: ")
            if given_expression == "exit":
                self.io.write(f"{BColors.OKCYAN}Exiting...{BColors.ENDC}")
                break
            try:
                self.postfix_notation = ShuntingYard(given_expression).parse_expression()
                result = Evaluate(self.postfix_notation).evaluate()
                self.io.write(result)
            except InvalidInputError:
                self.io.write(f"{BColors.FAIL}Invalid input error{BColors.ENDC}")
            except MisMatchedParenthesesError:
                self.io.write(f"{BColors.FAIL}Mismatched parentheses error{BColors.ENDC}")
