from snakegame.config import Config
from snakegame.engine import Engine

__version__ = '1.0.0.0'


def main():
    import locale
    locale.setlocale(locale.LC_ALL, '')
    with Engine() as game:
        game.run()
