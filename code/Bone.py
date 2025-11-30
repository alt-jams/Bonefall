from code.Entity import Entity


class Bone(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centery += 2
        if self.rect.bottom <= 0:
            self.rect.right = 500