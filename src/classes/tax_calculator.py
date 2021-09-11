from src.classes import TaxType, ConditionalTaxType


class TaxCalculator:
    @staticmethod
    def calculate(budget, tax_type) -> object:
        if isinstance(tax_type, (TaxType, ConditionalTaxType)):
            return tax_type.calculate(budget)
        else:
            raise TypeError("Invalid class for Tax.")
