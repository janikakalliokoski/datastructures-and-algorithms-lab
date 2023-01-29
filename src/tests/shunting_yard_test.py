import unittest
from shunting_yard import (InvalidInputError,
                           MisMatchedParenthesesError, ShuntingYard)

class TestShuntingYard(unittest.TestCase):
    def setUp(self):
        self.shunting_yard = ShuntingYard("")

    def test_sum_expression(self):
        self.shunting_yard.expression = "3+3"

        result = self.shunting_yard.parse_expression()

        self.assertEqual(result, "3 3 +")

    def test_subtraction_expression(self):
        self.shunting_yard.expression = "3-3"

        result = self.shunting_yard.parse_expression()

        self.assertEqual(result, "3 3 -")

    def test_correct_amount_of_parentheses(self):
        self.shunting_yard.expression = "2*(2+2)"

        result = self.shunting_yard.parse_expression()

        self.assertEqual(result, "2 2 2 + *")

    def test_wrong_amount_of_parentheses_raises_an_error(self):
        self.shunting_yard.expression = "2*((2+2)"

        with self.assertRaises(MisMatchedParenthesesError):
            self.shunting_yard.parse_expression()

    def test_more_than_one_operator_consecutively_raises_an_error(self):
        self.shunting_yard.expression = "2++2"

        with self.assertRaises(InvalidInputError):
            self.shunting_yard.parse_expression()

    def test_numbers_with_more_than_one_digit_expression(self):
        self.shunting_yard.expression = "15+5"

        result = self.shunting_yard.parse_expression()

        self.assertEqual(result, "15 5 +")

    def test_expression_starting_with_period_raises_an_error(self):
        self.shunting_yard.expression = ".5+5"

        with self.assertRaises(InvalidInputError):
            self.shunting_yard.parse_expression()

    def test_expression_with_decimals_work(self):
        self.shunting_yard.expression = "5+0.5"

        result = self.shunting_yard.parse_expression()

        self.assertEqual(result, "5 0.5 +")

    def test_expression_with_decimal_raises_an_error_if_next_token_is_not_number(self):
        self.shunting_yard.expression = "5+0./"

        with self.assertRaises(InvalidInputError):
            self.shunting_yard.parse_expression()

    def test_division_expression(self):
        self.shunting_yard.expression = "10/2"

        result = self.shunting_yard.parse_expression()

        self.assertEqual(result, "10 2 /")

    def test_multiplication_expression(self):
        self.shunting_yard.expression = "2*2"

        result = self.shunting_yard.parse_expression()

        self.assertEqual(result, "2 2 *")

    def test_spaces_are_removed_from_given_expression(self):
        self.shunting_yard.given_expression = "5 + 5"

        self.shunting_yard.expression = "5+5"

        self.assertEqual(self.shunting_yard.expression, "5+5")

    def test_decimals_given_with_comma_raises_an_error(self):
        self.shunting_yard.expression = "5,5+5"

        with self.assertRaises(InvalidInputError):
            self.shunting_yard.parse_expression()

    def test_period_with_no_next_token_raises_an_error(self):
        self.shunting_yard.expression = "5+0."

        with self.assertRaises(InvalidInputError):
            self.shunting_yard.parse_expression()

    def test_remaining_parentheses_raise_an_error(self):
        self.shunting_yard.expression = "2*(2+2)("

        with self.assertRaises(MisMatchedParenthesesError):
            self.shunting_yard.parse_expression()

    def test_exponent_expression(self):
        self.shunting_yard.expression = "2*(2+2)^2"

        result = self.shunting_yard.parse_expression()

        self.assertEqual(result, "2 2 2 + 2 ^ *")

    def test_negative_number_expression(self):
        self.shunting_yard.expression = "-2+2"

        result = self.shunting_yard.parse_expression()

        self.assertEqual(result, "-2 2 +")

    def test_minus_token_and_then_parentheses_adds_0_to_output(self):
        self.shunting_yard.expression = "-(2+2)"

        result = self.shunting_yard.parse_expression()

        self.assertEqual(result, "0 2 2 + -")