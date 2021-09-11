from unittest import TestCase

from src.classes.budget import Budget
from src.classes.item import Item


class TestBudget(TestCase):
    def setUp(self):
        self.random_budget = Budget()
        self.generic_item_1 = Item("Generic Item 1", 10.0)
        self.generic_item_2 = Item("Generic Item 2", 640.0)
        self.random_budget.add_item(self.generic_item_1)
        self.random_budget.add_item(self.generic_item_2)

    def test_should_have_initial_value(self):
        expected_budget_value = 650
        budget_value = self.random_budget.value
        self.assertEqual(expected_budget_value, budget_value)

    def test_should_return_tuples_of_itens(self):
        expected_budget_itens = (self.generic_item_1, self.generic_item_2)
        budget_itens = self.random_budget.get_itens()
        self.assertEqual(expected_budget_itens, budget_itens)

    def test_should_return_quantity_of_itens(self):
        expected_budget_itens_quantity = 2
        budget_itens_quantity = self.random_budget.itens_quantity
        self.assertEqual(expected_budget_itens_quantity, budget_itens_quantity)

    def test_should_allow_add_new_item_to_budget_itens(self):
        new_generic_item = Item("New Generic Item", 50.0)
        self.random_budget.add_item(new_generic_item)
        expected_budget_itens_quantity = 3
        budget_itens_quantity = self.random_budget.itens_quantity
        self.assertEqual(expected_budget_itens_quantity, budget_itens_quantity)

    def test_should_now_allow_add_item_when_item_is_not_instance_of_item(self):
        with self.assertRaises(TypeError):
            self.random_budget.add_item(self.random_budget)
