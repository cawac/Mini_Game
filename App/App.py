from game_elements.Game import Game
from App.Settings import Settings


class App:
    def __init__(self):
        self.settings = Settings()
        self.game = Game(self.settings)

    def run(self):
        self.game.run()
