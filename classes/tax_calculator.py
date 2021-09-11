from classes.tax import TaxType


class TaxCalculator:
    @staticmethod
    def calculate(budget, tax_type):
        if not isinstance(tax_type, TaxType):
            raise TypeError("Invalid class for Tax.")
        return tax_type.calculate(budget)
