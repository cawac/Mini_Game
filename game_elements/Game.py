from game_elements.Requirements import Requirements
from game_elements.Board import Board
import pygame
from json import load
from game_elements.NoneBlock import NoneBlock


class Game:
    def __init__(self, settings):
        self.board = None
        self.requirements = None
        self.screen = None
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Nightmare Realm mini-game")
        self.clock = pygame.time.Clock()
        self.settings = settings
        self.load("1")

    def load(self, level):
        with open(f"levels/{level}.json") as json:
            level = load(json)
            self.screen = pygame.display.set_mode((1, 1))  # change to the real resolution
            self.requirements = Requirements(level["path_to_requirements_bar"], level["requirements"])
            self.board = Board(level["path_to_background_image"], level["position_of_locked_blocks"],
                               level["requirements"], level["lines"], level["columns"], 0,
                               self.requirements.get_rect().height + 10)
            self.screen = pygame.display.set_mode((self.requirements.get_width(),
                                                   self.requirements.get_height() + self.board.get_height() + 10))

    def run(self):
        running = True
        while running:
            self.clock.tick(self.settings.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print(pygame.mouse.get_pos())
                        pos1 = self.board.get_pos_of_block(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        print(pygame.mouse.get_pos())
                        pos2 = self.board.get_pos_of_block(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                        self.board.move(pos1, pos2)
                        if self.is_win():
                            running = False
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()
        pygame.quit()

    def draw(self):
        self.requirements.draw(self.screen)
        self.board.draw(self.screen)

    def is_win(self):
        for i in range(len(self.board.map)):
            for j in range(len(self.board.map[i])):
                if self.requirements.map[0][j] != "None":
                    if self.board.map[i][j] != self.requirements.map[0][j].name:
                        return False
        return True