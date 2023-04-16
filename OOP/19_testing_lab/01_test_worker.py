from unittest import TestCase, main


class WorkerTests(TestCase):

    def test_worker_is_initialized_correctly(self):
        # Arrange, Act
        worker = Worker("Ivan", 100, 10)

        # Assert
        self.assertEqual("Ivan", worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(10, worker.energy)
        self.assertEqual(0, worker.money)

    def test_energy_is_increased_after_rest(self):
        # Arrange
        worker = Worker("Ivan", 100, 10)
        self.assertEqual(10, worker.energy)

        # Act
        worker.rest()

        # Assert
        self.assertEqual(11, worker.energy)

    def test_worker_tries_to_work_with_zero_energy_raises(self):
        # Arrange
        worker = Worker("Ivan", 100, 0)

        # Act, Assert
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_tries_to_work_with_negative_energy_raises(self):
        # Arrange
        worker = Worker("Ivan", 100, -1)

        # Act, Assert
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_money_increased_by_salary_after_working(self):
        # Arrange
        worker = Worker("Ivan", 100, 10)
        self.assertEqual(0, worker.money)

        # Act
        worker.work()

        # Assert
        self.assertEqual(100, worker.money)

        # Act - допълнителен тест, за да проверим дали не е изпуснат '+' при self.money += self.salary
        worker.work()

        # Assert
        self.assertEqual(200, worker.money)

    def test_energy_decreased_after_working(self):
        # Arrange
        worker = Worker("Ivan", 100, 10)
        self.assertEqual(10, worker.energy)

        # Act
        worker.work()

        # Assert
        self.assertEqual(9, worker.energy)

    def test_get_info_returns_proper_string(self):
        # Arrange
        worker = Worker("Ivan", 100, 10)

        # Act
        result = worker.get_info()
        expected_output = "Ivan has saved 0 money."

        # Assert
        self.assertEqual(expected_output, result)


if __name__ == "__main__":
    main()
