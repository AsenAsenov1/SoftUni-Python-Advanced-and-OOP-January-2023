from abc import ABC, abstractmethod


class Animal(ABC):

    @staticmethod
    @abstractmethod
    def make_sound():
        ...


class Dog(Animal):

    @staticmethod
    def make_sound():
        return "woof-woof"


class Cat(Animal):

    @staticmethod
    def make_sound():
        return "meow"


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat, Dog]
animal_sound(animals)

