from item.Item import Item
import pygame
from LoadSave import LoadSave
import random
class Box(Item):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.image = LoadSave.get_item_atlas(LoadSave.BOX_ATLAS)
        self.image = pygame.transform.scale(self.image,(64,32))
        self.type = random.choice(["exam","timer"])
        self.value = random.randint(1,10)
    def initHitbox(self, x, y):
        self.hitbox = pygame.Rect(x,y,64,32)
    def getHitbox(self):
        return self.hitbox
    