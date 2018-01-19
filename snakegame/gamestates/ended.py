import curses


class Ended:
    def __init__(self, engine, score):
        self.engine = engine
        self.line0 = f"{score:n}"
        self.line1 = "Game Over"
        self.line2 = "Press enter to try again"

    def input(self):
        key = self.engine.screen.getch()
        if key == 10:
            self.engine.play()
        if key == ord('q'):
            exit()

    def update(self):
        pass

    def render(self):
        middle = self.engine.screen_middle()

        self.engine.screen.erase()
        self.engine.screen.border(0)
        self.engine.screen.addstr(middle.x - 2, middle.y - len(self.line0) // 2,
                                  self.line0,
                                  curses.color_pair(curses.COLOR_MAGENTA))
        self.engine.screen.addstr(middle.x, middle.y - len(self.line1) // 2,
                                  self.line1,
                                  curses.color_pair(curses.COLOR_RED))
        self.engine.screen.addstr(middle.x + 1, middle.y - len(self.line2) // 2,
                                  self.line2,
                                  curses.color_pair(curses.COLOR_RED))
