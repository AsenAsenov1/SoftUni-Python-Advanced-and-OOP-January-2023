from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    __DVD_CAPACITY = 15
    __CUSTOMER_CAPACITY = 10

    def __init__(self, name: str):
        self.name = name
        self.customers = []  # empty list of Customer objects
        self.dvds = []  # empty list of DVD objects

    @staticmethod
    def dvd_capacity():
        return MovieWorld.__DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.__CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.__CUSTOMER_CAPACITY:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.__DVD_CAPACITY:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer_obj = self.__find_object_by_id(self.customers, customer_id)
        dvd_obj = self.__find_object_by_id(self.dvds, dvd_id)

        if dvd_obj in customer_obj.rented_dvds:
            return f"{customer_obj.name} has already rented {dvd_obj.name}"
        elif dvd_obj.is_rented:
            return "DVD is already rented"
        elif customer_obj.age < dvd_obj.age_restriction:
            return f"{customer_obj.name} should be at least {dvd_obj.age_restriction} to rent this movie"
        else:
            customer_obj.rented_dvds.append(dvd_obj)
            dvd_obj.is_rented = True
            return f"{customer_obj.name} has successfully rented {dvd_obj.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer_obj = self.__find_object_by_id(self.customers, customer_id)
        dvd_obj = self.__find_object_by_id(self.dvds, dvd_id)

        if dvd_obj in customer_obj.rented_dvds:
            dvd_obj.is_rented = False
            customer_obj.rented_dvds.remove(dvd_obj)
            return f"{customer_obj.name} has successfully returned {dvd_obj.name}"
        return f"{customer_obj.name} does not have that DVD"

    @staticmethod
    def __find_object_by_id(list_of_objs, obj_id):
        return [x for x in list_of_objs if x.id == obj_id][0]

    def __repr__(self):
        each_customer = "\n".join([x.__repr__() for x in self.customers])
        each_dvd = "\n".join([x.__repr__() for x in self.dvds])
        output = each_customer + "\n" + each_dvd
        return output
