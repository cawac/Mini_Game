from pygame import image, transform
from random import choice
from game_elements.Field import Field
from game_elements.type_of_blocks.LockedBlock import LockedBlock
from game_elements.type_of_blocks.MovableBlock import MovableBlock
from game_elements.type_of_blocks.NoneBlock import NoneBlock
from game_elements.Settings import Settings


class Board(Field):
    def __init__(self, path_to_background, position_of_locked_blocks, requirements, width_of_field, height_of_field,
                 start_x=0, start_y=0,
                 settings=Settings()):
        super().__init__(path_to_background, width_of_field, height_of_field, start_x, start_y)
        for i in position_of_locked_blocks:
            self.map[i[0]][i[1]] = LockedBlock(i[1] * settings.block_rect["width"] + 5 * (i[1] + 1) + start_x,
                                               i[0] * settings.block_rect["height"] + 5 * (i[0] + 1) + start_y)
        needed_blocks = [i for i in requirements if i is not None for j in range(height_of_field)]
        empty_positions = [(i, j) for i in range(height_of_field) for j in range(width_of_field)
                           if isinstance(self.map[i][j], NoneBlock)]
        while needed_blocks:
            posy, posx = choice(empty_positions)
            type_of_Block = choice(needed_blocks)
            self.map[posy][posx] = MovableBlock(posx * settings.block_rect["width"] + 5 * (posx + 1) + start_x,
                                                posy * settings.block_rect["height"] + 5 * (posy + 1) + start_y,
                                                type_of_Block)
            needed_blocks.remove(type_of_Block)
            empty_positions.remove((posy, posx))
        self.image = image.load(path_to_background)
        self.image = transform.scale(self.image, self.get_size())

    def move(self, pos1, pos2):
        if self.get_block(pos1[0], pos1[1]) is not None:
            block1, block1_line, block1_col = self.get_block(pos1[0], pos1[1])
            block2_col, block2_line = None, None
            if block1 is not None:
                if (block1.rect.x < pos2[0] < block1.rect.x + block1.rect.width) and\
                      (block1.rect.y + block1.rect.height < pos2[1] < self.rect.y + self.rect.height):
                    block2_col = block1_col
                    block2_line = block1_line + 1
                elif (block1.rect.x < pos2[0] < block1.rect.x + block1.rect.width) and\
                      (block1.rect.y > pos2[1] > self.rect.y):
                    block2_col = block1_col
                    block2_line = block1_line - 1
                elif (block1.rect.x > pos2[0] > self.rect.x) and\
                      (block1.rect.y < pos2[1] < block1.rect.height + block1.rect.y):
                    block2_col = block1_col - 1
                    block2_line = block1_line
                elif (block1.rect.x + block1.rect.width < pos2[0] < self.rect.x + self.rect.width) and \
                        (block1.rect.y < pos2[1] < block1.rect.y + block1.rect.height):
                    block2_col = block1_col + 1
                    block2_line = block1_line
            if block2_col is not None and block2_line is not None and 0 <= block2_line <= len(self.map) and 0 <= block2_col <= len(self.map[0]):
                block2 = self.map[block2_line][block2_col]
            else:
                block2 = None
            if block2 is not None:
                if block1.is_movable() and isinstance(block2, NoneBlock):
                    block1.change(block2)
                    self.map[block2_line][block2_col] = block1
                    self.map[block1_line][block1_col] = block2

    def get_block(self, x, y):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j].collide(x, y):
                    return self.map[i][j], i, j
        return None
