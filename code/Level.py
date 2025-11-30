import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import MENU_COLOR, WIN_HEIGHT, BLACK, EVENT_BONE, EVENT_SPEEDUP, LEVEL_COLOR
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Gameover import GameOver


class Level:

    def __init__(self, window):
        self.window = window
        self.entity_list: list[Entity] = []
        self.entity_list.append(EntityFactory.get_entity('Level'))
        self.entity_list.append(EntityFactory.get_entity('Player'))
        self.bone_delay = 2000  # timer inicial
        pygame.time.set_timer(EVENT_BONE, self.bone_delay)
        pygame.time.set_timer(EVENT_SPEEDUP, 2000)  # a cada 20 seg
        self.show_intro = True
        self.intro_start_time = pygame.time.get_ticks()
        self.score = 0
        self.missed = 0

    def run(self):
        pygame.mixer_music.load('./asset/game_sound.ogg')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(ent.surf, ent.rect)
                ent.move()
            for ent in self.entity_list[:]: # loop pra verificar colisão
                if ent.name == 'Bone':
                    # se colidir com Player
                    player = next(e for e in self.entity_list if e.name == 'Player')
                    if player.rect.colliderect(ent.rect):
                        self.entity_list.remove(ent)
                        self.score += 1
                    if ent.rect.top > WIN_HEIGHT:  # não pegou o osso
                        self.entity_list.remove(ent)
                        self.missed += 1
                        if self.missed >= 5:
                            GameOver(self.window, self.entity_list, self.score, self.missed).run()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_BONE:
                    self.entity_list.append(EntityFactory.get_entity('Bone'))
                if event.type == EVENT_SPEEDUP:
                    if self.bone_delay > 400:  # limite mínimo para não ficar zero
                        self.bone_delay -= 100
                        pygame.time.set_timer(EVENT_BONE, self.bone_delay)
                        print(self.bone_delay)

            if self.show_intro:
                time_passed = pygame.time.get_ticks() - self.intro_start_time
                if time_passed < 2000:
                    self.level_txt(22, 'Pegue o máximo de ossos que puder!', LEVEL_COLOR, (180 , WIN_HEIGHT / 2 + 80))
                else:
                    self.show_intro = False

            #print text
            self.level_txt(14, f'Score: {self.score}', BLACK , (10, 4))
            self.level_txt(14, f'Missed: {self.missed}/5', BLACK , (10, 22))
            pygame.display.flip()

    def level_txt(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size, bold=True)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
