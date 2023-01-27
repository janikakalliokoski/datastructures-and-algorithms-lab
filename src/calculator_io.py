class CalculatorIO:
    def read(self, text="Input"):
        input_expression = input(f"{text}")
        return input_expression

    def write(self, output):
        print(output)


calculator_io = CalculatorIO()
