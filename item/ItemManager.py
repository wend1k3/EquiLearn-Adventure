import pygame
from item.Box import Box
class ItemManager:
    def __init__(self):
        self.items = []
    def loadItem(self,items):
        for i in items:
            self.items.append(Box(i[0],i[1]))

    def drawItem(self,surface,camera):
 
        for item in self.items:  # Directly iterate over items
            if item.isAlive():
                hitbox = item.getHitbox()  # Assuming getHitbox returns a pygame.Rect or similar
                draw_x = hitbox.x - camera.x
                draw_y = hitbox.y - camera.y
                surface.blit(item.image, (draw_x, draw_y))  # Assuming each item has an 'image' attribute
                pygame.draw.rect(surface, (255, 0, 0), (draw_x, draw_y, hitbox.width, hitbox.height), 1)
    def checkCollision(self,player):
        for item in self.items:
            if (player.getHitbox().colliderect(item.getHitbox())):
                player.addItem(item)
                item.setAlive()
    
            