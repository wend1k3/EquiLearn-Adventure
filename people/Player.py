from people.Entity import Entity
from LoadSave import LoadSave
import pygame
class Player(Entity):
    def __init__(self,x,y,width,height,level,maxSize):
        super().__init__(x,y,width,height,level)
        self.walkSpeed = 10
        
        self.frames = []
        self.current_frame_index = 0
        self._loadAnimations()
        self.initHitbox(40,34)
        self.maxSize = maxSize
        self.bag = []
       
    

    def _loadAnimations(self):
        sprite = LoadSave.get_sprite_atlas(LoadSave.NPC_WHEELCHAIR_ATLAS)
        frame_width = sprite.get_width() // 4
        frame_height = sprite.get_height()
        
      
        for i in range(4):
            # Define the rectangle area to extract (x, y, width, height)
            rect = pygame.Rect(i * frame_width, 0, frame_width, frame_height)
            frame = sprite.subsurface(rect)
            new_f = pygame.transform.scale(frame,(int(48*1.5),int(34*1.5)))
       
            self.frames.append(new_f)
    def addItem(self,item):
        if (len(self.bag)<self.maxSize):
            self.bag.append(item)
            print("add item")
      
    def useItem(self):
        if (not len(self.bag)==0):
            self.bag.pop().setAlive()
      
      

   
       