from src.classes import Budget


class DiscountType:
    def __init__(self, next_discount):
        self.__next_discount = next_discount

    @property
    def next_discount(self):
        return self.__next_discount

    @property
    def discount_percentage(self):
        raise NotImplementedError

    def calculate(self, budget: Budget):
        raise NotImplementedError


class FiveItens(DiscountType):
    def __init__(self, next_discount):
        super().__init__(next_discount)

    @property
    def discount_percentage(self):
        return 0.1

    def calculate(self, budget: Budget):
        if budget.itens_quantity >= 5:
            return budget.value * self.discount_percentage
        return self.next_discount.calculate(budget)


class ValueGreaterThanFiveHundred(DiscountType):
    def __init__(self, next_discount):
        super().__init__(next_discount)

    @property
    def discount_percentage(self):
        return 0.07

    def calculate(self, budget: Budget):
        if budget.value >= 500:
            return budget.value * self.discount_percentage
        return self.next_discount.calculate(budget)


class NotEligible:
    @property
    def discount_percentage(self):
        return 0.0

    def calculate(self, budget: Budget):
        return budget.value * self.discount_percentage
