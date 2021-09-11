class Item:
    def __init__(self, name: str, value: float) -> None:
        self.__name = name
        self.__value = value

    @property
    def value(self) -> float:
        return self.__value

    @property
    def name(self) -> str:
        return self.__name
