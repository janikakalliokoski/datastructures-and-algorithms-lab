from calculator_io import calculator_io
from shunting_yard import (InvalidInputError,
                           MisMatchedParenthesesError, ShuntingYard)
from evaluator import Evaluate

class BColors:
    """Colors for text UI.
    """

    OKCYAN = '\033[96m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class Calculator:
    """This class is the framework for the calculatorand currently it
    starts the calculator. It uses an IO attribute to ask user for an expression
    and then the IO module reads the input. Then the IO module gives the expression
    for the ShuntingYard class to parse and finally it prints the output.
    """

    def __init__(self, io=calculator_io):
        """Constructor for the Calculator class. It creates an instance for the
        IO module

        Args:
            io : Used to read user's inputs and printing outputs.
            Defaults to calculator_io.
            postfix_notation (str) : Stores the postfix expression
        """

        self.io = io
        self.postfix_notation = ""

    def start(self):
        """This method starts the calculator and is in charge of running the calculator.
        It also asks the user for inputs and gives a correct expression for the ShuntingYard
        class to parse. This class also gives the postfix notation expression to Evaluate
        class so the result can be calculated. Finally it prints the result.
        """

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
