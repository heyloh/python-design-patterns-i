from unittest import TestCase

from classes import Budget, Item
from classes.tax import ISS, ICMS
from classes.tax_calculator import TaxCalculator


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
        self.assertEqual(expected_resulted_tax, resulted_tax)

    def test_should_return_ICMS_tax_of_budget(self) -> None:
        resulted_tax = TaxCalculator.calculate(self.random_budget, ICMS())
        expected_resulted_tax = 39.0
        self.assertEqual(expected_resulted_tax, resulted_tax)

    def test_should_not_allow_calculate_tax_when_passing_object_that_is_not_instance_of_tax_type(self) -> None:
        with self.assertRaises(TypeError):
            TaxCalculator.calculate(self.random_budget, TaxCalculator)
