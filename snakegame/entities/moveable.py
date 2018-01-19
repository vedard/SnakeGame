from snakegame.entities import Entity
from snakegame.utilities import Vector


class Moveable(Entity):
    def __init__(self):
        self.velocity = Vector(0, 0)

    def update(self):
        self.position += self.velocity
