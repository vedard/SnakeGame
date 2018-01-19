import curses


class Paused:
    def __init__(self, engine, playing_state):
        self.text = "Paused"
        self.engine = engine
        self.playing_state = playing_state

    def input(self):
        key = self.engine.screen.getch()
        if key == 10 or key == ord('p'):
            self.engine.state = self.playing_state
        if key == ord('q'):
            exit()

    def update(self):
        pass

    def render(self):
        middle = self.engine.screen_middle()
        self.engine.screen.erase()
        self.engine.screen.border(0)
        self.engine.screen.addstr(middle.x, middle.y - len(self.text) // 2,
                                  self.text,
                                  curses.color_pair(curses.COLOR_RED))
