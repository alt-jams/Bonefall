import random

from code.Bone import Bone
from code.Const import WIN_HEIGHT
from code.Player import Player
from code.Background import Background


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level':
                return Background('game_bg2', (0, 0))
            case 'Player':
                return Player('Player', (10, WIN_HEIGHT - 120))
            case 'Bone':
                return Bone('Bone', (random.randint(15, 705), 0))
        return None

