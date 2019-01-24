from unittest import TestCase
import die
import random


class TestDie(TestCase):
    def test_get_number_of_sides(self):
        test_die = die.die(7, 6)
        self.assertEqual(7, test_die.get_number_of_sides())

    def test_set_number_of_sides(self):
        test_die = die.die(6, 6)
        test_die.set_number_of_sides(10)
        self.assertEqual(10, test_die.get_number_of_sides())

    def test_get_face_value(self):
        test_die = die.die(6, 7)
        self.assertEqual(7, test_die.get_face_value())

    def test_set_face_value(self):
        test_die = die.die(6, 6)
        test_die.set_face_value(10)
        self.assertEqual(10, test_die.get_face_value())

    def test_roll_die(self):
        test_die = die.die(6, 6)
        random.seed(1)
        self.assertEqual(2, test_die.roll_die())
