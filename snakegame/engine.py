import curses
import time

from snakegame import Config
from snakegame.utilities import Vector
from snakegame.gamestates import Playing, Paused, Ended


class Engine:
    def __init__(self):
        self.delay = Config.STARTING_DELAY

    def __enter__(self):
        self.screen = curses.initscr()
        self.screen.nodelay(True)
        self.screen.keypad(True)
        curses.noecho()
        curses.cbreak()
        curses.curs_set(False)
        curses.start_color()
        curses.use_default_colors()
        for i in range(0, curses.COLORS):
            curses.init_pair(i, i, -1)

        return self

    def __exit__(self, type, value, tb):
        self.screen.keypad(False)
        self.screen.nodelay(False)
        curses.nocbreak()
        curses.curs_set(True)
        curses.echo()

    def run(self):
        self.state = Playing(self)
        next_update = time.monotonic()
        while True:
            self.state.input()
            while time.monotonic() > next_update:
                self.state.update()
                next_update += self.delay
            self.state.render()
            time.sleep(0.001)

    def screen_size(self):
        return Vector(*self.screen.getmaxyx())

    def screen_middle(self):
        return self.screen_size() // 2

    def play(self):
        self.state = Playing(self)

    def pause(self):
        self.state = Paused(self, self.state)

    def end(self, score):
        self.state = Ended(self, score)
