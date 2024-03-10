from Item import Item
import pygame
class Box(Item):
    def __init__(self,x,y):
        super().__init__(x,y)
    def initHitbox(self, x, y):
        self.hitbox = pygame.Rect(x,y,32,32)