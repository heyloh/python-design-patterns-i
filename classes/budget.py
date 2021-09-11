from classes import Item


class Budget:
    def __init__(self) -> None:
        self.__itens = []

    @property
    def value(self) -> float:
        total = 0.0
        for item in self.__itens:
            total += item.value
        return total

    def get_itens(self) -> tuple:
        return tuple(self.__itens)

    @property
    def itens_quantity(self) -> int:
        return len(self.__itens)

    def add_item(self, item: Item) -> None:
        if not isinstance(item, Item):
            raise TypeError("Invalid type for Item.")
        self.__itens.append(item)
