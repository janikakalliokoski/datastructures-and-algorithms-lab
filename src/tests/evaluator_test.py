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
