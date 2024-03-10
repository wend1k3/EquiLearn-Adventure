import pygame
import random
from item.Box import Box
from item.Book import Book
import pygame
import random

class ItemManager:
    def __init__(self):
        self.items = []  


    def loadItems(self, coordinates):
        for coord in coordinates:
            if random.choice(["box", "book"]) == "box":
                self.items.append(Box(coord[0], coord[1]))
            else:
                self.items.append(Book(coord[0], coord[1], random.randint(1, 10)))
           

    def drawItem(self, surface, camera):

        for item in self.items:
            if item.isAlive():
                hitbox = item.getHitbox()
                draw_x = hitbox.x - camera.x
                draw_y = hitbox.y - camera.y
                surface.blit(item.image, (draw_x, draw_y))
                pygame.draw.rect(surface, (255, 0, 0), (draw_x, draw_y, hitbox.width, hitbox.height), 1)

    def checkCollision(self, player):
        for item in self.items:  
            if player.getHitbox().colliderect(item.getHitbox()):
                if isinstance(item, Box):
                    player.addItem(item)
                elif isinstance(item, Book):
                    player.addBook(item)  
                item.setAlive() 
