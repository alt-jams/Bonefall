#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, MENU_COLOR, MENU_OPTION


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Menu2.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./asset/menu_sound.ogg')
        pygame.mixer_music.play(-1)

        menu_option = 0

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(70, "BoneFall", MENU_COLOR, ((WIN_WIDTH / 2), 150), True)
            self.menu_text(23, "Utilize as setas para controlar o personagem", MENU_COLOR, ((WIN_WIDTH / 2), 400), True)
            self.menu_text(20, " <=   =>", MENU_COLOR, ((WIN_WIDTH / 2), 430), True)

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(30, MENU_OPTION[i], MENU_COLOR, ((WIN_WIDTH / 2), 500 + 50 * i), bold=True)
                else:
                    self.menu_text(30, MENU_OPTION[i], MENU_COLOR, ((WIN_WIDTH / 2), 500 + 50 * i), bold=False)

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

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, bold: bool):
        text_font: Font = pygame.font.SysFont(name="papyrus", size=text_size, bold=bold)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
