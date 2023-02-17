import unittest
from evaluator import Evaluate

class TestEvaluate(unittest.TestCase):
    def setUp(self):
        self.evaluate = Evaluate("")

    def test_sum_expression(self):
        self.evaluate.set_expression("1 1 +")

        result = self.evaluate.evaluate()

        self.assertEqual(result, 2.0)

    def test_subtraction_expression(self):
        self.evaluate.set_expression("2 3 -")

        result = self.evaluate.evaluate()

        self.assertEqual(result, -1.0)

    def test_multiplication_expression(self):
        self.evaluate.set_expression("60 10 *")

        result = self.evaluate.evaluate()

        self.assertEqual(result, 600.0)

    def test_division_expression(self):
        self.evaluate.set_expression("3 4 /")

        result = self.evaluate.evaluate()

        self.assertEqual(result, 0.75)

    def test_exponent_expression(self):
        self.evaluate.set_expression("2 2 + 2 1 + ^")

        result = self.evaluate.evaluate()

        self.assertEqual(result, 64.0)

    def test_expression_with_decimal_number(self):
        self.evaluate.set_expression("1.0 1 +")

        result = self.evaluate.evaluate()

        self.assertEqual(result, 2.0)

    def test_sin_function(self):
        self.evaluate.set_expression("90 sin")

        result = self.evaluate.evaluate()

        self.assertEqual(result, 1.0)

    def test_cos_function(self):
        self.evaluate.set_expression("0 cos")

        result = self.evaluate.evaluate()

        self.assertEqual(result, 1.0)

    def test_tan_function(self):
        self.evaluate.set_expression("45 tan")

        result = self.evaluate.evaluate()

        self.assertEqual(result, 1.0)

    def test_sqrt_function(self):
        self.evaluate.set_expression("4 sqrt")

        result = self.evaluate.evaluate()

        self.assertEqual(result, 2.0)

    def test_lg_function(self):
        self.evaluate.set_expression("10 lg")

        result = self.evaluate.evaluate()

        self.assertEqual(result, 1.0)

    def test_lb_function(self):
        self.evaluate.set_expression("4 lb")

        result = self.evaluate.evaluate()

        self.assertEqual(result, 2.0)

    def test_ln_function(self):
        self.evaluate.set_expression("8 ln")

        result = self.evaluate.evaluate()

        self.assertEqual(result, 2.079)

    def test_exp_function(self):
        self.evaluate.set_expression("8 exp")

        result = self.evaluate.evaluate()

        self.assertEqual(result, 2980.958)

    def test_abs_function(self):
        self.evaluate.set_expression("-3 abs")

        result = self.evaluate.evaluate()

        self.assertEqual(result, 3.0)

    def test_function_with_negative_number(self):
        self.evaluate.set_expression("-90 sin")

        result = self.evaluate.evaluate()

        self.assertEqual(result, -1.0)

    def test_two_functions_in_expression(self):
        self.evaluate.set_expression("-90 sin -90 sin +")

        result = self.evaluate.evaluate()

        self.assertEqual(result, -2.0)

    def test_sqrt_function_with_negative_number_raises_error(self):
        self.evaluate.set_expression("-4 sqrt")

        with self.assertRaises(ValueError):
            self.evaluate.evaluate()

    def test_empty_function_raises_error(self):
        self.evaluate.set_expression("sqrt")

        with self.assertRaises(IndexError):
            self.evaluate.evaluate()

    def test_complex_expression(self):
        self.evaluate.set_expression("3 sin -1 cos 2 1 - ^ +")

        result = self.evaluate.evaluate()

        self.assertEqual(result, 1.052)

    def test_parentheses_in_exponent(self):
        self.evaluate.set_expression("2 2 3 * ^")

        result = self.evaluate.evaluate()

        self.assertEqual(result, 64.0)

    def test_long_expression(self):
        self.evaluate.set_expression("4 3 * 12 1 - ^ 5 +")

        result = self.evaluate.evaluate()

        self.assertEqual(result, 743008370693.0)
