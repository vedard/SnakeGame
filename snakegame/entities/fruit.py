import random
import curses

from snakegame import Config
from snakegame.entities import Drawable, Entity
from snakegame.utilities import Vector


class Fruit(Drawable, Entity):
    def __init__(self, screen_size):
        self.appearance = 'o'
        self.position = Vector(random.randint(1, screen_size.x - 2),
                               random.randint(1, screen_size.y - 2))

        self.double_gain = (random.random() > Config.SPECIAL_FRUIT_PROBABILITY)
        if self.double_gain:
            self.color = curses.COLOR_MAGENTA
        else:
            self.color = curses.COLOR_RED
