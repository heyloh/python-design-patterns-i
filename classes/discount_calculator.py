from classes import Budget, FiveItens, ValueGreaterThanFiveHundred, NotEligible


class DiscountCalculator:
    @staticmethod
    def calculate(budget: Budget):
        return FiveItens(
            ValueGreaterThanFiveHundred(
                NotEligible()
            )
        ).calculate(budget)
