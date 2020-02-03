"""
    作者:北辰
    日期:17/05/2019
    功能:为wargame创建单元测试

    5月24日: 新增 test_play,user_input_processor,test_occupy_huts方法
"""

import unittest
from knight import Knight
from orcrider import OrcRider
from abstractgameunit import AbstractGameUnit
from gameutils import weighted_random_selection
from hut import Hut
from attackoftheorcs import AttackOfTheOrcs
from unittest import mock

class TestWarGame(unittest.TestCase):
    """This class contains unit tests for the game Attack of The Orcs."""

    def setUp(self):
        """Overrides the setUp fixture of the superclass."""
        self.knight = Knight()
        self.enemy = OrcRider()

    def test_injured_unit_selection(self):
        """Unit test to verify if the injured unit is
        an instance of class AbstractGameUnit
        """
        for i in range(100):
            injured_unit = weighted_random_selection(self.knight,self.enemy)
            self.assertIsInstance(
                injured_unit,
                AbstractGameUnit,
                "Injured unit must be an instance of AbstractGameUnit"
            )

    def test_play(self):
        """Unit test to verify AttackOfTheOrcs.play method."""
        print("\nCalling test_wargame.test_play..")
        game = AttackOfTheOrcs()
        self.hut_selection_counter = 0
        with mock.patch('builtins.input',new=self.user_input_processor):
            game.play()
            #Create a list that collects information on whether the
            # huts are acquired. It is a boolean list
            acquired_hut_list = [h.is_acquired for h in game.huts]

            # Player wins if all huts are acquired AND the player health
            # is grater than 0.
            if all(acquired_hut_list):
                # All the huts are acquired (winning criteria).
                # check the player's health!
                self.assertTrue(game.player.health_meter > 0)
            else:
                # This is the losing criteria.. Player health can not be
                # positive when he/she loses.
                self.assertFalse(game.player.health_meter > 0)

    def user_input_processor(self,prompt):
        """Simulate user input based on user prompt

        :param prompt: The question asked to the user
        :return: The simulated user input
        """
        # The prompt can be either of the following:
        # 1. "choose a hut number to enter (1-5):"
        # 2. "...continue attack? (y/n):"

        # Check if some keywords exist in the prompt
        if 'hut' in prompt.lower():
            # 'The prompt contains 'hut'..should be asking for a hut number.
            self.hut_selection_counter += 1
            assert self.hut_selection_counter <= 5
            return self.hut_selection_counter
        elif 'attack' in prompt.lower():
            # This prompt should be asking permission to continue attack
            return 'y'
        else:
            raise Exception("Got an unexpected prompt!",prompt)

    def test_occupy_huts(self):
        """Unittest to verify number of huts and the occupants..."""
        game = AttackOfTheOrcs()
        game.setup_game_scenario()

        # Verify that only 5 huts are created.
        self.assertEqual(len(game.huts),5)

        # Huts occupant muse be an instance of a Knight or OrcRider
        # or it could be set to None.
        for hut in game.huts:
            assert((hut.occupant is None) or
                   isinstance(hut.occupant,AbstractGameUnit))

if __name__ == '__main__':
    unittest.main()