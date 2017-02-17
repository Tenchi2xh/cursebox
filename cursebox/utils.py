# -*- encoding: utf-8 -*-

import sys
import os

from six.moves import zip_longest


def clamp(n, lower, upper):
    """
    Restricts the given number to a lower and upper bound (inclusive)

    :param n:     input number
    :param lower: lower bound (inclusive)
    :param upper: upper bound (inclusive)
    :return:      clamped number
    """
    if lower > upper:
        lower, upper = upper, lower
    return max(min(upper, n), lower)


def is_native_windows():
    return os.name == "nt" and sys.platform != "cygwin"


def group(n, iterable, fill_value=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fill_value)


def hex_to_rgb(hex_color):
    return (int(hex_color[0:2], 16),
            int(hex_color[2:4], 16),
            int(hex_color[4:6], 16))
