from unittest import TestCase

from classes import Budget


class TestBudget(TestCase):
    def setUp(self):
        self.random_budget = Budget(500)

    def test_should_have_initial_value(self):
        expected_budget_value = 500
        budget_value = self.random_budget.value
        self.assertEqual(expected_budget_value, budget_value)
