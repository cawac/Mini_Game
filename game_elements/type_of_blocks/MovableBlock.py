from game_elements.Block import Block


class MovableBlock(Block):
    def __init__(self, x, y, number_of_type):
        super().__init__(x, y, "images/" + str(number_of_type) + ".png")
        self.name = str(number_of_type)

    def is_movable(self):
        return True
