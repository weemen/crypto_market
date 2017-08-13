import unittest
import curses
from view.color import Color


class TestColor(unittest.TestCase):

    def test_it_can_has_correct_color_pairs(self):
        self.assertEquals(1, Color.WHITE_ON_BLACK)
        self.assertEquals(2, Color.RED_ON_WHITE)
        self.assertEquals(3, Color.GREEN_ON_BLACK)
        self.assertEquals(4, Color.RED_ON_BLACK)
