from project.animal import Animal


class Cheetah(Animal):
    DEFAULT_MONEY_FOR_CARE = 60

    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, self.DEFAULT_MONEY_FOR_CARE)
