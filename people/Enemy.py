from people.Entity import Entity
from LoadSave import LoadSave
from collections import deque
import pygame
class Enemy(Entity):
    def __init__(self,x,y,width,height,level):
        super().__init__(x,y,width,height,level)
        self.walkSpeed = 4
  
        
        
        self._loadAnimations()
        self.initHitbox(48,48)
        self.aniSpeed = 5
    def _loadAnimations(self):
        sprite = LoadSave.get_enemy_atlas(LoadSave.Enemy_ATLAS)
        frame_width = sprite.get_width() // 6
        frame_height = sprite.get_height()

        for i in range(6):
            
            rect = pygame.Rect(i * frame_width, 0, frame_width, frame_height)
            frame = sprite.subsurface(rect)
            new_f = pygame.transform.scale(frame,(int(48*1.5),int(48*1.5)))
       
            self.frames.append(new_f)
  
  

