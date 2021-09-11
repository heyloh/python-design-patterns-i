from unittest import TestCase

from src.classes.budget import Budget
from src.classes.item import Item
from src.classes.discount_calculator import DiscountCalculator


class TestDiscountCalculator(TestCase):
    def setUp(self):
        self.random_budget = Budget()
        generic_item_1 = Item("Generic Item 1", 100)
        generic_item_2 = Item("Generic Item 2", 100)
        generic_item_3 = Item("Generic Item 3", 100)
        self.random_budget.add_item(generic_item_1)
        self.random_budget.add_item(generic_item_2)
        self.random_budget.add_item(generic_item_3)

    def test_should_calculate_discount_when_budget_has_five_or_more_itens(self):
        self.random_budget.add_item(Item("New Generic Item", 100.0))
        self.random_budget.add_item(Item("New Generic Item", 100.0))
        expected_calculated_discount = 50.0
        calculated_discount = DiscountCalculator.calculate(self.random_budget)
        self.assertEqual(expected_calculated_discount, calculated_discount)

    def test_should_calculate_discount_when_budget_has_less_than_five_itens_and_more_than_500_on_value(self):
        self.random_budget.add_item(Item("New Generic Item", 201.0))
        expected_calculated_discount = 35.07
        calculated_discount = DiscountCalculator.calculate(self.random_budget)
        self.assertEqual(expected_calculated_discount, calculated_discount)

    def test_should_not_allow_have_discounts_when_less_than_five_itens_and_less_than_500_on_budget(self):
        expected_calculated_discount = 0.0
        calculated_discount = DiscountCalculator.calculate(self.random_budget)
        self.assertEqual(expected_calculated_discount, calculated_discount)
