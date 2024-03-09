from Entity import Entity
from LoadSave import LoadSave
import pygame
class Player(Entity):
    def __init__(self,level):
        super().__init__(2,2,48,48,level)
        self.walkSpeed = 1
        
        self.frames = []
        self.current_frame_index = 0
        self._loadAnimations()
       

    def _loadAnimations(self):
        sprite = LoadSave.get_sprite_atlas(LoadSave.NPC_WHEELCHAIR_ATLAS)
        frame_width = sprite.get_width() // 4
        frame_height = sprite.get_height()
       
      
        for i in range(4):
            # Define the rectangle area to extract (x, y, width, height)
            rect = pygame.Rect(i * frame_width, 0, frame_width, frame_height)
            frame = sprite.subsurface(rect)
            new_f = pygame.transform.scale(frame,(int(48*1.5),int(48*1.5)))
       
            self.frames.append(new_f)
      
      

   
       