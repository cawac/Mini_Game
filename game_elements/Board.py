from pygame import image, transform
from random import choice
from game_elements.Field import Field
from game_elements.type_of_blocks.LockedBlock import LockedBlock
from game_elements.type_of_blocks.MovableBlock import MovableBlock
from game_elements.type_of_blocks.NoneBlock import NoneBlock
from App.Settings import Settings

class Board(Field):
    def __init__(self, path_to_background, position_of_locked_blocks, requirements, n, m, start_x=0, start_y=0, settings = Settings()):
        super().__init__(path_to_background, n, m, start_x, start_y)
        for i in position_of_locked_blocks:
            self.map[i[0]][i[1]] = LockedBlock(i[1] * settings.block_rect["width"] + 5 * (i[1] + 1) + start_x,
                                               i[0] * settings.block_rect["height"] + 5 * (i[0] + 1) + start_y)
        needed_blocks = [i for i in requirements if i is not None for j in range(self.height_of_field)]
        empty_positions = [(i, j) for i in range(self.height_of_field) for j in range(self.width_of_field)
                           if isinstance(self.map[i][j], NoneBlock)]
        while needed_blocks:
            posy, posx = choice(empty_positions)
            type_of_Block = choice(needed_blocks)
            self.map[posy][posx] = MovableBlock(posx * settings.block_rect["width"] + 5 * (posx + 1) + start_x,
                                                posy * settings.block_rect["height"] + 5 * (posy + 1) + start_y, type_of_Block)
            needed_blocks.remove(type_of_Block)
            empty_positions.remove((posy, posx))
        self.image = image.load(path_to_background)
        self.image = transform.scale(self.image, self.get_size())

    def move(self, pos1, pos2):
        if pos1 is not None and pos2 is not None:
            y1, x1 = pos1
            y2, x2 = pos2
            block1 = self.map[y1][x1]
            block2 = self.map[y2][x2]
            if block1 is not None and block2 is not None and block1 is not block2:
                if self.is_adjacent(y1, x1, y2, x2):
                    if block1.is_movable() and isinstance(block2, NoneBlock):
                        block1.change(block2)
                        self.map[y2][x2] = block1
                        self.map[y1][x1] = block2


