from game_elements.Block import Block


class NoneBlock(Block):
    """class for empty slots"""
    def __init__(self, x, y, name="None"):
        super().__init__(x, y, f"images/{name}.png")
        self.name = name

    def is_movable(self):
        return False

