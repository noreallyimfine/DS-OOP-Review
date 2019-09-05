import unittest
from players import OPlayer, Quarterback
from possible_values import *
from game import Game
# TODO - some things you can add...

# import the `season` file and make sure generate_random_games only
# makes games with appropriate team names (and never has a team playing itself)

# Complete the FootballGameTest


class FootballGameTest(unittest.TestCase):
    '''test the class'''
    def test_field_goal_made(self):
        game = Game(teams=['h', 'j'])
        score1 = game.score['h']
        game.field_goal('h')
        self.assertEqual(game.score['h'], (score1+3))

    def test_get_winner(self):
        game = Game(teams=['h', 'j'])
        winner = game.teams[0]
        game.get_winning_team()
        self.assertEqual(winner, game.winning_team_)


class FootballPlayerTest(unittest.TestCase):
    '''Check the default values for Player and Quarterback
    yards=120, touchdowns=5, safety=1,
                 interceptions=0
    '''
    def test_default_player_yards(self):
        player = OPlayer(name='Dude')
        self.assertEqual(player.yards, 120)

    def test_player_yards_set_to(self):
        player = OPlayer(name='OtherDude', yards=150)
        self.assertEqual(player.yards, 150)

    def test_default_qb_interceptions(self):
        qb = Quarterback(name='FancyDude')
        self.assertEqual(qb.interceptions, 2)

    def test_default_qb_completed_passes(self):
        qb = Quarterback()
        self.assertEqual(qb.completed_passes, 20)

    def test_passing_score(self):
        qb = Quarterback()
        self.assertEqual((20 - (2 * 3) + 168), qb.passing_score())


if __name__ == '__main__':
    unittest.main()
