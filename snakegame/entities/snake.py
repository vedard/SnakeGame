import curses

from snakegame.entities import Drawable, Moveable, Entity
from snakegame.utilities import Vector


class Snake(Drawable, Moveable, Entity):

    class BodyPart(Drawable, Entity):
        def __init__(self, position):
            self.position = position
            self.color = curses.COLOR_GREEN
            self.appearance = '+'

    def __init__(self, position):
        self.position = position
        self.velocity = Vector(0, -1)
        self.appearance = 'x'
        self.color = curses.COLOR_GREEN
        self.body = [Snake.BodyPart(Vector(-1, -1)),
                     Snake.BodyPart(Vector(-1, -1))]

    def update(self):
        super().update()
        if any(self.body):
            self.body.pop()
            self.body.insert(0, Snake.BodyPart(self.position - self.velocity))

    def render(self, screen):
        super().render(screen)
        for part in self.body:
            part.render(screen)

    def go_left(self):
        self.velocity = self.verify_velocity(Vector(0, -1))

    def go_right(self):
        self.velocity = self.verify_velocity(Vector(0, 1))

    def go_up(self):
        self.velocity = self.verify_velocity(Vector(-1, 0))

    def go_down(self):
        self.velocity = self.verify_velocity(Vector(1, 0))

    def verify_velocity(self, new_velocity):
        # Keep old velocity if we go directly into our body
        if not any(self.body) or self.position + new_velocity != self.body[0].position:
            return new_velocity
        else:
            return self.velocity

    def add_part(self):
        self.body.insert(0, Snake.BodyPart(self.position - self.velocity))

    def is_running_over_himself(self):
        return any([self.is_colliding_with(part) for part in self.body])
