import pygame
import os
class LoadSave:
 
    Enemy_ATLAS = "walk.png"
    BOX_ATLAS = "Box3.png"
    BOOK_ATLAS = "book.png"
    TILE_0_ATLAS = "0.png"
    IDLE_ATLAS = "idle.png"
    WALK_ATLAS = "walk.png"
    INST_ATLAS = "inst.png"
    INST2_ATLAS = "inst2.png"
    @staticmethod
    def get_disable_atlas(file_name):
        try:
            img = pygame.image.load(os.path.join('assets/characters/player/disable', file_name))
            return img
        except pygame.error as e:
            print(f"Error loading image: {file_name}\n{e}")
            return None
    @staticmethod
    def get_enable_atlas(file_name):
        try:
            img = pygame.image.load(os.path.join('assets/characters/player/enable', file_name))
            return img
        except pygame.error as e:
            print(f"Error loading image: {file_name}\n{e}")
            return None
    @staticmethod
    def get_enemy_atlas(file_name):
        try:
            img = pygame.image.load(os.path.join('assets/characters/enemy', file_name))
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
    
    @staticmethod
    def get_inst_atlas(file_name):
        try:
            img = pygame.image.load(os.path.join('assets/bg', file_name))
            return img
        except pygame.error as e:
            print(f"Error loading image: {file_name}\n{e}")
            return None
    
