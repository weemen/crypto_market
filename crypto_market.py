from curses import wrapper
from finance.broker.litebit import Litebit
from finance.currency import Currency
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


def fetch_currency_data():
    liteBit = Litebit(load_currencies())
    liteBit.fetch_token_data()
    return liteBit.tokens()


def load_currencies():
    config = json.loads(open('config/config.json').read())
    currencies = []
    for token in config['inventory']:
        currency = Currency(token)
        for inventory in config['inventory'][token]['inventory']:
            try:
                currency.addTokens(int(inventory['amount']), float(inventory['buyValue']))
            except ValueError:
                quit_program(("there seems to be a problem with your configuration: double check value at token: %s" % token))
        currencies += [currency]
    return currencies


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


def print_menuWindow(window, label, is_selected):
    color = Color.WHITE_ON_BLACK
    if is_selected:
        color = Color.RED_ON_WHITE

    window.bkgd(' ', Color.set_color(color))
    window.addstr(0, 1, label, curses.color_pair(color))


def is_selected_menu_item(tabindex, menuIndex):
    return (tabindex == menuIndex)


def should_refresh_window(latest_refresh_time):
    return (dt.datetime.now().minute - latest_refresh_time.minute) >= 1


def main(myscreen):
    # Make myscreen.getch non=blocking
    myscreen.nodelay(True)
    myscreen.clear()

    #creating windows and panels
    menuMarket = curses.newwin(1, 8, 0, 5)
    menuMarket.immedok(True)

    menuCurrencies = curses.newwin(1, 17, 0, 14)
    menuCurrencies.immedok(True)

    curses.flushinp()
    myscreen.clear()

    #set default non curses variables
    tabindex     = 0
    maxTabIndex  = 1
    main_screens = {0: print_market}


    tokens = fetch_currency_data()
    latest_refresh_time = dt.datetime.now()

    while True:
        if should_refresh_window(latest_refresh_time):
            latest_refresh_time = dt.datetime.now()
            tokens = fetch_currency_data()
            myscreen.clear()
            main_screens[0](myscreen, tokens)

        pressedCharacter = myscreen.getch()
        # Clear out anything else the user has typed in

        # If the user presses p, increase the width of the springy bar
        if pressedCharacter == ord('q'):
            quit_program()

        if pressedCharacter == ord('\t'):
            tabindex+=1
            if tabindex > maxTabIndex:
                tabindex = 0

        if pressedCharacter == ord('\n'):
            main_screens[0](myscreen, tokens)

        print_menuWindow(menuMarket, "Market", is_selected_menu_item(tabindex, 0))
        print_menuWindow(menuCurrencies, "Edit Currencies", is_selected_menu_item(tabindex, 1))

        myscreen.getch()
        time.sleep(0.1)


wrapper(main)