from pygame import surface, image, transform
from game_elements.type_of_blocks.NoneBlock import NoneBlock
from game_elements import Settings


class Field(surface.Surface):
    """class for show required blocks and game board"""
    def __init__(self, path_to_background, width_of_field, height_of_field, start_x=0, start_y=0, settings = Settings.Settings()):
        self.map = tuple([NoneBlock(j * settings.block_rect["width"] + 5 * (j + 1) + start_x,
                                    i * settings.block_rect["height"] + 5 * (i + 1) + start_y) for j in range(width_of_field)]
                         for i in range(height_of_field))
        super().__init__(
            ((settings.block_rect["width"] * width_of_field + 5 * (width_of_field + 1)),
             settings.block_rect["height"] * height_of_field + 5 * (height_of_field + 1)))
        self.image = image.load(path_to_background)
        self.image = transform.scale(self.image, self.get_size())
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        for i in self.map:
            for j in i:
                j.draw(screen)


