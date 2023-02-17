import unittest
from calculator import Calculator
from calculator_io import instructions

class StubIO:
    def __init__(self):
        self.inputs = []
        self.outputs = []

    def read(self, text=""):
        return self.inputs.pop(0)

    def write(self, output):
        self.outputs.append(output)

    def help(self):
        self.outputs.append(instructions)

    def set_inputs(self, inputs: list):
        self.inputs = inputs + ["exit"]

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.io = StubIO()
        self.calculator = Calculator(self.io)

    def test_exit_expression_quits(self):
        self.io.set_inputs(["exit"])

        self.calculator.start()

        output = self.io.outputs[0][5:-4]

        self.assertEqual(output, "Exiting...")

    def test_invalid_input_error(self):
        self.io.set_inputs(["1++1"])

        self.calculator.start()

        output = self.io.outputs[0][5:-4]

        self.assertEqual(output, "Invalid input error")

    def test_mismatched_parentheses_error(self):
        self.io.set_inputs(["1*(1+1))"])

        self.calculator.start()

        output = self.io.outputs[0][5:-4]

        self.assertEqual(output, "Mismatched parentheses error")

    def test_valid_input(self):
        self.io.set_inputs(["60*10"])

        self.calculator.start()

        output = self.io.outputs[0]

        self.assertEqual(output, 600.0)

    def test_empty_error_raises_value_error(self):
        self.io.set_inputs(["sin()"])

        self.calculator.start()

        output = self.io.outputs[0][5:-4]

        self.assertEqual(output, "Index error")

    def test_only_a_function_raises_index_error(self):
        self.io.set_inputs(["sin"])

        self.calculator.start()

        output = self.io.outputs[0][5:-4]

        self.assertEqual(output, "Index error")

    def test_instructions(self):
        self.io.set_inputs(["help"])

        self.calculator.start()

        output = self.io.outputs[0]

        self.assertEqual(output, instructions)

    def test_cannot_divide_by_zero(self):
        self.io.set_inputs(["1/0"])

        self.calculator.start()

        output = self.io.outputs[0][5:-4]

        self.assertEqual(output, "Division by zero error")

    def test_complex_expression_input(self):
        self.io.set_inputs(["sin(2)+cos(3)+tan(5)^3+10"])

        self.calculator.start()

        output = self.io.outputs[0]

        self.assertEqual(output, 11.034)

    def test_mismatched_parentheses_in_function(self):
        self.io.set_inputs(["sin(2"])

        self.calculator.start()

        output = self.io.outputs[0][5:-4]

        self.assertEqual(output, "Mismatched parentheses error")

    def test_long_expression(self):
        self.io.set_inputs(["((5*7)/(8/3))*(1/6)^2*sqrt(5*sin(30))"])

        self.calculator.start()

        output = self.io.outputs[0]

        self.assertEqual(output, 0.576)