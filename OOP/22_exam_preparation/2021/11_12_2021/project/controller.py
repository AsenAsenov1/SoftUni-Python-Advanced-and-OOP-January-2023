from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    VALID_CARS = ['MuscleCar', 'SportsCar']
    CARS_CLASSES = [MuscleCar, SportsCar]

    def __init__(self):
        self.cars = []  # An empty list that will contain all cars (objects)
        self.drivers = []  # An empty list that will contain all drivers (objects)
        self.races = []  # An empty list that will contain all races (objects)

    def __find_car(self, car_model):
        for car in self.cars:
            if car.model == car_model:
                return car

    def __find_driver(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver

    def __find_race(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in self.VALID_CARS:
            return
        if self.__find_car(model):
            raise Exception(f"Car {model} is already created!")

        for car in self.CARS_CLASSES:
            if car.__name__ == car_type:
                new_car = car(model, speed_limit)
                self.cars.append(new_car)
                return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if self.__find_driver(driver_name):
            raise Exception(f"Driver {driver_name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if self.__find_race(race_name):
            raise Exception(f"Race {race_name} is already created!")

        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        found_cars = []
        current_driver = self.__find_driver(driver_name)

        for car in self.cars[::-1]:
            if (not car.is_taken) and (car.__class__.__name__ == car_type):
                found_cars.append(car)
        if not self.__find_driver(driver_name):
            raise Exception(f"Driver {driver_name} could not be found!")
        if car_type not in self.VALID_CARS or len(found_cars) == 0:
            raise Exception(f"Car {car_type} could not be found!")

        available_car = found_cars[0]

        if current_driver.car:
            old_model = current_driver.car
            old_model.is_taken = False
            current_driver.car = available_car
            current_driver.car.is_taken = True
            return f"Driver {driver_name} changed his car from {old_model.model} to {current_driver.car.model}."

        current_driver.car = available_car
        available_car.is_taken = True
        return f"Driver {driver_name} chose the car {available_car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        current_race = self.__find_race(race_name)
        current_driver = self.__find_driver(driver_name)

        if not current_race:
            raise Exception(f"Race {race_name} could not be found!")
        if not current_driver:
            raise Exception(f"Driver {driver_name} could not be found!")
        if not current_driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        else:
            if current_driver in current_race.drivers:
                return f"Driver {driver_name} is already added in {race_name} race."

            current_race.drivers.append(current_driver)
            return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        current_race = self.__find_race(race_name)
        output_message = ''

        if not current_race:
            raise Exception(f"Race {race_name} could not be found!")
        if len(current_race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        top_three_drivers = {}
        for driver in current_race.drivers:
            driver_name = driver.name
            speed = driver.car.speed_limit
            top_three_drivers[driver_name] = speed

        for driver, speed in sorted(top_three_drivers.items(), key=lambda x: -x[1])[:3]:
            output_message += f'Driver {driver} wins the {race_name} race with a speed of {speed}.\n'

        return output_message.strip()
