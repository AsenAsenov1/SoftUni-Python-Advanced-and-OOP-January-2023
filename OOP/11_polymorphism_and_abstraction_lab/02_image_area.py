"""
Create a class called ImageArea which will store the width and the height of an image. Create a method called get_area()
which will return the area of the image. We have also to implement all the magic methods for comparison of two image areas
(>, >=, <, <=, ==, !=), which will compare their areas.
"""


class ImageArea:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def __gt__(self, other):  # greater (works also for less: '<')
        return self.get_area() > other.get_area()

    def __ge__(self, other):  # greater or equal (works also for less or equal: '<=')
        return self.get_area() >= other.get_area()

    def __eq__(self, other):  # equal (works also for not equal: '!=')
        return self.get_area() == other.get_area()


a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 == a2)
print(a1 != a3)

a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 != a2)
print(a1 >= a3)

a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 <= a2)
print(a1 < a3)