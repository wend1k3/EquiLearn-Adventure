from people.Entity import Entity
from LoadSave import LoadSave
import pygame
class Player(Entity):
    def __init__(self,x,y,width,height,level,maxSize,type):
        super().__init__(x,y,width,height,level)
        self.able = type == "enable"
        self.walkSpeed = 2 if not self.able else 6
        
        self.frames = []
        self.current_frame_index = 0
        self._loadAnimations()
        self.initHitbox(40,34)
        self.maxSize = maxSize
        self.bag = []
        self.knowledge = 0
        self.overload = False
        self.maxBrain = 40
        self.aniSpeed=5
        self.time = 10
        self.digit_imgs =  self.digit_images = self.load_digit_images("assets/item/digits/")
        self.win = False
       
    
    @staticmethod
    def load_digit_images(path):
        digit_images = {}
        for i in range(10):
            digit_image = pygame.image.load(f"{path}{i}.png")
            digit_images[str(i)] = digit_image
        return digit_images


    def _loadAnimations(self):
        sprite = LoadSave.get_enable_atlas(LoadSave.WALK_ATLAS) if self.able else LoadSave.get_disable_atlas(LoadSave.IDLE_ATLAS)
        num = 6 if self.able else 4
        frame_width = sprite.get_width() // num
        frame_height = sprite.get_height()
        
      
        for i in range(4):
            
            rect = pygame.Rect(i * frame_width, 0, frame_width, frame_height)
            frame = sprite.subsurface(rect)
            new_f = pygame.transform.scale(frame,(int(48*1.5),int(34*1.5)))
       
            self.frames.append(new_f)
    def addBook(self,book):
        self.knowledge += book.knowledge
        self.overload = True if self.knowledge>self.maxBrain else False
    def addItem(self,item):
        if (len(self.bag)<self.maxSize):
            self.bag.append(item)
            print("add item")
      
    def useItem(self):
        if (not len(self.bag)==0):
            box = self.bag.pop()
            if (box.type=="exam"):
                self.knowledge -= box.value
                if (self.knowledge<0):
                    self.overload = True
            else:
                self.time += box.value
            box.setAlive()
    
    def setTime(self,num):
        self.time += num
    def checkOverLoad(self):
        if self.overload:
            self.walkSpeed *= 0.5
    
    def draw(self,surface,camera):
        super().draw(surface,camera)
        time_str = str(self.time)
        digit_width = self.digit_images['0'].get_width()
        digit_height = self.digit_images['0'].get_height()
        total_width = digit_width * len(time_str)
        
        
        start_x = self.x + self.width / 2 - total_width / 2 - camera.x
        start_y = self.y - digit_height - 10 - camera.y  
        
        for i, digit in enumerate(time_str):
            surface.blit(self.digit_images[digit], (start_x + i * digit_width, start_y))

    def checkAlive(self):
        if (self.x//32==37 and self.y//32==44 and self.time>=0):
            self.win = True
        else:
            self.win = False
            
      
    
   
       