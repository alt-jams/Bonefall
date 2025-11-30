import pygame


class Score:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/score.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save_score(self, score):
        print('save score')
        pygame.mixer_music.load('./asset/menu_sound.mid')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.display.flip()
            pass

    def show_score(self):
        print('show score')
        pygame.mixer_music.load('./asset/menu_sound.mid')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.display.flip()
            pass