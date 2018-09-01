# -*- encoding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r") as f:
    README = f.read()

setup(
    name="cursebox-lib",
    packages=find_packages(),
    version="1.0.0",
    description="Curses made simple",
    long_description=README,
    author="Tenchi",
    author_email="tenchi@team2xh.net",
    url="https://github.com/Tenchi2xh/cursebox",
    project_urls={
        "Documentation": "https://cursebox.readthedocs.io/en/latest/"
    },
    keywords=["terminal", "termbox", "curses"],
    classifiers=[
        "Development Status :: 4 - Beta",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
    install_requires=["six"],
    extras_require={
        "test": ["pytest"]
    }
)
