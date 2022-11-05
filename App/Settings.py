from json import load
from game_elements import Rect


class Settings:
    def __init__(self, path_to_settings):
        self.FPS = 60
        with open(path_to_settings, "r") as file:
            config = load(file)
            self.block_rect = Rect.Rect(width=config["block_rect"][2], height=config["block_rect"][3])

