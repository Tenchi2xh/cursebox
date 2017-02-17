.. title:: Index

.. image:: _static/logo_animation.gif
   :width: 216px

*Curses made easy*

----

Cursebox is a library based around the curses_ standard module.
Its goal is to avoid the C-like ceremony of curses_ and
provide a modern approach to terminal drawing:

>>> from cursebox import *
>>> with Cursebox() as cb:
...     width, height = cb.width, cb.height
...     greeting = "Hello, World!"
...     # Center text on the screen
...     cb.put(x=(width - len(greeting)) / 2,
...            y=height / 2, text=greeting,
...            fg=colors.black, bg=colors.white)
...     # Wait for any keypress
...     cb.poll_event()

It provides several useful features:

- No setup/teardown
- RGB conversion to terminal 256-colors palette
- Event management

.. _curses: https://docs.python.org/3/library/curses.html

----

.. toctree::
   :maxdepth: 2
   :caption: Contents

   quickstart
   api
