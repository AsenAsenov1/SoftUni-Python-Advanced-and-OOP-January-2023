from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TennisPlayerTests(TestCase):

    def test_initialization_with_correct_data(self):
        player = TennisPlayer("Asen", 69, 420)
        self.assertEqual("Asen", player.name)
        self.assertEqual(69, player.age)
        self.assertEqual(420, player.points)
        self.assertEqual([], player.wins)

    def test_name_setter_raises(self):
        with self.assertRaises(ValueError) as ve:
            TennisPlayer("X", 69, 420)
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            TennisPlayer("XY", 69, 420)
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_name_setter_correct(self):
        player = TennisPlayer("Asen", 69, 420)
        self.assertEqual("Asen", player._TennisPlayer__name)

    def test_age_setterraises(self):
        with self.assertRaises(ValueError) as ve:
            TennisPlayer("Asen", 3, 420)
        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_age_setter_correct(self):
        player = TennisPlayer("Asen", 69, 420)
        self.assertEqual(69, player._TennisPlayer__age)

    def test_add_new_win(self):
        player = TennisPlayer("Asen", 69, 420)
        player.add_new_win("HY")
        self.assertEqual(["HY"], player.wins)

    def test_add_new_win_returns(self):
        player = TennisPlayer("Asen", 69, 420)
        player.add_new_win("HY")
        action = player.add_new_win("HY")
        self.assertEqual("HY has been already added to the list of wins!", action)

    def test_lt_method_returns_top(self):
        player_1 = TennisPlayer("Asen", 50, 12)
        player_2 = TennisPlayer("Ilian", 49, 5)
        comparison = player_2.__lt__(player_1)
        self.assertEqual("Asen is a top seeded player and he/she is better than Ilian", comparison)

    def test_lt_method_returns_better(self):
        player_1 = TennisPlayer("Asen", 30, 10.5)
        player_2 = TennisPlayer("Ilian", 35, 8)
        comparison = player_1.__lt__(player_2)
        self.assertEqual('Asen is a better player than Ilian', comparison)

    def test_str_method(self):
        player = TennisPlayer("Asen", 30, 10)
        player.add_new_win("h")
        player.add_new_win("z")
        output = f"Tennis Player: Asen\n" \
                 f"Age: 30\n" \
                 f"Points: 10.0\n" \
                 f"Tournaments won: h, z"
        result = str(player)
        self.assertEqual(output, result)


if __name__ == "__main__":
    main()