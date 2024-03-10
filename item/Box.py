from item.Item import Item
import pygame
from LoadSave import LoadSave
class Box(Item):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.image = LoadSave.get_item_atlas(LoadSave.BOX_ATLAS)
    def initHitbox(self, x, y):
        self.hitbox = pygame.Rect(x,y,32,32)
    def getHitbox(self):
        return self.hitbox
    def draw(self, surface, camera):
        # Assuming the box has an image attribute or similar
        draw_x = self.hitbox.x - camera.x
        draw_y = self.hitbox.y - camera.y
        surface.blit(self.image, (draw_x, draw_y))

        # Optionally draw the hitbox for debugging
        pygame.draw.rect(surface, (255, 0, 0), (draw_x, draw_y, self.hitbox.width, self.hitbox.height), 1)