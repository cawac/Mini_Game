from game_elements.Field import Field
from game_elements.type_of_blocks.NoneBlock import NoneBlock
from game_elements.Settings import Settings


class Requirements(Field):
    def __init__(self, path_to_background, requirements, x=0, y=0, settings=Settings()):
        super().__init__(path_to_background, len(requirements), 1, x, y)
        for i in range(len(requirements)):
            if requirements[i] is not None:
                self.map[0][i] = NoneBlock(i * settings.block_rect["width"] + 5 * (i + 1), 5, str(requirements[i]))
