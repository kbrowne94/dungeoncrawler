from unittest import TestCase
import Character


class TestCharacter(TestCase):

    def test_set_name(self):
        test_character = Character.Character(10, "Kyle")
        test_character.set_name("keelay")
        self.assertEqual("keelay", test_character.name)

    def test_set_hp(self):
        test_character = Character.Character(10, "Kyle")
        test_character.set_hp(8)
        self.assertEqual(8, test_character.hp)

    def test_get_name(self):
        test_character = Character.Character(10, "kyle")
        self.assertEqual("kyle", test_character.get_name())

    def test_get_hp(self):
        test_character = Character.Character(10, "Kyle")
        self.assertEqual(10, test_character.get_hp())

    def test_get_x_position(self):
        test_character = Character.Character(10, "Kyle")
        self.assertEqual(0, test_character.get_x_position())

    def test_get_y_position(self):
        test_character = Character.Character(10, "Kyle")
        self.assertEqual(0, test_character.get_y_position())

    def test_set_x_position(self):
        test_character = Character.Character(10, "Kyle")
        test_character.set_x_position(7)
        self.assertEqual(7, test_character.x_position)

    def test_set_y_position(self):
        test_character = Character.Character(10, "Kyle")
        test_character.set_y_position(8)
        self.assertEqual(8, test_character.y_position)

    def test_get_alive(self):
        test_character = Character.Character(10, "Kyle")
        self.assertEqual(True, test_character.get_alive())

    def test_set_alive(self):
        test_character = Character.Character(10, "Kyle")
        test_character.set_alive(False)
        self.assertEqual(False, test_character.alive)


