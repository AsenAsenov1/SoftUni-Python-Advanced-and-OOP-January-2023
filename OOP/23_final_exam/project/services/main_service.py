from project.services.base_service import BaseService


class MainService(BaseService):
    _CAPACITY = 30

    def __init__(self, name: str, capacity=_CAPACITY):
        super().__init__(name, capacity)

    def details(self):
        result = f"{self.name} Main Service:\n"
        if not self.robots:
            result += "Robots: none"
        else:
            result += f"Robots: {', '.join(str(x.name) for x in self.robots)}"

        return result
