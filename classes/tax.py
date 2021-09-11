from classes import Budget


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
