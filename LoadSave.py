import pygame
import os
class LoadSave:
    NPC_WHEELCHAIR_ATLAS = "Idle.png"
    BOX_ATLAS = "Box3.png"
    TILE_0_ATLAS = "0.png"
    @staticmethod
    def get_sprite_atlas(file_name):
        try:
            img = pygame.image.load(os.path.join('assets/characters/wheelchair', file_name))
            return img
        except pygame.error as e:
            print(f"Error loading image: {file_name}\n{e}")
            return None
    @staticmethod
    def get_item_atlas(file_name):
        try:
            img = pygame.image.load(os.path.join('assets/item', file_name))
            return img
        except pygame.error as e:
            print(f"Error loading image: {file_name}\n{e}")
            return None

    @staticmethod
    def get_tile_atlas(file_name):
        try:
            img = pygame.image.load(os.path.join('assets/tile', file_name))
            return img
        except pygame.error as e:
            print(f"Error loading image: {file_name}\n{e}")
            return None

