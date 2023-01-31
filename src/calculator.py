from calculator_io import calculator_io
from shunting_yard import (InvalidInputError,
                           MisMatchedParenthesesError, ShuntingYard)

class bcolors:
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
                self.io.write(f"{bcolors.OKCYAN}Exiting...{bcolors.ENDC}")
                break
            else:
                try:
                    self.postfix_notation = ShuntingYard(given_expression).parse_expression()
                    self.io.write(self.postfix_notation)
                except InvalidInputError:
                    self.io.write(f"{bcolors.FAIL}Invalid input error{bcolors.ENDC}")
                except MisMatchedParenthesesError:
                    self.io.write(f"{bcolors.FAIL}Mismatched parentheses error{bcolors.ENDC}")
