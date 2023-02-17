class BColors:
    WARNING = '\033[93m'
    ENDC = '\033[0m'

instructions = ["Use periods in decimal numbers, e.g. 0.5 and not 0,5",
                "Correct way to use functions is e.g. sin(90), not sin90",
                "Trigonometric functions use degrees"]

class CalculatorIO:
    def read(self, text="Input"):
        input_expression = input(f"{text}")
        return input_expression

    def write(self, output):
        if output is not None:
            print(output)

    def help(self):
        for instruction in instructions:
            print(f"{BColors.WARNING}{instruction}{BColors.ENDC}")
            print()

calculator_io = CalculatorIO()
