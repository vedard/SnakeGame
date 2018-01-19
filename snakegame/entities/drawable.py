import curses

from snakegame.entities import Entity


class Drawable(Entity):
    def __init__(self):
        self.appearance = 'X'
        self.color = curses.COLOR_WHITE

    def render(self, screen):
        try:
            screen.addstr(self.position.x, self.position.y,
                          self.appearance, curses.color_pair(self.color))
        except curses.error:
            pass
