from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    _INITIAL_WEIGHT = 9

    def __init__(self, name, kind, price, weight=_INITIAL_WEIGHT):
        super().__init__(name, kind, price, weight)

    def eating(self):
        self.weight += 3
