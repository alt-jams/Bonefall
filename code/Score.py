from datetime import datetime

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import MENU_COLOR, WIN_WIDTH
from code.DBProxy import DBProxy


class Score:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/score.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save_score(self, score):
        pygame.mixer_music.load('./asset/menu_sound.mid')
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ''

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.draw_score('Lucida Sans Typewriter', 30, 'Salvar Score', MENU_COLOR, ((WIN_WIDTH / 2) - 110, 25), True)
            self.draw_score('Lucida Sans Typewriter', 30, f'Score: {score}', MENU_COLOR, ( 30, 200), False)
            self.draw_score('Lucida Sans Typewriter', 30, f'Digite seu nome: ', MENU_COLOR, (30 , 250), False)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(name) <= 8:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        return 'menu'
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) <= 8:
                            name += event.unicode

            self.draw_score('Lucida Sans Typewriter', 30, f'Digite seu nome: {name}', MENU_COLOR, (30, 250), False)
            pygame.display.flip()
            pass

    def show_score(self):
        print('show score')
        pygame.mixer_music.load('./asset/menu_sound.mid')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)

        while True:
            self.draw_score('Lucida Sans Typewriter', 30, 'Salvar Score', MENU_COLOR, ((WIN_WIDTH / 2) - 110, 25), True)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.display.flip()


    def draw_score(self, font_name:str, text_size: int, text: str, text_color: tuple, pos: tuple, bold: bool):
        text_font: Font = pygame.font.SysFont(name=font_name, size=text_size, bold=bold)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=pos[0], top=pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%Y")
    return f'{current_date} - {current_time}'