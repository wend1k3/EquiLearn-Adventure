from Direction import Direction
from EntityState import EntityState
from Level import Level
import pygame
class Entity:
    def __init__(self,x,y,width,height,level):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dir = Direction.NONE
        self.walkSpeed = 0
        self.state = EntityState.IDLE
        self.frames = []
        self.aniTick = 0
        self.aniSpeed = 10
        self.aniIndex = 0
        self.flipX = 1
        self.flipW = 1
        self.up = False
        self.down = False
        self.right = False
        self.left = False
        self.canMove = True
        self.level = level
        self.scale_factor = 1.5
        self.hitbox = pygame.Rect(self.x,self.y,self.width,self.height)
    def move(self):
        if ((self.left or self.right)and ((not self.right) or (not self.left))):
            if (self.left and (not self.right)):
                self._moveLeft()
            if (self.right and (not self.left)):
                self._moveRight()
        elif ((self.up or self.down)and ((not self.down) or (not self.up))):
            if (self.up and (not self.down)):
                self._moveUp()
            if (self.down and (not self.up)):
                self._moveDown()
    def update(self):
        self.updateDirection()  # Determine the new direction based on input
        self.checkCanMove()     # Check if movement is possible in the new direction
        if self.canMove:
            self.move()         # Move if allowed
      

    def updateDirection(self):
        # Reset direction to NONE if no movement keys are pressed
        if not (self.up or self.down or self.left or self.right):
            self.dir = Direction.NONE
        else:
            if self.left:
                self.dir = Direction.LEFT
            elif self.right:
                self.dir = Direction.RIGHT
            if self.up:
                self.dir = Direction.UP
            elif self.down:
                self.dir = Direction.DOWN
    '''
    def update(self):
    
        self.checkCanMove()
        if (self.canMove):
            self.move()
        self.dir= Direction.NONE
        
    '''

    
    def checkCanMove(self):
        new_x, new_y = self.x, self.y
        if self.dir == Direction.LEFT:
            new_x -= self.walkSpeed
        elif self.dir == Direction.RIGHT:
            new_x += self.walkSpeed
        elif self.dir == Direction.UP:
            new_y -= self.walkSpeed
        elif self.dir == Direction.DOWN:
            new_y += self.walkSpeed

           
        
        if self.level.canMove(new_x, new_y, self.width, self.height):
            self.setCanMove(True)
        else:
            self.setCanMove(False)

            
            
        
    def _moveRight(self):
        self.x += self.walkSpeed
        self.flipX = 0
        self.flipW = 1
        self.dir = Direction.RIGHT
    def _moveLeft(self):
        self.x -= self.walkSpeed
        self.flipX = self.width
        self.flipW = -1
        self.dir = Direction.LEFT
    def _moveUp(self):
        self.y -= self.walkSpeed
        self.dir = Direction.UP
    def _moveDown(self):
        self.y += self.walkSpeed
        self.dir = Direction.DOWN
    def updateAnimationTick(self):
        self.aniTick+=1
        if (self.aniTick>=self.aniSpeed):
            self.aniTick = 0
            self.aniIndex+=1
            if (self.aniIndex >= 4):
                self.aniIndex = 0
    '''
    def draw(self, surface):
        frame  = self.frames[self.aniIndex]
        if self.flipW == -1:
            frame = pygame.transform.flip(frame,True,False)
  
        surface.blit(frame, (self.x, self.y))
    '''
    def draw(self, surface):
        frame = self.frames[self.aniIndex]
        if self.flipW == -1:
            frame = pygame.transform.flip(frame, True, False)
        
        surface.blit(frame, (self.x, self.y))

        # Draw the hitbox around the sprite for visual debugging
        # Create a temporary Rect for drawing purposes since self.x and self.y are used instead of self.hitbox
        temp_hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(surface, (255, 0, 0), temp_hitbox, 1)

   

    def setRight(self,flag):
        self.right = flag
    def setLeft(self,flag):
        self.left = flag
    def setUp(self,flag):
        self.up= flag
    def setDown(self,flag):
        self.down = flag
    def setCanMove(self,flag):
        self.canMove = flag
    






