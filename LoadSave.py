import pygame
import os
class LoadSave:
    NPC_WHEELCHAIR_ATLAS = "Idle.png"

    @staticmethod
    def get_sprite_atlas(file_name):
        try:
            img = pygame.image.load(os.path.join('assets/characters/wheelchair', file_name))
            return img
        except pygame.error as e:
            print(f"Error loading image: {file_name}\n{e}")
            return None
