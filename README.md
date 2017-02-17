
<img src=resources/logo_animation.gif width=216/>

*Curses made simple*

<p align="right">
    <a href="https://pypi.python.org/pypi?:action=display&name=cursebox">
        <img height=27 alt="PyPI" src="https://img.shields.io/pypi/v/cursebox.svg">
    </a>
    <a href='http://cursebox.readthedocs.io/en/latest/?badge=latest'>
        <img height=27 src='https://readthedocs.org/projects/cursebox/badge/?version=latest' alt='Documentation Status' />
    </a>
    <a href="https://www.codacy.com/app/Tenchi2xh/cursebox">
        <img height=27 alt="Codacy" src="https://img.shields.io/codacy/cd823f12d6dc4a78a68825d97448ae9f.svg">
    </a>
    <a href="https://travis-ci.org/Tenchi2xh/cursebox">
        <img height=27 alt="Travis-CI" src="https://img.shields.io/travis/Tenchi2xh/cursebox.svg">
    </a>
    <a href="https://github.com/Tenchi2xh/Almonds/releases/tag/1.0">
        <img height=27 alt="Tag" src="https://img.shields.io/badge/tag-1.0-blue.svg">
    </a>
</p>

---

Cursebox is a library based around the [curses](https://docs.python.org/3/library/curses.html) standard module. Its goal is to avoid the C-like ceremony of [curses](https://docs.python.org/3/library/curses.html) and provide a modern approach to terminal drawing:

```python
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
```

It provides several useful features:

- No setup/teardown
- RGB conversion to terminal 256-colors palette
- Event management

Full documentation on [Read the Docs](http://cursebox.readthedocs.io/)

# TODO

- Add on PyPI
- Unit tests
- Finish documentation
- Handmade `curses` module using ANSI escape sequences for Windows replacement
- Add pixel buffer from other project
g