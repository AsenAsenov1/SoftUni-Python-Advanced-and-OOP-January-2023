from unittest import TestCase, main
# from vehicle.project.vehicle import Vehicle
from project.vehicle import Vehicle


class VehicleTests(TestCase):

    def test_default_fuel_consumption(self):
        vehicle = Vehicle(50, 150)

        self.assertEqual(1.25, vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_class_initializes_with_valid_data(self):
        vehicle = Vehicle(10, 150)

        self.assertEqual(10, vehicle.fuel)
        self.assertEqual(10, vehicle.capacity)
        self.assertEqual(150, vehicle.horse_power)
        self.assertEqual(1.25, vehicle.fuel_consumption)

    def test_drive_with_not_enough_fuel_raises(self):
        vehicle = Vehicle(10, 150)

        with self.assertRaises(Exception) as ex:
            vehicle.drive(15)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_with_enough_fuel_reduces_fuel(self):
        vehicle = Vehicle(12.5, 150)

        vehicle.drive(9)
        self.assertEqual(1.25, vehicle.fuel)

        vehicle.drive(1)
        self.assertEqual(0, vehicle.fuel)

    def test_refuel_over_capacity_raises(self):
        vehicle = Vehicle(10, 150)

        with self.assertRaises(Exception) as ex:
            vehicle.refuel(10)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_with_valid_amount_fuel_increase(self):
        vehicle = Vehicle(12.5, 150)

        vehicle.drive(10)
        vehicle.refuel(5)
        self.assertEqual(5, vehicle.fuel)

    def test_str_returns_correct_data(self):
        vehicle = Vehicle(50, 150)

        result = "The vehicle has 150 horse power with 50 fuel left and 1.25 fuel consumption"
        self.assertEqual(result, str(vehicle))


if __name__ == "__main__":
    main()
