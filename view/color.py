import curses


class Color:

    WHITE_ON_BLACK = 1
    RED_ON_WHITE = 2
    GREEN_ON_BLACK = 3
    RED_ON_BLACK = 4

    @staticmethod
    def set_color(color_pair):
        curses.init_pair(Color.WHITE_ON_BLACK, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(Color.RED_ON_WHITE, curses.COLOR_RED, curses.COLOR_WHITE)
        curses.init_pair(Color.GREEN_ON_BLACK, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(Color.RED_ON_BLACK, curses.COLOR_RED, curses.COLOR_BLACK)

        return curses.color_pair(color_pair)
