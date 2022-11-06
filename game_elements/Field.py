import pygame
from game_elements.type_of_blocks.NoneBlock import NoneBlock
from App import Settings


class Field(pygame.surface.Surface):
    def __init__(self, path_to_background, width, height, start_x=0, start_y=0):
        self.width_of_field = width
        self.height_of_field = height
        self.block_rect = Settings.Settings("App/settings.json").block_rect
        self.map = tuple([NoneBlock(j * self.block_rect.width + 5 * (j + 1) + start_x,
                                    i * self.block_rect.height + 5 * (i + 1) + start_y) for j in range(self.width_of_field)]
                         for i in range(self.height_of_field))
        super().__init__(
            ((self.block_rect.width * self.width_of_field + 5 * (self.width_of_field + 1)),
             self.block_rect.height * self.height_of_field + 5 * (self.height_of_field + 1)))
        self.image = pygame.image.load(path_to_background)
        self.image = pygame.transform.scale(self.image, self.get_size())
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        for i in self.map:
            for j in i:
                j.draw(screen)

    def __call__(self, pos):
        return self.map[pos]

    def get_pos_of_block(self, x, y):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j].collide(x, y):
                    return i, j
        return None

    def is_adjacent(self, y1, x1, y2, x2):
        if ((y2 - 1 == y1 or y1 == y2 + 1) and x1 == x2) or ((x2 - 1 == x1 or x1 == x2 + 1) and y1 == y2):
            return True
        else:
            return False
