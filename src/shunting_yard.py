import re
from collections import namedtuple

OPInfo = namedtuple('Operator', 'precedence associativity')
operator_info = {
    "+": OPInfo(0, "Left"),
    "-": OPInfo(0, "Left"),
    "/": OPInfo(1, "Left"),
    "*": OPInfo(1, "Left"),
    "^": OPInfo(2, "Right")
}

functions = ["abs", "cos", "exp", "lb", "lg", "ln", "sin", "sqrt", "tan"]


class InvalidInputError(Exception):
    """This class is used to raise an error if an input is invalid.
    """

class MisMatchedParenthesesError(Exception):
    """This class is used to raise an error if there are mismatched parentheses
    found in a given expression"""

class ShuntingYard:
    """This class parses a given expression from infix notation to postfix notation using the
    Shunting-Yard algorithm.

    Attributes:
        expression: The expression which will be parsed.
        output: A list that for storing the output as the algorithm parses the input.
        operator_stack: A list that is used to store operators.
        previous: A string containing the previous character(s).
    """

    def __init__(self, expression: str):
        """The constructor for the ShuntingYard class.

        Args:
            expression (str): the given expression in infix notation.
        """
        self.expression = re.sub(r'\s+', "", expression)
        self.output = []
        self.operator_stack = []
        self.previous = ""

    def parse_expression(self):
        """This method is in charge of parsing the given expression and returning the final output.

        This method goes through each token in the given expression to check the tokens type
        and handle it correctly. This method also checks the given expression for any invalidities.

        Raises:
            InvalidInputError: This error is raised if the expression includes invalid characters.
        Returns:
            str: The expression in postfix notation.
        """

        for index, token in enumerate(self.expression):
            if index == len(self.expression)-1:
                next_token = None
            else:
                next_token = self.expression[index+1]

            if index == 0:
                previous_token = None
            else:
                previous_token = self.expression[index-1]

            self.check_for_consecutive_operators(token, next_token)

            if token.isdigit():
                self.number_handler(token, next_token)
            elif token in operator_info.keys():
                self.operator_handler(token)
            elif token == "-":
                self.minus_token_handler(token, previous_token, next_token)
            elif token == ".":
                self.period_handler(token, next_token, index)
            elif token in ("(", ")"):
                self.parentheses_handler(token)
            else:
                raise InvalidInputError

        self.finish()

        return " ".join(self.output)

    def number_handler(self, token: str, next_token):
        """This method is for handling a number token.

        If next token is also a number, it will be stored. If not, it will be added to output.

        Args:
            token (str): Current token (number)
            next_token (str | None): The next token in expression.
        """
        if not next_token:
            self.output.append(self.previous + token)
        elif next_token.isdigit() or next_token == ".":
            self.previous += token
        else:
            self.output.append(self.previous + token)
            self.previous = ""

    # I'm still working on this method, because it works with input e.g. 5+.5 and gives
    # 5 .5 + and it's supposed to raise an error

    def period_handler(self, token: str, next_token, index: int):
        """This method is for handling a period token.

        Args:
            token (str): Current token (period).
            next_token (str | None): The next token in expression.
            index (int): Current token's index.

        Raises:
            InvalidInputError: Error will be raised if the expression starts with a period.
            InvalidInputError: Error will be raised, if next token is something else than a number.
        """

        if index == 0:
            raise InvalidInputError
        if not next_token or not next_token.isdigit():
            raise InvalidInputError
        self.previous += token

    def operator_handler(self, token: str):
        """This method is for handling an operator token.

        Args:
            token (str): Current token (operator).
        """

        if not self.operator_stack:
            self.operator_stack.append(token)
        else:
            while (self.operator_stack[-1] != "("
                   and ((operator_info[self.operator_stack].precedence\
                    > operator_info[token].precedence)
                        or (operator_info[self.operator_stack].precedence\
                             == operator_info[token].precedence
                            and operator_info[token].associativity == "Left"))):
                self.output.append(self.operator_stack.pop())
                if len(self.operator_stack) == 0:
                    break
            self.operator_stack.append(token)

    def parentheses_handler(self, token: str):
        """This method is for handling a parenthesis token.

        Args:
            token (str): Current token (left or right parenthesis).

        Raises:
            MisMatchedParenthesesError: Error will be raised if parenthesis is not found.
        """

        if token == "(":
            self.operator_stack.append(token)
        else:
            while True:
                if not self.operator_stack:
                    raise MisMatchedParenthesesError
                current_operator = self.operator_stack.pop()
                if current_operator != "(":
                    self.output.append(current_operator)
                    continue
                break

    def check_for_consecutive_operators(self, token: str, next_token):
        """This method checks if there are more than one operators consecutively.

        Args:
            token (str): Current token.
            next_token (str | None): Next token.

        Raises:
            InvalidInputError: Error will be raised if the expression contains more
            than one operator consecutively.
        """

        if token in operator_info.keys() and next_token in operator_info.keys():
            raise InvalidInputError

    # I'm still working on this method, it does not work correctly

    def minus_token_handler(self, token: str, previous_token, next_token):
        """This method checks if minus token means an operator or negation.

        Args:
            token (str): Current token (minus / -).
            previous_token (str | None): Token before minus sign.
            next_token (str | None): Next token after minus sign.
        """

        if previous_token is None and next_token == "(":
            self.output.append("0")
            self.operator_handler(token)
        elif previous_token is None or previous_token.isdigit() or not previous_token == ")":
            self.previous += token
        else:
            self.operator_handler(token)

    def finish(self):
        """This method iterates through the operator stack to check if any parentheses remain,
        and adding operators to the output.

        Raises:
            MisMatchedParenthesesError: Error will be raised if ay parentheses
            are left in the operator stack.
        """
        while self.operator_stack:
            if "(" in self.operator_stack or ")" in self.operator_stack:
                raise MisMatchedParenthesesError
            self.output.append(self.operator_stack.pop())


if __name__ == "__main__":
    exp = input("give an expression: ")
    print(ShuntingYard(exp))