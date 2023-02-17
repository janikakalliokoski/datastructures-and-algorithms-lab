from string import ascii_lowercase
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
        self.variables = {}

    def start(self):
        """This method starts the calculator and is in charge of running the calculator.
        It also asks the user for inputs and gives a correct expression for the ShuntingYard
        class to parse. This class also gives the postfix notation expression to Evaluate
        class so the result can be calculated. Finally it prints the result.
        """

        while True:
            given_expression = self.io.read(
                "Give an expression, 'help' for instructions,"+
                " 'var' for variables, 'exit' for exit: "
            )
            if given_expression == "exit":
                self.io.write(f"{BColors.OKCYAN}Exiting...{BColors.ENDC}")
                break
            if given_expression == "var":
                self.variable()
                continue
            if given_expression == "help":
                self.io.write(self.io.help())
                continue
            try:
                self.postfix_notation = ShuntingYard(given_expression).parse_expression()
                result = Evaluate(self.postfix_notation).evaluate()
                self.io.write(result)
            except InvalidInputError:
                self.io.write(f"{BColors.FAIL}Invalid input error{BColors.ENDC}")
            except MisMatchedParenthesesError:
                self.io.write(f"{BColors.FAIL}Mismatched parentheses error{BColors.ENDC}")
            except IndexError:
                self.io.write(f"{BColors.FAIL}Index error{BColors.ENDC}")
            except ZeroDivisionError:
                self.io.write(f"{BColors.FAIL}Division by zero error{BColors.ENDC}")

    def variable(self):
        """This method is for setting and listing variables.
        """

        while True:
            given_input = self.io.read(
                "Input 'set' to set new variable, 'list' to show variables, 'exit' for exit: "
            )
            if given_input == "exit":
                self.io.write(f"{BColors.OKCYAN}Exiting...{BColors.ENDC}")
                break
            if given_input == "set":
                self.set_variable()
            elif given_input == "list":
                self.list_variables()

    def set_variable(self):
        """This method sets new variables and checks variables names and values validity.
        """

        while True:
            var = self.io.read("Input variable's name: ")
            if var in self.variables:
                self.io.write(f"{BColors.OKCYAN}Variable's name already in use{BColors.ENDC}")
                continue
            check = var in ascii_lowercase
            if not check or len(var) != 1:
                print(f"{BColors.OKCYAN}\
                    Variable's name must be in lowercase letters and 1 letter long\
                    {BColors.ENDC}")
                continue
            break

        while True:
            value = self.io.read("Input variable's value: ")
            if "." in value:
                value_to_set = float(value)
            else:
                value_to_set = int(value)
            break

        self.variables[var] = value_to_set

    def list_variables(self):
        """This method lists all variables that are set.
        """

        for var, value in self.variables.items():
            self.io.write(f"{var} = {value}")
