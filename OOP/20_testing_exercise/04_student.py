from unittest import TestCase, main
from project.student import Student


# from student.project.student import Student


class StudentTests(TestCase):

    def test_class_initializes_correctly_without_course_data(self):
        student = Student("Boris")

        self.assertEqual("Boris", student.name)
        self.assertEqual({}, student.courses)

    def test_class_initializes_correctly_with_course_data(self):
        student = Student("Boris", {"Math": ["M1", "M2"]})

        self.assertEqual("Boris", student.name)
        self.assertEqual({"Math": ["M1", "M2"]}, student.courses)

    def test_enroll_existing_course_adds_notes(self):
        student = Student("Boris", {"Math": ["M1", "M2"], "Physics": ["P1"]})

        student.enroll("Math", ["M3", "M4"])
        self.assertEqual({"Math": ["M1", "M2", "M3", "M4"], "Physics": ["P1"]}, student.courses)

    def test_enroll_existing_course_returns_message(self):
        student = Student("Boris", {"Math": ["M1", "M2"], "Physics": ["P1"]})

        result = student.enroll("Math", ["M3", "M4"])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_with_add_course_notes_equal_to_y(self):
        student = Student("Boris", {"Math": ["M1", "M2"]})

        student.enroll("Physics", ["P1"], "Y")
        self.assertEqual({"Math": ["M1", "M2"], "Physics": ["P1"]}, student.courses)

    def test_enroll_with_add_course_notes_equal_to_empty_string(self):
        student = Student("Boris", {"Math": ["M1", "M2"]})

        student.enroll("Physics", ["P1"], "")
        self.assertEqual({"Math": ["M1", "M2"], "Physics": ["P1"]}, student.courses)

    def test_enroll_with_add_course_notes_equal_to_y_or_empty_string_returns_message(self):
        student = Student("Boris", {"Math": ["M1", "M2"]})

        result = student.enroll("Physics", ["P1"], "Y")
        self.assertEqual("Course and course notes have been added.", result)

        result_ = student.enroll("Physics", ["P1"], "")
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_without_adding_notes(self):
        student = Student("Boris", {"Math": ["M1", "M2"]})

        student.enroll("Physics", ["P1"], "y")
        self.assertEqual({"Math": ["M1", "M2"], "Physics": []}, student.courses)

    def test_enroll_without_adding_notes_returns_message(self):
        student = Student("Boris", {"Math": ["M1", "M2"]})

        result = student.enroll("Physics", ["P1"], "2")
        self.assertEqual("Course has been added.", result)

    def test_add_notes_with_existing_course_name(self):
        student = Student("Boris", {"Math": ["M1", "M2"]})

        result = student.add_notes("Math", "M3")
        self.assertEqual({"Math": ["M1", "M2", "M3"]}, student.courses)
        self.assertEqual("Notes have been updated", result)

    def test_add_notes_to_invalid_course_name_raises(self):
        student = Student("Boris", {"Math": ["M1", "M2"]})

        with self.assertRaises(Exception) as ex:
            student.add_notes("Physics", "P1")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_with_existing_name(self):
        student = Student("Boris", {"Math": ["M1", "M2"], "Physics": ["P1"]})

        result = student.leave_course("Math")
        self.assertEqual({"Physics": ["P1"]}, student.courses)
        self.assertEqual("Course has been removed", result)

    def test_leave_course_with_invalid_course_name_raises(self):
        student = Student("Boris", {"Math": ["M1", "M2"]})

        with self.assertRaises(Exception) as ex:
            student.leave_course("Physics")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()
