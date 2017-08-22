import unittest
import curses
from view.color import Color


class TestColor(unittest.TestCase):

    def test_it_can_has_correct_color_pairs(self):
        self.assertEqual(1, Color.WHITE_ON_BLACK)
        self.assertEqual(2, Color.RED_ON_WHITE)
        self.assertEqual(3, Color.GREEN_ON_BLACK)
        self.assertEqual(4, Color.RED_ON_BLACK)
