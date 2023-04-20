from unittest import TestCase, main


class CarTests(TestCase):
    def test_car_is_initialized_correctly(self):
        car = Car("TestMake", "TestModel", 5, 50)
        self.assertEqual("TestMake", car.make)
        self.assertEqual("TestModel", car.model)
        self.assertEqual(5, car.fuel_consumption)
        self.assertEqual(50, car.fuel_capacity)
        self.assertEqual(0, car.fuel_amount)

    def test_car_invalid_make_raises(self):
        car = Car("TestMake", "TestModel", 5, 50)
        with self.assertRaises(Exception) as ex:
            car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_car_invalid_model_raises(self):
        car = Car("TestMake", "TestModel", 5, 50)
        with self.assertRaises(Exception) as ex:
            car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_car_zero_or_negative_fuel_consumption_raises(self):
        car = Car("TestMake", "TestModel", 5, 50)
        with self.assertRaises(Exception) as ex:
            car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

        car = Car("TestMake", "TestModel", 5, 50)
        with self.assertRaises(Exception) as ex:
            car.fuel_consumption = -5
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_car_zero_or_negative_fuel_capacity_raises(self):
        car = Car("TestMake", "TestModel", 5, 50)
        with self.assertRaises(Exception) as ex:
            car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

        car = Car("TestMake", "TestModel", 5, 50)
        with self.assertRaises(Exception) as ex:
            car.fuel_capacity = -50
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_car_negative_fuel_amount_raises(self):
        car = Car("TestMake", "TestModel", 5, 50)
        with self.assertRaises(Exception) as ex:
            car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_zero_or_negative_fuel_amount_raises(self):
        car = Car("TestMake", "TestModel", 5, 50)
        with self.assertRaises(Exception) as ex:
            car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel(self):
        car = Car("TestMake", "TestModel", 5, 50)
        car.refuel(5)
        self.assertEqual(5, car.fuel_amount)
        car.refuel(5)
        self.assertEqual(10, car.fuel_amount)

    def test_refuel_fuel_amount_bigger_than_fuel_capacity(self):
        car = Car("TestMake", "TestModel", 5, 50)
        car.refuel(55)
        self.assertEqual(50, car.fuel_amount)

    def test_drive_not_enough_fuel_to_drive_raises(self):
        car = Car("TestMake", "TestModel", 5, 50)
        with self.assertRaises(Exception) as ex:
            car.drive(100)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive(self):
        car = Car("TestMake", "TestModel", 5, 50)
        car.refuel(50)
        car.drive(5)
        # needed = (5 /100) * 5 -> 0.25
        self.assertEqual(49.75, car.fuel_amount)


if __name__ == "__main__":
    main()