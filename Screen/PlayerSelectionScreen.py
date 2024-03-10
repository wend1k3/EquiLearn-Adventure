import pygame
from LoadSave import LoadSave
import sys

class AnimatedSprite:
    def __init__(self, flag):
        sprite = LoadSave.get_disable_atlas(LoadSave.IDLE_ATLAS).convert_alpha() if flag else LoadSave.get_enable_atlas(LoadSave.IDLE_ATLAS).convert_alpha()
        frame_width = sprite.get_width() // 4
        frame_height = sprite.get_height()
        self.frames = []
        for i in range(4):
            rect = pygame.Rect(i * frame_width, 0, frame_width, frame_height)
            frame = sprite.subsurface(rect)
            new_f = pygame.transform.scale(frame,(int(frame_width*10),int(frame_height*10)))
            self.frames.append(new_f)


       
        self.current_frame = 0
        self.animation_speed = 0.1  
        self.last_update = pygame.time.get_ticks()
    
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_speed * 1000:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.frames)
    
    def draw(self, surface, position):
        surface.blit(self.frames[self.current_frame], position)


class PlayerSelectionScreen:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width, self.screen_height = screen.get_size()
        
        
        self.avatar_enable = AnimatedSprite(False)
        self.avatar_disable = AnimatedSprite(True)
     
        self.player_choices = []  

    def draw(self, player_number, selected):
        self.screen.fill((0, 0, 0))
        title_font = pygame.font.Font('fonts/monogram.ttf', 40)
        title_text = title_font.render(f'Player {player_number} Choose', True, (255, 255, 255))
        self.screen.blit(title_text, (self.screen_width // 2 - title_text.get_width() // 2, 50))

      
        enable_pos = (self.screen_width // 4 - 50, self.screen_height // 2 - 50)
        disable_pos = (3 * self.screen_width // 4 - 50, self.screen_height // 2 - 50)

        self.avatar_enable.update()
        self.avatar_disable.update()
        
        if selected == 'enable':
            self.avatar_enable.draw(self.screen,enable_pos)
            self.avatar_disable.draw(self.screen,disable_pos)
            pygame.draw.rect(self.screen, (255, 255, 0), (*enable_pos, 100, 100), 3)  # Highlight
        else:
         
            self.avatar_enable.draw(self.screen,enable_pos)
            self.avatar_disable.draw(self.screen,disable_pos)
            pygame.draw.rect(self.screen, (255, 255, 0), (*disable_pos, 100, 100), 3)  # Highlight
        
 
        pygame.display.flip()

    def run(self):
        for player_number in [1, 2]:  
            choosing = True
            selected = 'enable'
            while choosing:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                            selected = 'disable' if selected == 'enable' else 'enable'
                        elif event.key == pygame.K_RETURN:
                            self.player_choices.append(selected)
                            choosing = False
                self.draw(player_number, selected)

        return self.player_choices