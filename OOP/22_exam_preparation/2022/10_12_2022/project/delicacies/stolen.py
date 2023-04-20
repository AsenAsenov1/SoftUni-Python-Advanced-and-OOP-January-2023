from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    __PORTION = 250

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        self.portion = self.__PORTION

    def details(self):
        return f"Stolen {self.name}: 250g - {self.price:.2f}lv."
