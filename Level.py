import pygame

from Pix import Pix
from LoadSave import LoadSave
class Level:
    def __init__(self, img_path):
        self.img = pygame.image.load(img_path)
        self.width, self.height = self.img.get_size()
        # Initialize the level data with zeros (for simplicity)
        self.lvl_data = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.player_spawn = None
        self.load_level()
        self.tile_size = 32
    
    def find_grid_coordinates(self):
        grid_coordinates = []  # List to store coordinates containing Pix.GRID
        for y, row in enumerate(self.lvl_data):
            for x, tile in enumerate(row):
                if tile == Pix.GRID:
                    print(f"Grid found at: ({x}, {y})")  # Print each grid coordinate
                    grid_coordinates.append((x, y))  # Add the coordinate to the list
        
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
        # Example condition for red values (customize as needed)
        '''
        if red_value >= 50:
            self.lvl_data[y][x] = Pix.BLANK  # Wall or obstacle
        else:
            self.lvl_data[y][x] = Pix.GRID# Path
        if (red_value==233):
            self.lvl_data[y][x] = Pix.GRID
        '''
        if red_value != 11:
            self.lvl_data[y][x] = Pix.BLANK
        else:
            self.lvl_data[y][x] = Pix.GRID

      
        
    def load_entities(self, green_value, x, y):
        # Example condition for green values (customize as needed)
        if green_value == 100:
            self.lvl_data[y][x] = Pix.TRAP
    

    def load_objects(self, blue_value, x, y):
        pass
    
    def checkSolid(self, x, y):
        maxWidth = len(self.lvl_data[0])*self.tile_size
        if (x< 0 or x>=maxWidth):
            return True
        if (y<0 or y>=720):
            return True
        new_x = int(x//self.tile_size)
        new_y = int(y//self.tile_size)
        
       
        return self.lvl_data[new_y][new_x]==Pix.GRID


    def canMove(self,x,y,w,h):
        return (not self.checkSolid(x,y)) and (not self.checkSolid(x+w,y+h)) and (not self.checkSolid(x+w,y)) and (not (self.checkSolid(x,y+h)))
        


    

 
        
    '''
    def draw(self, screen):
   
        for y, row in enumerate(self.lvl_data):
            for x, tile in enumerate(row):
                if tile == Pix.GRID:
                    pygame.draw.rect(screen, (255, 0, 0), (x*self.tile_size, y*self.tile_size, self.tile_size, self.tile_size))
                if tile == Pix.TRAP:
                    sprite = LoadSave.get_item_atlas(LoadSave.BOX_ATLAS)
                    screen.blit(sprite,(x,y))
                    print(x,y)
    '''
    def draw(self, screen, camera):
        for y, row in enumerate(self.lvl_data):
            for x, tile in enumerate(row):
                if tile != Pix.BLANK:  # Assuming 0 represents empty space
                    screen_x = x * self.tile_size - camera.x
                    screen_y = y * self.tile_size - camera.y
                    # Only draw the tile if it's within the camera's viewport
                    pygame.draw.rect(screen, (255, 255, 255), (screen_x, screen_y, self.tile_size, self.tile_size))