from unittest import TestCase, main


class IntegerListTests(TestCase):

    def test_is_initialized_correctly_without_data(self):
        # това е args в (), можем да му подадем 0, 1 или много аргументи --> подаваме 0
        integer = IntegerList()
        self.assertEqual([], integer._IntegerList__data)

    def test_init_takes_only_integers(self):
        integer = IntegerList("abcd", 8.1, 9)
        self.assertEqual([9], integer._IntegerList__data)

    def test_get_data_returns_correct_data(self):
        integer = IntegerList("abcd", 8.1, 9)

        integer.get_data()
        self.assertEqual([9], integer._IntegerList__data)

    def test_if_data_not_int_raises(self):
        integer = IntegerList(9)

        with self.assertRaises(ValueError) as ex:
            integer.add("9")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_if_data_is_int_append(self):
        integer = IntegerList(9)

        integer.add(16)
        self.assertEqual([9, 16], integer._IntegerList__data)

    def test_remove_index_is_out_of_range(self):
        integer = IntegerList(9, 7)

        # Greater than the length index
        with self.assertRaises(IndexError) as ex:
            integer.remove_index(5)
        self.assertEqual("Index is out of range", str(ex.exception))

        # Equal of the length index
        with self.assertRaises(IndexError) as ex:
            integer.remove_index(2)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_index_removes_element(self):
        integer = IntegerList(9)

        integer.remove_index(0)
        self.assertEqual([], integer._IntegerList__data)

    def test_remove_index_returns_element_at_the_removed_index(self):
        integer = IntegerList(9)

        result = integer.remove_index(0)
        self.assertEqual(9, result)

    def test_get_index_is_out_of_range_raises(self):
        integer = IntegerList(9)

        with self.assertRaises(IndexError) as ex:
            # Greater than the length index
            integer.get(2)
        self.assertEqual("Index is out of range", str(ex.exception))

        with self.assertRaises(IndexError) as ex:
            # Equal of the length index
            integer.get(1)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_index_returns_the_correct_element(self):
        integer = IntegerList(9)

        result = integer.get(0)
        self.assertEqual(9, result)

    def test_insert_index_is_out_of_range_raises(self):
        integer = IntegerList(9)

        with self.assertRaises(IndexError) as ex:
            integer.insert(5, 5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_invalid_data_type_raises(self):
        integer = IntegerList(9)

        with self.assertRaises(ValueError) as ex:
            integer.insert(0, 'asd')
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_adds_element(self):
        integer = IntegerList(9)

        integer.insert(0, 5)
        self.assertEqual([5, 9], integer._IntegerList__data)

    def test_get_biggest(self):
        integer = IntegerList(9, 6, -456, 987, 15644583, -16)

        result = integer.get_biggest()
        self.assertEqual(15644583, result)

    def test_get_index(self):
        integer = IntegerList(9, 6, -456, 987, 15644583, -16)

        result = integer.get_index(6)
        self.assertEqual(1, result)


if __name__ == "__main__":
    main()
