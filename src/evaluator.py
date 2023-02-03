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

        return self.stack.pop()

    def set_expression(self, expression: str):
        """Used for testing only.

        Args:
            expression (str): Postfix expression parsed by ShuntingYard algorithm.
        """

        self.expression = expression.split(" ")
