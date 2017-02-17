# -*- encoding: utf-8 -*-

from .palette import closest_color
from .utils import is_native_windows


UNIX_COLORS = {
    "black": 0,
    "red": 1,
    "green": 2,
    "yellow": 3,
    "blue": 4,
    "magenta": 5,
    "cyan": 6,
    "white": 7
}

WIN_COLORS = {
    "black": 0,
    "blue": 1,
    "green": 2,
    "cyan": 3,
    "red": 4,
    "magenta": 5,
    "yellow": 6,
    "white": 7
}


class Colors(object):
    def __init__(self):
        self.dark = True
        self.bright = True
        if is_native_windows():
            self.codes = WIN_COLORS
        else:
            self.codes = UNIX_COLORS

    def toggle_dark(self):
        self.dark = not self.dark

    def toggle_bright(self):
        self.bright = not self.bright

    def default_fg(self):
        if self.dark:
            return self.white
        return 0

    def default_bg(self):
        if self.dark:
            return 0
        return self.white

    @property
    def offset(self):
        return 8 if self.bright else 0

    @property
    def transparent(self):
        return -1

    @property
    def black(self):
        return 0

    @property
    def red(self):
        return self.codes["red"] + self.offset

    @property
    def green(self):
        return self.codes["green"] + self.offset

    @property
    def yellow(self):
        return self.codes["yellow"] + self.offset

    @property
    def blue(self):
        return self.codes["blue"] + self.offset

    @property
    def magenta(self):
        return self.codes["magenta"] + self.offset

    @property
    def cyan(self):
        return self.codes["cyan"] + self.offset

    @property
    def white(self):
        return self.codes["white"] + self.offset

    @staticmethod
    def from_rgb(color):
        return closest_color(color)

colors = Colors()
