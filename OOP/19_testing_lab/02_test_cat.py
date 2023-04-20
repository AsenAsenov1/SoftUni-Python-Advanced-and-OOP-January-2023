from unittest import TestCase, main


class CatTests(TestCase):


    def test_cat_size_increased_after_eating(self):
        cat = Cat("Tom")
        self.assertEqual(0, cat.size)
        cat.eat()
        self.assertEqual(1, cat.size)

    def test_cat_is_fed_after_eating(self):
        cat = Cat("Tom")
        self.assertFalse(cat.fed)
        cat.eat()
        self.assertTrue(cat.fed)

    def test_cat_cannot_eat_if_already_fed_raises(self):
        cat = Cat("Tom")
        cat.eat()

        with self.assertRaises(Exception) as ex:
            cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_cat_cannot_fall_asleep_if_not_fed_raises(self):
        cat = Cat("Tom")
        self.assertFalse(cat.fed)

        with self.assertRaises(Exception) as ex:
            cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_is_not_sleepy_after_sleeping(self):
        cat = Cat("Tom")
        cat.eat()
        self.assertTrue(cat.sleepy)
        cat.sleep()
        self.assertFalse(cat.sleepy)


if __name__ == "__main__":
    main()