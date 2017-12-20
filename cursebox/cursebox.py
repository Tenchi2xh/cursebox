# -*- encoding: utf-8 -*-

import curses
import os
import locale
from threading import Lock

from .constants import *
from .symbols import symbols
from .pairs import Pairs


class Cursebox(object):
    """
    A wrapper for curses which provides simple API calls.

    Instances should be created using the with statement,
    which will take care of initializing the curses environment
    and disposing of it when the context is lost:

    >>> with Cursebox() as cb:
    >>>    cb.put(42, 13, "Hello from curses!", colors.black, colors.white)
    >>>    cb.refresh()

    Cursebox also handles keyboard strokes and events:

    >>> event = cb.poll_event()
    >>> if event == EVENT_CTRL_C:
    >>>     exit()
    """
    def __init__(self, blocking_events=True):
        self.blocking_events = blocking_events

        self.mutex = Lock()
        self.threads = []

    def add_thread(self, thread):
        self.threads.append(thread)
        thread.daemon = True
        thread.start()

    def hide_cursor(self):
        """
        Hides the cursor.
        """
        curses.curs_set(0)

    def set_cursor(self, x, y):
        """
        Sets the cursor to the desired position.

        :param x: X position
        :param y: Y position
        """
        curses.curs_set(1)
        self.screen.move(y, x)

    def refresh(self):
        """
        Refreshes the screen.
        """
        self.mutex.acquire()
        self.screen.refresh()
        self.mutex.release()

    def put(self, x, y, text, fg, bg):
        """
        Puts a string at the desired coordinates using the provided colors.

        :param x:    X position
        :param y:    Y position
        :param text: Text to write
        :param fg:   Foreground color number
        :param bg:   Background color number
        """
        self.mutex.acquire()
        if x < self.width and y < self.height:
            try:
                self.screen.addstr(int(y), int(x),
                                   symbols.encode(text),
                                   self.pairs[fg, bg])
            except curses.error:
                # Ignore out of bounds error
                pass
        self.mutex.release()

    def put_arrow(self, x, y, direction, fg, bg):
        ch = getattr(curses, "ACS_UARROW")
        if direction == "down":
            ch = getattr(curses, "ACS_DARROW")
        if direction == "left":
            ch = getattr(curses, "ACS_LARROW")
        if direction == "right":
            ch = getattr(curses, "ACS_RARROW")

        if x < self.width and y < self.height:
            try:
                self.screen.addch(y, x, ch, self.pairs[fg, bg])
            except curses.error:
                # Ignore out of bounds error
                pass

    @property
    def width(self):
        """
        The width of the current terminal.
        """
        return self.screen.getmaxyx()[1]

    @property
    def height(self):
        """
        The height of the current terminal.
        """
        return self.screen.getmaxyx()[0]

    def clear(self):
        """
        Clears the terminal.
        """
        self.screen.clear()

    def poll_event(self):
        """
        Checks if an event happens and returns a string related to the event.

        Returns -1 if nothing happened during self.screen.timeout milliseconds.

        If the event is a normal (letter) key press,
        the letter is returned (case sensitive)

        :return: Event type
        """
        self.mutex.acquire()
        ch = self.screen.getch()
        self.mutex.release()

        if ch == -1:
            return EVENT_SKIP
        elif ch == 27:
            return EVENT_ESC
        elif ch == curses.KEY_RESIZE:
            return EVENT_RESIZE
        elif ch == 10 or ch == curses.KEY_ENTER:
            return EVENT_ENTER
        elif ch == 127 or ch == curses.KEY_BACKSPACE:
            return EVENT_BACKSPACE
        elif ch == curses.KEY_UP:
            return EVENT_UP
        elif ch == curses.KEY_DOWN:
            return EVENT_DOWN
        elif ch == curses.KEY_LEFT:
            return EVENT_LEFT
        elif ch == curses.KEY_RIGHT:
            return EVENT_RIGHT
        elif ch == 3:
            return EVENT_CTRL_C
        elif ch == 409:
            return EVENT_CLICK
        elif 0 <= ch < 256:
            return chr(ch)
        else:
            return EVENT_UNHANDLED

    def __enter__(self):
        # Default delay when pressing ESC is too long, at 1000ms
        os.environ["ESCDELAY"] = "25"
        self.pairs = Pairs()
        # Make curses use unicode
        locale.setlocale(locale.LC_ALL, "")

        self.screen = curses.initscr()

        curses.noecho()
        # Using raw instead of cbreak() gives us access to CTRL+C and others
        curses.raw()
        self.screen.keypad(True)
        if not self.blocking_events:
            self.screen.timeout(33)
        curses.start_color()
        curses.use_default_colors()
        self.hide_cursor()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # for thread in self.threads:
        #     thread.join()
        curses.noraw()
        self.screen.keypad(False)
        curses.echo()
        curses.endwin()
