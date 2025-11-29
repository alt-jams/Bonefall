from code.Background import Background
from code.Entity import Entity


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level':
                list_bg = []
                for i in range(1):
                    list_bg.append(Background('game_bg', (0, 0)))
                return list_bg

