from .Block import Block


class NoneBlock(Block):
    def __init__(self, x, y, name="None"):
        super().__init__(x, y, f"images/{name}.png")
        self.name = name

    def is_movable(self):
        return False

