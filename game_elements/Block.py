from pygame import image, sprite


class Block(sprite.Sprite):
    def __init__(self, x, y, path_to_image):
        super().__init__()
        self.image = image.load(path_to_image).convert_alpha()
        self.image.set_colorkey(-1) # Use the upper-left pixel color as transparent
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = None

    def is_movable(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def collide(self, x, y):
        if (self.rect.x + self.image.get_rect().width > x > self.rect.x) and \
                (self.rect.y + self.image.get_rect().height > y > self.rect.y):
            return True
        else:
            return False

    def change(self, other):
        buffer = other.rect
        other.rect = self.rect
        self.rect = buffer

    def __eq__(self, name):
        if self.name == name:
            return True
        else:
            return False
