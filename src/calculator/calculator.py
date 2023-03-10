from string import ascii_lowercase
from calculator.calculator_io import calculator_io
from algorithms.shunting_yard import (InvalidInputError,
                           MisMatchedParenthesesError,
                           ShuntingYard)
from algorithms.evaluator import Evaluate

class BColors:
    """Colors for text UI.
    """

    OKCYAN = '\033[96m'
    WARNING = '\033[93m'
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
                self.postfix_notation = ShuntingYard(given_expression,
                                        self.variables).parse_expression()
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
            except ValueError:
                self.io.write(f"{BColors.FAIL}Value error{BColors.ENDC}")

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

    def check_variable_name(self, variable):
        """This method is tp check if variable name is valid.

        Args:
            variable (str): Variable to be set.

        Returns:
            Boolean: True if variable name is valid and False if variable name is invalid.
        """

        if variable not in ascii_lowercase or len(variable) != 1:
            return False
        return True

    def set_variable(self):
        """This method sets new variables and checks variables names and values validity.
        """

        while True:
            var = self.io.read("Input variable's name: ")
            if var in self.variables:
                self.io.write(f"{BColors.WARNING}Variable's name already in use{BColors.ENDC}")
                continue

            if not self.check_variable_name(var):
                self.io.write(f"{BColors.WARNING}"+
                    "Variable's name must be in lowercase letters and 1 letter long"+
                    f"{BColors.ENDC}")
                continue
            break

        while True:
            value = self.io.read("Input variable's value: ")
            try:
                if "." in value:
                    if "." == value[0]:
                        self.io.write(f"{BColors.WARNING}"+
                        "Value cannot start with a period"+
                        f"{BColors.ENDC}")
                        continue
                    value_to_set = float(value)
                else:
                    value_to_set = int(value)
            except ValueError:
                self.io.write(f"{BColors.FAIL}Value error{BColors.ENDC}")
                continue
            break

        self.variables[var] = value_to_set

    def list_variables(self):
        """This method lists all variables that are set.
        """
        if len(self.variables) == 0:
            self.io.write(f"{BColors.WARNING}No defined variables{BColors.ENDC}")
        for var, value in self.variables.items():
            self.io.write(f"{var} = {value}")
