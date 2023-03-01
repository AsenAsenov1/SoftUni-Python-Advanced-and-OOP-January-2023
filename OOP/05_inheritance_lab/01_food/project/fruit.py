from project.food import Food


class Fruit(Food):
    def __init__(self, name: str, inspiration_date: str, ):
        super().__init__(inspiration_date)
        self.name = name
