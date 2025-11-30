import pygame

from code.Entity import Entity


class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.image_right = self.surf
        self.image_left = pygame.transform.flip(self.surf, True, False)
        self.surf = self.image_right

    def update(self):
        pass

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_RIGHT] and self.rect.x < 705:
            self.rect.x += 9
            self.surf = self.image_right
        if pressed_key[pygame.K_LEFT] and self.rect.x > 15:
            self.rect.x -= 9
            self.surf = self.image_left
        pass
