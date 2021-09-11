from unittest import TestCase

from src.classes.budget import Budget
from src.classes.item import Item
from src.classes.tax_calculator import TaxCalculator
from src.classes.tax import ISS, ICMS, ICPP, IKCV


class TestTaxCalculator(TestCase):
    def setUp(self) -> None:
        self.random_budget = Budget()
        self.generic_item_1 = Item("Generic Item 1", 10.0)
        self.generic_item_2 = Item("Generic Item 2", 640.0)
        self.random_budget.add_item(self.generic_item_1)
        self.random_budget.add_item(self.generic_item_2)

    def test_should_return_ISS_tax_of_budget(self) -> None:
        resulted_tax = TaxCalculator.calculate(self.random_budget, ISS())
        expected_resulted_tax = 65.0
        self.assertEqual(expected_resulted_tax, round(resulted_tax, 1))

    def test_should_return_ICMS_tax_of_budget(self) -> None:
        resulted_tax = TaxCalculator.calculate(self.random_budget, ICMS())
        expected_resulted_tax = 39.0
        self.assertEqual(expected_resulted_tax, round(resulted_tax, 1))

    def test_should_return_ICPP_tax_of_budget_greater_than_five_hundred(self):
        resulted_tax = TaxCalculator.calculate(self.random_budget, ICPP())
        expected_resulted_tax = 45.5
        self.assertEqual(expected_resulted_tax, round(resulted_tax, 1))

    def test_should_return_ICPP_tax_of_budget_smaller_than_five_hundred(self):
        new_random_budget = Budget()
        new_random_budget.add_item(Item("Generic Item", 10.5))
        resulted_tax = TaxCalculator.calculate(new_random_budget, ICPP())
        expected_resulted_tax = 0.5
        self.assertEqual(expected_resulted_tax, round(resulted_tax, 1))

    def test_should_return_IKCV_tax_of_budget_greater_than_five_hundred_that_has_item_with_value_greater_than_a_hundred(
            self):
        resulted_tax = TaxCalculator.calculate(self.random_budget, IKCV())
        expected_resulted_tax = 65.0
        self.assertEqual(expected_resulted_tax, round(resulted_tax, 1))

    def test_should_return_IKCV_tax_of_budget_smaller_than_five_hundred(self):
        new_random_budget = Budget()
        new_random_budget.add_item(Item("Generic Item", 10.5))
        resulted_tax = TaxCalculator.calculate(new_random_budget, IKCV())
        expected_resulted_tax = 0.6
        self.assertEqual(expected_resulted_tax, round(resulted_tax, 1))

    def test_should_not_allow_calculate_tax_when_passing_object_that_is_not_instance_of_tax_type_or_conditional_tax_type(
            self) -> None:
        with self.assertRaises(TypeError):
            TaxCalculator.calculate(self.random_budget, TaxCalculator)
