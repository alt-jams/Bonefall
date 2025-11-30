import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import MENU_COLOR, WIN_WIDTH, WIN_HEIGHT, GAMEOVER_OPTION
from code.Score import Score


class GameOver:

    def __init__(self, window, entities, score, missed):
        self.window = window
        self.entities = entities
        self.score = score
        self.missed = missed

    def run(self):
        clock = pygame.time.Clock()

        overlay = pygame.Surface(self.window.get_size())
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))

        option = 0

        while True:
            clock.tick(60)

            # Adiciona entities como estavam com filtro escuro
            for ent in self.entities:
                self.window.blit(ent.surf, ent.rect)
            self.window.blit(overlay, (0, 0))

            self.draw_text('papyrus', 64, "GAME OVER", MENU_COLOR, ((WIN_WIDTH // 2), WIN_HEIGHT // 2 - 150), True)
            self.draw_text('Lucida Sans Typewriter', 30, f'Score: {self.score}', MENU_COLOR, ((WIN_WIDTH // 2), WIN_HEIGHT // 2 - 20), True)
            self.draw_text('Lucida Sans Typewriter', 30, f'Ossos perdidos: {self.missed}', MENU_COLOR, ((WIN_WIDTH // 2), WIN_HEIGHT // 2 + 20), True)

            for i in range(len(GAMEOVER_OPTION)):
                if i == option:
                    self.draw_text('papyrus',30, GAMEOVER_OPTION[i], MENU_COLOR, ((WIN_WIDTH / 2), 500 + 50 * i), bold=True)
                else:
                    self.draw_text('papyrus',30, GAMEOVER_OPTION[i], MENU_COLOR, ((WIN_WIDTH / 2), 500 + 50 * i), bold=False)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP: # Salvar score
                        option = 0
                    if event.key == pygame.K_DOWN: # menu
                        option = 1
                    if event.key == pygame.K_RETURN: #Enter
                        if option == 0: # salvar score
                            score = Score(self.window)
                            score.save_score(self.score)
                        if option == 1: # Volta pra tela inicial
                            return 'menu'

            pygame.display.flip()

    def draw_text(self, font_name:str, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, bold: bool):
        text_font: Font = pygame.font.SysFont(name=font_name, size=text_size, bold=bold)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)