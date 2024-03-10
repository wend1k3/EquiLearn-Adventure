from item.Item import Item
import pygame
from LoadSave import LoadSave
class Book(Item):
    def __init__(self,x,y,knowledge):
        super().__init__(x,y)
        self.knowledge = knowledge
        self.image = LoadSave.get_item_atlas(LoadSave.BOOK_ATLAS)
        self.image = pygame.transform.scale(self.image,(32,32))
    def initHitbox(self, x, y):
        self.hitbox = pygame.Rect(x,y,32,32)
    def getHitbox(self):
        return self.hitbox