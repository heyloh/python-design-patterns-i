from classes import Budget


class DiscountCalculator:
    @staticmethod
    def calculate(budget: Budget):
        if budget.itens_quantity >= 5:
            return budget.value * 0.1
        elif budget.value > 500:
            return budget.value * 0.07
        return 0.0
