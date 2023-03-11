from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []  # empty  list of customer objects
        self.trainers = []  # empty list of trainer objects
        self.equipment = []  # empty list of equipment objects
        self.plans = []  # empty list of plan objects
        self.subscriptions = []  # empty list of subscription objects

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription_obj = self.__find_instance_by_id(subscription_id, self.subscriptions)
        customer_obj = self.__find_instance_by_id(subscription_id, self.customers)
        trainer_obj = self.__find_instance_by_id(subscription_id, self.trainers)
        equipment_obj = self.__find_instance_by_id(subscription_id, self.equipment)
        plan_obj = self.__find_instance_by_id(subscription_id, self.plans)
        info = '\n'.join(
            [repr(subscription_obj), repr(customer_obj), repr(trainer_obj), repr(equipment_obj), repr(plan_obj)])

        return info

    @staticmethod
    def __find_instance_by_id(instance_id, list_of_objects):
        return [x for x in list_of_objects if x.id == instance_id][0]
