from project.animal import Animal
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: float):
        if price > self.__budget:
            return "Not enough budget"
        elif len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name: str):
        for current_worker in self.workers:
            if current_worker.name == worker_name:
                self.workers.remove(current_worker)
                return f"{current_worker.name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        workers_salaries_sum = sum([worker.salary for worker in self.workers])
        if self.__budget >= workers_salaries_sum:
            self.__budget -= workers_salaries_sum
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_tend = sum([animal.money_for_care for animal in self.animals])

        if self.__budget < total_tend:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= total_tend
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        all_lions = [repr(lion) for lion in self.animals if isinstance(lion, Lion)]
        all_tigers = [repr(tiger) for tiger in self.animals if isinstance(tiger, Tiger)]
        all_cheetahs = [repr(cheetah) for cheetah in self.animals if isinstance(cheetah, Cheetah)]

        output = f"You have {len(self.animals)} animals\n"
        output += f"----- {len(all_lions)} Lions:\n"
        output += "\n".join(all_lions) + "\n"

        output += f"----- {len(all_tigers)} Tigers:\n"
        output += "\n".join(all_tigers) + "\n"

        output += f"----- {len(all_cheetahs)} Cheetahs:\n"
        output += "\n".join(all_cheetahs)

        return output

    def workers_status(self):
        all_keepers = [repr(x) for x in self.workers if isinstance(x, Keeper)]
        all_caretakers = [repr(x) for x in self.workers if isinstance(x, Caretaker)]
        all_vets = [repr(x) for x in self.workers if isinstance(x, Vet)]

        output = f"You have {len(self.workers)} workers\n"
        output += f"----- {len(all_keepers)} Keepers:\n" + "\n".join(all_keepers) + "\n"
        output += f"----- {len(all_caretakers)} Caretakers:\n" + "\n".join(all_caretakers) + "\n"
        output += f"----- {len(all_vets)} Vets:\n" + "\n".join(all_vets)

        return output.strip()
