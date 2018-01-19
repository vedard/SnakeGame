import curses

from snakegame.entities import Snake, Fruit
from snakegame import Config


class Playing:
    def __init__(self, engine):
        self.engine = engine
        self.snake = Snake(self.engine.screen_middle())
        self.fruit = Fruit(self.engine.screen_size())
        self.score = 0
        self.collected_fruit = 0
        self.next_score_gain = Config.STARTING_FRUIT_SCORE
        self.engine.delay = Config.STARTING_DELAY
        self.snake.go_left()

    def input(self):
        key = self.engine.screen.getch()
        if key == curses.KEY_UP:
            self.snake.go_up()
        if key == curses.KEY_DOWN:
            self.snake.go_down()
        if key == curses.KEY_LEFT:
            self.snake.go_left()
        if key == curses.KEY_RIGHT:
            self.snake.go_right()
        if key == ord('p'):
            self.engine.pause()
        if key == ord('q'):
            exit()

    def update(self):
        self.snake.update()

        if self.snake.is_colliding_with(self.fruit):
            self.collect_fruit()

        if (self.snake.is_running_over_himself() or
                self.snake.is_out_of_screen(self.engine.screen_size())):
            self.engine.end(self.score)

    def render(self):
        self.engine.screen.erase()
        self.engine.screen.border(0)
        self.snake.render(self.engine.screen)
        self.fruit.render(self.engine.screen)
        self.engine.screen.addstr(0, 2,
                                  f"Score: {self.score:n} | Fruits: {self.collected_fruit}",
                                  curses.color_pair(curses.COLOR_CYAN))
        self.engine.screen.addstr(self.engine.screen_size().x - 1, 2,
                                  f"Control: ← ↑ → ↓  Quit: q  Pause: p",
                                  curses.color_pair(curses.COLOR_CYAN))

    def collect_fruit(self):
        self.collected_fruit += 1
        self.score += self.next_score_gain
        if self.fruit.double_gain:
            self.next_score_gain *= Config.SPECIAL_FRUIT_MULTIPLIER
        self.engine.delay /= Config.DIFICULTY_MULTIPLIER
        self.snake.add_part()
        self.fruit = Fruit(self.engine.screen_size())
