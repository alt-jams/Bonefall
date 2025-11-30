import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, GAMEOVER_OPTION
from code.Level import Level
from code.Menu import Menu
from code.Score import Score


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                level = Level(self.window)
                level_return = level.run()
                if level_return == 'menu':
                    continue
            elif menu_return == MENU_OPTION[1]:
                score.show_score()
            elif menu_return == MENU_OPTION[2]:
                pygame.quit()
                quit()
            else:
                pass