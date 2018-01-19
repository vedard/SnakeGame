import re

from setuptools import setup, find_packages


def get_version():
    with open('snakegame/__init__.py') as f:
        version_match = re.search(r"__version__ = '(.*)'", f.read())
    if version_match:
        return version_match.group(1)

    raise RuntimeError("Unable to find version string.")


setup(
    name="SnakeGame",
    license="MIT",
    version=get_version(),
    author="Vincent Bédard",
    description="Snake game",
    long_description="",
    keywords='snake game',
    url="https://github.com/vedard/SnakeGame/",
    packages=find_packages(exclude=["test"]),
    zip_safe=True,
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'snakegame=snakegame:main',
        ],
    },
)
