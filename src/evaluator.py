class Evaluate:
    def __init__(self, expression: str):
        self.top = -1
        self.expression = expression.split(" ")
        self.stack = []

    def evaluate(self):
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
        self.expression = expression.split(" ")
