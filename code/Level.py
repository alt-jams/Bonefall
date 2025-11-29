import pygame

from code.Entity import Entity


class Level:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/game_bg.png')
        self.rect = self.surf.get_rect(left=0, top=0)
        self.entity_list: list[Entity] = []

    def run(self, ):
        pygame.mixer_music.load('./asset/game_sound.ogg')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
