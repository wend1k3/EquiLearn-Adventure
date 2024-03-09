import pygame
import sys

class Level:
    def __init__(self, img_path):
        self.img = pygame.image.load(img_path)
        self.width, self.height = self.img.get_size()
        # Initialize the level data with zeros (for simplicity)
        self.lvl_data = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.player_spawn = None
        self.load_level()
    
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
        if red_value >= 50:
            self.lvl_data[y][x] = 0  # Wall or obstacle
        else:
            self.lvl_data[y][x] = red_value # Path
        if (red_value==233):
            self.lvl_data[y][x] = -1
      

    def load_entities(self, green_value, x, y):
        # Example condition for green values (customize as needed)
        if green_value == 100:
            self.player_spawn = (x, y)

    def load_objects(self, blue_value, x, y):
        # Example condition for blue values (customize as needed)
        pass  # Implement object loading logic here if needed

    def draw(self, screen):
        # Example drawing logic (customize as needed)
        for y, row in enumerate(self.lvl_data):
            for x, tile in enumerate(row):
                if tile == 1:
                    pygame.draw.rect(screen, (255, 0, 0), (x * 10, y * 10, 10, 10))

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Load the level
level = Level('1.png')  # Update path to your level image

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Clear the screen with black
    level.draw(screen)  # Draw the level
    pygame.display.flip()  # Update the display

    clock.tick(60)  # Cap the frame rate to 60 FPS

pygame.quit()
sys.exit()
