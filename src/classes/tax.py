from src.classes import Budget


class TaxType:
    @property
    def tax_percentage(self) -> float:
        raise NotImplementedError

    def calculate(self, budget: Budget) -> float:
        return budget.value * self.tax_percentage


class ISS(TaxType):
    @property
    def tax_percentage(self) -> float:
        return 0.1


class ICMS(TaxType):
    @property
    def tax_percentage(self) -> float:
        return 0.06


class ConditionalTaxType:
    @property
    def max_tax_percentage(self):
        raise NotImplementedError

    @property
    def min_tax_percentage(self):
        raise NotImplementedError

    def should_implement_max_tax_percentage(self, budget: Budget):
        raise NotImplementedError

    def calculate(self, budget: Budget):
        if self.should_implement_max_tax_percentage(budget):
            return budget.value * self.max_tax_percentage
        return budget.value * self.min_tax_percentage


class ICPP(ConditionalTaxType):
    @property
    def max_tax_percentage(self):
        return 0.07

    @property
    def min_tax_percentage(self):
        return 0.05

    def should_implement_max_tax_percentage(self, budget):
        return budget.value > 500


class IKCV(ConditionalTaxType):
    @property
    def max_tax_percentage(self):
        return 0.1

    @property
    def min_tax_percentage(self):
        return 0.06

    def should_implement_max_tax_percentage(self, budget):
        return budget.value > 500 and any(item.value > 100 for item in budget.get_itens())
