from project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    __PORTION = 200

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        self.portion = self.__PORTION

    def details(self):
        return f"Gingerbread {self.name}: 200g - {self.price:.2f}lv."
