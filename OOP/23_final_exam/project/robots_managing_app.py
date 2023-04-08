from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICES = ['MainService', 'SecondaryService']
    SERVICES_CLASSES = {'MainService': MainService, 'SecondaryService': SecondaryService}
    VALID_ROBOTS = ['MaleRobot', 'FemaleRobot']
    ROBOTS_CLASSES = {'MaleRobot': MaleRobot, 'FemaleRobot': FemaleRobot}

    def __init__(self):
        self.robots = []  # Empty list that will contain all robots (objects) that are created.
        self.services = []  # Empty list that will contain all services (objects) that are created.

    def __find_robot(self, robot_name):
        for robot in self.robots:
            if robot.name == robot_name:
                return robot

    def __find_service(self, service_name):
        for service in self.services:
            if service.name == service_name:
                return service

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICES:
            raise Exception("Invalid service type!")

        new_service_class = self.SERVICES_CLASSES[service_type]
        service_name = new_service_class(name)
        self.services.append(service_name)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOTS:
            raise Exception("Invalid robot type!")

        new_robot_class = self.ROBOTS_CLASSES[robot_type]
        robot_name = new_robot_class(name, kind, price)
        self.robots.append(robot_name)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        current_robot = self.__find_robot(robot_name)
        current_service = self.__find_service(service_name)
        robot_type_key = current_robot.__class__.__name__
        service_type_key = current_service.__class__.__name__

        if self.ROBOTS_CLASSES[robot_type_key] == FemaleRobot:
            if self.SERVICES_CLASSES[service_type_key] != SecondaryService:
                return "Unsuitable service."

        if self.ROBOTS_CLASSES[robot_type_key] == MaleRobot:
            if self.SERVICES_CLASSES[service_type_key] != MainService:
                return "Unsuitable service."

        if len(current_service.robots) == current_service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(current_robot)
        current_service.robots.append(current_robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        current_service = self.__find_service(service_name)
        for robot in current_service.robots:
            if robot.name == robot_name:
                current_service.robots.remove(robot)
                self.robots.append(robot)
                return f"Successfully removed {robot_name} from {service_name}."
        raise Exception("No such robot in this service!")

    def feed_all_robots_from_service(self, service_name: str):
        current_service = self.__find_service(service_name)
        number_of_robots_fed = 0

        for robot in current_service.robots:
            robot.eating()
            number_of_robots_fed += 1

        return f"Robots fed: {number_of_robots_fed}."

    def service_price(self, service_name: str):
        current_service = self.__find_service(service_name)
        calculated_price = 0

        for robot in current_service.robots:
            calculated_price += robot.price

        return f"The value of service {service_name} is {calculated_price:.2f}."

    def __str__(self):
        message = "\n".join([service.details() for service in self.services])
        return message
