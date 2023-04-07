from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_DELICACIES = ['Gingerbread', 'Stolen']
    DELICACY_CLASSES = {'Gingerbread': Gingerbread, 'Stolen': Stolen}
    VALID_BOOTHS = ['Open Booth', 'Private Booth']
    BOOTHS_CLASSES = {'Open Booth': OpenBooth, 'Private Booth': PrivateBooth}

    def __init__(self):
        self.booths = []  # obj booths
        self.delicacies = []  # obj delicacies
        self.income = 0.0

    def __find_delicacy(self, delicacy_name):
        for delicacy in self.delicacies:
            if delicacy.name == delicacy_name:
                return delicacy

    def __find_booth(self, booth_number):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                return booth

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if type_delicacy not in self.VALID_DELICACIES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        if self.__find_delicacy(name):
            raise Exception(f"{name} already exists!")

        delicacy_class = self.DELICACY_CLASSES[type_delicacy]
        new_delicacy = delicacy_class(name, price)
        self.delicacies.append(new_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if type_booth not in self.VALID_BOOTHS:
            raise Exception(f"{type_booth} is not a valid booth!")
        if self.__find_booth(booth_number):
            raise Exception(f"Booth number {booth_number} already exists!")

        booth_class = self.BOOTHS_CLASSES[type_booth]
        new_booth = booth_class(booth_number, capacity)
        self.booths.append(new_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."
        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        current_booth = self.__find_booth(booth_number)
        current_delicacy = self.__find_delicacy(delicacy_name)

        if not current_booth:
            raise Exception(f"Could not find booth {booth_number}!")
        if not current_delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        current_booth.delicacy_orders.append(current_delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        current_booth = self.__find_booth(booth_number)
        boot_price_for_reservation = current_booth.price_for_reservation
        orders_bill = sum([x.price for x in current_booth.delicacy_orders])
        total_price = boot_price_for_reservation + orders_bill
        self.income += total_price

        current_booth.delicacy_orders.clear()
        current_booth.is_reserved = False
        current_booth.price_for_reservation = 0

        return f"Booth {booth_number}:\n" \
               f"Bill: {total_price:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
