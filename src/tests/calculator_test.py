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

    def test_empty_error_raises_index_error(self):
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

    def test_setting_variable(self):
        self.io.set_inputs(["var", "set", "a", "1", "exit"])

        self.calculator.start()

        self.assertEqual(self.calculator.variables, {"a": 1})

    def test_try_number_var_name(self):
        self.io.set_inputs(["var", "set", "5", "b", "1", "exit"])

        self.calculator.start()

        output = self.io.outputs[0][5:-4]

        self.assertEqual(output, "Variable's name must be in lowercase letters and 1 letter long")
        self.assertEqual(self.calculator.variables, {"b": 1})

    def test_try_upper_case_var_name(self):
        self.io.set_inputs(["var", "set", "B", "b", "1", "exit"])

        self.calculator.start()

        output = self.io.outputs[0][5:-4]

        self.assertEqual(output, "Variable's name must be in lowercase letters and 1 letter long")
        self.assertEqual(self.calculator.variables, {"b": 1})

    def test_try_special_char_var_name(self):
        self.io.set_inputs(["var", "set", "%", "b", "1", "exit"])

        self.calculator.start()

        output = self.io.outputs[0][5:-4]

        self.assertEqual(output, "Variable's name must be in lowercase letters and 1 letter long")
        self.assertEqual(self.calculator.variables, {"b": 1})

    def test_try_longer_than_1char_var_name(self):
        self.io.set_inputs(["var", "set", "ab", "b", "1", "exit"])

        self.calculator.start()

        output = self.io.outputs[0][5:-4]

        self.assertEqual(output, "Variable's name must be in lowercase letters and 1 letter long")
        self.assertEqual(self.calculator.variables, {"b": 1})

    def test_decimal_as_value(self):
        self.io.set_inputs(["var", "set", "a", "0.1", "exit"])

        self.calculator.start()

        self.assertEqual(self.calculator.variables, {"a": 0.1})

    def test_invalid_value(self):
        self.io.set_inputs(["var", "set", "y", "0..1", "0.10", "exit"])

        self.calculator.start()

        output = self.io.outputs[0][5:-4]

        self.assertEqual(output, "Value error")
        self.assertEqual(self.calculator.variables, {"y": 0.1})

    def test_comma_as_period_in_value(self):
        self.io.set_inputs(["var", "set", "y", "0,1", "0.10", "exit"])

        self.calculator.start()

        output = self.io.outputs[0][5:-4]

        self.assertEqual(output, "Value error")
        self.assertEqual(self.calculator.variables, {"y": 0.1})

    def test_if_value_starts_period(self):
        self.io.set_inputs(["var", "set", "y", ".1", "0.10", "exit"])

        self.calculator.start()

        output = self.io.outputs[0][5:-4]

        self.assertEqual(output, "Value cannot start with a period")
        self.assertEqual(self.calculator.variables, {"y": 0.1})

    def test_negative_number_as_value(self):
        self.io.set_inputs(["var", "set", "a", "-5", "exit"])

        self.calculator.start()

        self.assertEqual(self.calculator.variables, {"a": -5})

    def test_invalid_negative_number_as_value(self):
        self.io.set_inputs(["var", "set", "a", "--5", "-5", "exit"])

        self.calculator.start()

        output = self.io.outputs[0][5:-4]

        self.assertEqual(output, "Value error")
        self.assertEqual(self.calculator.variables, {"a": -5})

    def test_special_char_in_value(self):
        self.io.set_inputs(["var", "set", "a", "%5", "-5", "exit"])

        self.calculator.start()

        output = self.io.outputs[0][5:-4]

        self.assertEqual(output, "Value error")
        self.assertEqual(self.calculator.variables, {"a": -5})

    def test_var_name_already_in_use(self):
        self.calculator.variables = {"a": 1}
        self.io.set_inputs(["var", "set", "a", "b", "2", "exit"])

        self.calculator.start()

        output = self.io.outputs[0][5:-4]

        self.assertEqual(output, "Variable's name already in use")
        self.assertEqual(self.calculator.variables, {"a": 1, "b": 2})

    def test_list_variables(self):
        self.calculator.variables = {"a": 1}
        self.io.set_inputs(["var", "set", "b", "2", "list", "exit"])

        self.calculator.start()

        output = self.io.outputs[0:2]

        self.assertEqual(output, ["a = 1", "b = 2"])
