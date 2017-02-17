# -*- encoding: utf-8 -*-
# flake8: noqa

from six import iteritems
from six.moves import range


def generate_xterm_256():
    colors = {}
    steps_dim = [0, 128]
    steps_bright = [0, 255]
    steps_rgb = [0, 95, 135, 175, 215, 255]

    def add_colors(steps, start_index, skip=False, reverse=False):
        for r in steps:
            for g in steps:
                for b in steps:
                    if skip:
                        skip = False
                        continue
                    colors[start_index] = (b, g, r) if reverse else (r, g, b)
                    start_index += 1

    add_colors(steps_dim, 0, reverse=True)

    colors[8] = colors[7]
    colors[7] = (192, 192, 192)

    add_colors(steps_bright, 9, skip=True, reverse=True)
    add_colors(steps_rgb, 16)

    for i in range(24):
        colors[232 + i] = tuple([8 + 10 * i] * 3)

    return colors


def remove_duplicate_values(dictionary):
    # Remove duplicate colors by swapping key/values twice
    dictionary = {v: k for k, v in iteritems(dictionary)}
    return {v: k for k, v in iteritems(dictionary)}


XTERM_256 = remove_duplicate_values(generate_xterm_256())


def distance(c1, c2):
    dr = c1[0] - c2[0]
    dg = c1[1] - c2[1]
    db = c1[2] - c2[2]
    return dr * dr + dg * dg + db * db


def closest_color(color, cache={}):
    if color in cache:
        return cache[color]
    else:
        closest = min(XTERM_256, key=lambda k: distance(color, XTERM_256[k]))
        cache[color] = closest
        return closest


def closest_color_dithered(color, x, y, threshold=0.35, cache={}):
    darker = x % 2 ^ y % 2 == 0
    if color in cache:
        dark, bright, f_dark = cache[color]
    else:
        distances = [(k, distance(color, XTERM_256[k])) for k in XTERM_256]
        distances = sorted(distances, key=lambda t: t[1])

        dark, bright = distances[0], distances[1]
        if dark[0] < bright[0]:
            dark, bright = bright, dark

        dist_sum = float(dark[1] + bright[1])
        f_dark = dark[1] / dist_sum

        cache[color] = dark[0], bright[0], f_dark
        dark, bright = dark[0], bright[0]

    if f_dark > threshold:
        return dark if darker else bright
    else:
        return dark
