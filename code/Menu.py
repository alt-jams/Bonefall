#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, MENU_COLOR, MENU_OPTION


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Menu.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./asset/menu_sound.mid')
        pygame.mixer_music.play(-1)

        menu_option = 0

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(60, "BoneFall", MENU_COLOR, ((WIN_WIDTH / 2), 100), True)

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(30, MENU_OPTION[i], MENU_COLOR, ((WIN_WIDTH / 2), 300 + 40 * i), bold=True)
                else:
                    self.menu_text(30, MENU_OPTION[i], MENU_COLOR, ((WIN_WIDTH / 2), 300 + 40 * i), bold=False)

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # ENTER
                        return MENU_OPTION[menu_option]

            pygame.display.flip()




    #     menu_option = 0
    #     pygame.mixer_music.load('./asset/Menu.mp3')
    #     pygame.mixer_music.play(-1)
    #     while True:
    #         # DRAW IMAGES
    #         self.window.blit(source=self.surf, dest=self.rect)
    #         self.menu_text(50, "Mountain", C_ORANGE, ((WIN_WIDTH / 2), 70))
    #         self.menu_text(50, "Shooter", C_ORANGE, ((WIN_WIDTH / 2), 120))
    #
    #         for i in range(len(MENU_OPTION)):
    #             if i == menu_option:
    #                 self.menu_text(20, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
    #             else:
    #                 self.menu_text(20, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))
    #         pygame.display.flip()
    #
    #         # Check for all events
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 pygame.quit()  # Close Window
    #                 quit()  # end pygame
    #             if event.type == pygame.KEYDOWN:
    #                 if event.key == pygame.K_DOWN:  # DOWN KEY
    #                     if menu_option < len(MENU_OPTION) - 1:
    #                         menu_option += 1
    #                     else:
    #                         menu_option = 0
    #                 if event.key == pygame.K_UP:  # UP KEY
    #                     if menu_option > 0:
    #                         menu_option -= 1
    #                     else:
    #                         menu_option = len(MENU_OPTION) - 1
    #                 if event.key == pygame.K_RETURN:  # ENTER
    #                     return MENU_OPTION[menu_option]
    #
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, bold: bool):
        text_font: Font = pygame.font.SysFont(name="papyrus", size=text_size, bold=bold)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
