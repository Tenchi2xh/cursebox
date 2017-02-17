# -*- encoding: utf-8 -*-

from .cursebox import Cursebox
from .colors import colors
from .constants import EVENT_SKIP
from .utils import hex_to_rgb


logo = [u"                    █          ",
        u"█▀█ █ █ █▀█ █▀▀ █▀█ █▀▄ █▀█ █▄█",
        u"█   █ █ █   ▀▀█ █▄█ █ █ █ █ ▄█▄",
        u"█▄█ █▄█ █   ▄▄█ █▄▄ █▄█ █▄█ █ █"]


grey = colors.from_rgb((127, 127, 127))
rainbow = ["ffffff", "ffaaaa", "ff5555", "ff0000",
           "ff6d00", "ffda00", "b6ff00", "48ff00",
           "00ff24", "00ff91", "00ffff", "0091ff",
           "0024ff", "4800ff", "b600ff", "ff00da",
           "ff006d", "ff0000", "ff5555", "ffaaaa"]

prompt = "cursebox v1.0 - Press any key to exit"


def demo():
    l_width, l_height = len(logo[0]), len(logo)
    x_s = 0.4

    palette = [colors.from_rgb(hex_to_rgb(hex)) for hex in rainbow]
    padding = [colors.white] * (int(x_s * l_width) + 3)
    palette = padding + palette + padding

    with Cursebox(blocking_events=False) as cb:
        width, height = cb.width, cb.height

        def draw_logo(t):
            for y0, line in enumerate(logo):
                y1 = (height - l_height) / 2 + y0
                for x0, char in enumerate(line):
                    x1 = x0 + (width - l_width) / 2
                    offset = int(t + y0 + x_s * x0) % len(palette)
                    cb.put(x=x1, y=y1, text=char,
                           fg=palette[offset],
                           bg=colors.transparent)

        t = 0
        l = 100

        cb.put(x=(width - len(prompt)) / 2,
               y=(height + l_height) / 2 + 1,
               text=prompt, fg=grey, bg=colors.transparent)

        while cb.poll_event() == EVENT_SKIP:
            draw_logo(t if t < len(palette) else 0)
            t += 1
            if t > l + len(palette):
                t = 0


if __name__ == "__main__":
    demo()
