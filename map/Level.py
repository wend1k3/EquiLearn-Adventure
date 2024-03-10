import pygame

from map.Pix import Pix
from LoadSave import LoadSave
import random

class Level:
    def __init__(self, img_path):
        self.img = pygame.image.load(img_path)
        self.width, self.height = self.img.get_size()
 
        self.lvl_data = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.player_spawn = None
        
        self.tile_size = 32
        self.obj =[]
        self.load_level()
    
    def find_grid_coordinates(self):
        grid_coordinates = []  
        for y, row in enumerate(self.lvl_data):
            for x, tile in enumerate(row):
                if tile == Pix.GRID:
                   
                    grid_coordinates.append((x, y)) 
        
        return grid_coordinates
    
    def find_blank_coordinates(self):
        grid_coordinates = []  
        for y, row in enumerate(self.lvl_data):
            for x, tile in enumerate(row):
                if tile == Pix.BLANK:
                 
                    grid_coordinates.append((x, y)) 
        
        return grid_coordinates

    def load_level(self):
        for y in range(self.height):
            for x in range(self.width):
                color = self.img.get_at((x, y))
                red, green, blue = color.r, color.g, color.b
                self.load_level_data(red, x, y)
                self.load_entities(green, x, y)
                self.load_objects(blue, x, y)

    def load_level_data(self, red_value, x, y):
        
        if red_value != 11:
            self.lvl_data[y][x] = Pix.BLANK
        else:
            self.lvl_data[y][x] = Pix.GRID

      
        
    def load_entities(self, green_value, x, y):
   
        pass
        
    

    def load_objects(self, blue_value, x, y):
        if blue_value == 250:
            self.lvl_data[y][x] = Pix.TRAP
            self.recordObject(x*self.tile_size,y*self.tile_size)
    
    def checkSolid(self, x, y):
        maxWidth = len(self.lvl_data[0])*self.tile_size
        if (x< 0 or x>=maxWidth):
            return True
        if (y<0 or y>=720*2):
            return True
        new_x = int(x//self.tile_size)
        new_y = int(y//self.tile_size)
        
       
        return self.lvl_data[new_y][new_x]==Pix.GRID


    def canMove(self,x,y,w,h):
        return (not self.checkSolid(x,y)) and (not self.checkSolid(x+w,y+h)) and (not self.checkSolid(x+w,y)) and (not (self.checkSolid(x,y+h)))
        
    def recordObject(self,x,y):
        self.obj.append((x,y))
    def getObject(self):
        return self.obj

    

 
        
   
    def draw(self, screen, camera):
        for y, row in enumerate(self.lvl_data):
            for x, tile in enumerate(row):
                if tile == Pix.GRID :
                    sprite = LoadSave.get_tile_atlas(LoadSave.TILE_0_ATLAS)
                    screen_x = int(x * self.tile_size - camera.x)
                    screen_y = int(y * self.tile_size - camera.y)
                    screen.blit(sprite,(screen_x,screen_y))
                    
                elif x==5 and y==5:
                    sprite = LoadSave.get_inst_atlas(LoadSave.INST_ATLAS)
                    sprite = pygame.transform.scale(sprite,(sprite.get_width()*2,sprite.get_height()*2))
                    screen_x = int(x * self.tile_size - camera.x)
                    screen_y = int(y * self.tile_size - camera.y)
                    screen.blit(sprite,(screen_x,screen_y))
                elif x==34 and y==1:
                    sprite = LoadSave.get_inst_atlas(LoadSave.INST2_ATLAS)
                    sprite = pygame.transform.scale(sprite,(sprite.get_width()*2,sprite.get_height()*2))
                    screen_x = int(x * self.tile_size - camera.x)
                    screen_y = int(y * self.tile_size - camera.y)
                    screen.blit(sprite,(screen_x,screen_y))
                

    def get_unoccupied_walkable_coordinates(self):
     
        walkable_coordinates = self.find_blank_coordinates()
        unoccupied_coordinates = [coord for coord in walkable_coordinates if coord not in self.obj]
        return unoccupied_coordinates

    def generate_random_items(self, num_items):
    
        unoccupied_coords = self.get_unoccupied_walkable_coordinates()
        for _ in range(num_items):
            if unoccupied_coords:  
                coord = random.choice(unoccupied_coords)
                self.place_item_at(coord)
                unoccupied_coords.remove(coord)  
    def place_item_at(self, coord):
     
        x, y = coord
     
        pixel_x, pixel_y = x * self.tile_size, y * self.tile_size
     
        self.obj.append((pixel_x, pixel_y))
       
   
    
