class Entity():
    def __init__(self, position):
        self.position = position

    def is_colliding_with(self, entity):
        return self.position == entity.position

    def is_out_of_screen(self, screen_size):
        return (
            self.position.x >= screen_size.x - 1 or
            self.position.x < 1 or
            self.position.y >= screen_size.y - 1 or
            self.position.y < 1
        )
