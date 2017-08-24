from curses import wrapper
from finance.broker.litebit import Litebit
from finance.currency import Currency
from finance.config import Config
from finance.exception.invalidConfigurationException import InvalidConfigurationException
from view.color import Color

import curses
import json
import sys
import time
import datetime as dt

def quit_program(message = ''):
    curses.endwin()

    if not message == '':
        print message

    sys.exit()

def print_market(myscreen, tokens):
    header = "|  %s    \t%s\t\t%s\t\t%s\t\t%s %s\t|" % ('Item'.ljust(10), 'Buy'.rjust(13), 'Sell'.rjust(13), 'Avg Buy Value'.rjust(13), 'Balance'.rjust(11), 'Unit bal'.rjust(12))
    myscreen.addstr(3, 5,  "|==========================================================================================================================|")
    myscreen.addstr(4, 5,  header)
    myscreen.addstr(5, 5,  "|==========================================================================================================================|")

    index = 0
    for token in tokens:
        average_value_per_unit = "{:5.6f}".format(token.average())
        balance_per_unit = float(token.sellValue) - token.average()
        balance = "{:10.4f} ({:10.4f})".format((balance_per_unit * token.count()),balance_per_unit)

        line  = "|  %s\t%s EUR\t%s EUR\t%s EUR\t" % (token.label().ljust(10), token.buyValue.rjust(13), token.sellValue.rjust(13), average_value_per_unit.rjust(13))
        balance_line = " %s EUR" % balance.rjust(24)
        closing_line = "|"
        myscreen.addstr((index+6), 5, line)

        if balance_per_unit > 0:
            myscreen.addstr((index+6), 95, balance_line, Color.set_color(Color.GREEN_ON_BLACK))
        else:
            myscreen.addstr((index + 6), 95, balance_line, Color.set_color(Color.RED_ON_BLACK))

        myscreen.addstr((index + 6), 128, closing_line, Color.set_color(Color.WHITE_ON_BLACK))
        index +=1

    myscreen.addstr((index+6), 5, "|==========================================================================================================================|")


def should_refresh_window(latest_refresh_time):
    return (dt.datetime.now().minute - latest_refresh_time.minute) >= 1


def main(myscreen):
    config = Config('config/config.json')
    try:
        config.load()
    except InvalidConfigurationException:
        quit_program(InvalidConfigurationException.message)

    liteBit = Litebit(config.currencies)

    # Make myscreen.getch non=blocking
    myscreen.nodelay(True)
    myscreen.clear()

    curses.flushinp()

    #set default non curses variables
    main_screens = {0: print_market}
    latest_refresh_time = None

    while True:
        if latest_refresh_time is None or should_refresh_window(latest_refresh_time):
            latest_refresh_time = dt.datetime.now()
            myscreen.clear()
            liteBit.fetch_token_data()
            main_screens[0](myscreen, liteBit.tokens())

        pressedCharacter = myscreen.getch()

        # If the user presses p, increase the width of the springy bar
        if pressedCharacter == ord('q'):
            quit_program()

        time.sleep(0.1)


wrapper(main)