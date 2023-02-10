import math
from shunting_yard import functions

class Evaluate:
    """This class calculates the result from the postfix expression that Shunting-Yard
    algorithm parsed.

    Attributes:
        expression: The postfix expression that the result will be calculated from.
    """

    def __init__(self, expression: str):
        """The constructor for Evaluate class.

        Args:
            expression (str): the postfix expression parsed by ShuntingYard algorithm.
        """

        self.top = -1
        self.expression = expression.split(" ")
        self.stack = []

    def evaluate(self):
        """This method iterates the expression and handles tokens. Finally it
        calculates the result.

        Returns:
            float: Calculated value.
        """
        for index, token in enumerate(self.expression):
            if token.isdigit() or "." in self.expression[index]:
                self.stack.append(float(token))
            elif token in "+-/*^":
                second = self.stack.pop()
                first = self.stack.pop()

                if token == "+":
                    self.stack.append(first + second)
                elif token == "-":
                    self.stack.append(first - second)
                elif token == "*":
                    self.stack.append(first * second)
                elif token == "/":
                    self.stack.append(first / second)
                elif token == "^":
                    self.stack.append(first ** second)
            elif token in functions:
                x = int(self.expression[index-1])
                self.calculate_function(token, x)

        return round(self.stack.pop(),3)

    def calculate_function(self, function: str, x: int):
        """This method calculates result from functions and adds the result to final result.

        Args:
            function (str): Function.
            x (int): Value for the function.
        """

        if function == "sin":
            self.stack.append(math.sin(math.radians(x)))
        elif function == "cos":
            self.stack.append(math.cos(math.radians(x)))
        elif function == "tan":
            self.stack.append(math.tan(math.radians(x)))
        elif function == "lg":
            self.stack.append(math.log(x, 10))
        elif function == "lb":
            self.stack.append(math.log(x, 2))
        elif function == "ln":
            self.stack.append(math.log(x))
        elif function == "sqrt":
            self.stack.append(math.sqrt(x))
        elif function == "abs":
            self.stack.append(abs(x))
        elif function ==  "exp":
            self.stack.append(math.exp(x))

    def set_expression(self, expression: str):
        """Used for testing only.

        Args:
            expression (str): Postfix expression parsed by ShuntingYard algorithm.
        """

        self.expression = expression.split(" ")

# if __name__ == "__main__":
#     exp = "-4 abs 2 2 * abs +"
#     exp1 = "sin"
#     print(Evaluate(exp1).evaluate())
