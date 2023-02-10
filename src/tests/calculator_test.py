import unittest
from calculator import Calculator

class StubIO:
    def __init__(self):
        self.inputs = []
        self.outputs = []

    def read(self, text=""):
        return self.inputs.pop(0)

    def write(self, output):
        self.outputs.append(output)

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

        self.assertEqual(output, "Value error")

    def test_only_a_function_raises_index_error(self):
        self.io.set_inputs(["sin"])

        self.calculator.start()

        output = self.io.outputs[0][5:-4]

        self.assertEqual(output, "Index error")
