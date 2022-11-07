from game_elements.Requirements import Requirements
from game_elements.Board import Board
import pygame
from json import load
from game_elements.Settings import Settings


class Game:
    """class for show game and interact with him"""
    def __init__(self, settings=Settings()):
        self.board = None
        self.requirements = None
        self.screen = None
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Nightmare Realm mini-game")
        self.clock = pygame.time.Clock()
        self.settings = settings
        self.sound = pygame.mixer.Sound(self.settings.music)
        self.current_level = 0
        self.load(str(self.current_level))

    def load(self, level):
        """function for loading level"""
        with open(f"levels/{level}.json") as json:
            level = load(json)
            self.screen = pygame.display.set_mode((1, 1))
            self.requirements = Requirements(level["path_to_requirements_bar"], level["requirements"])
            self.board = Board(level["path_to_background_image"], level["position_of_locked_blocks"],
                               level["requirements"], level["columns"], level["lines"], 0,
                               self.requirements.get_rect().height + 10)
            self.screen = pygame.display.set_mode((self.requirements.get_width(),
                                                   self.requirements.get_height() + self.board.get_height() + 10))

    def run(self):
        """main loop of the game"""
        running = True
        self.sound.play(5)
        while running:
            self.clock.tick(self.settings.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos1 = pygame.mouse.get_pos()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        pos2 = pygame.mouse.get_pos()
                    self.board.move(pos1, pos2)
                    if self.is_win():
                        if self.current_level < 4:
                            self.current_level += 1
                            self.load(str(self.current_level))
                        else:
                            running = False
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()
        pygame.quit()

    def draw(self):
        self.requirements.draw(self.screen)
        self.board.draw(self.screen)

    def is_win(self):
        """function for win condition"""
        for i in range(len(self.board.map)):
            for j in range(len(self.board.map[i])):
                if self.requirements.map[0][j] != "None":
                    if self.board.map[i][j] != self.requirements.map[0][j].name:
                        return False
        return True


