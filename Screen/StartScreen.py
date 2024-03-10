import pygame
import sys

class StartScreen:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self.running = True
        self.font = pygame.font.Font('fonts/monogram.ttf', 40)
        self.title_font = pygame.font.Font('fonts/monogram.ttf', 70)
        self.background_color = (30, 30, 30)
        self.text_color = (255, 255, 255)
        self.title_text = "cmd-f"
        self.menu_items = ["Start", "Options", "Exit"]
        self.selected_item = 0  # Index of the currently selected menu item
        original_background_image = pygame.image.load('background/blackboard.jpg').convert()
        self.background_image = pygame.transform.scale(original_background_image, (self.screen.get_width(), self.screen.get_height()))
     
       


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.selected_item > 0:
                    self.selected_item -= 1
                elif event.key == pygame.K_DOWN and self.selected_item < len(self.menu_items) - 1:
                    self.selected_item += 1
                elif event.key == pygame.K_RETURN:
                    self.select_menu_item()
            

    def select_menu_item(self):
        if self.menu_items[self.selected_item] == "Exit":
            pygame.quit()
            sys.exit()
        elif self.menu_items[self.selected_item] == "Start":
            self.running = False  # Proceed to the game
    
    def draw_menu(self):
        for index, item in enumerate(self.menu_items):
            if index == self.selected_item:
                text = self.font.render(item, True, (128, 128, 128))  # Highlight selected item
            else:
                text = self.font.render(item, True, self.text_color)
            text_rect = text.get_rect(center=(self.screen_width / 2, 2 * self.screen_height / 5 + self.screen_height / 13 * index))
            self.screen.blit(text, text_rect)

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))
        self.draw_title()
        self.draw_menu()
        
    def draw_title(self):
        title_surface = self.title_font.render(self.title_text, True, self.text_color)
        title_rect = title_surface.get_rect(center=(self.screen_width / 2, self.screen_height / 4))
        self.screen.blit(title_surface, title_rect)

    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            pygame.display.flip()
            pygame.time.Clock().tick(60)
