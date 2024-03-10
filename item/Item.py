class Item:
    def __init__(self,x,y):
        self.hitbox = None
        self.alive = True
        self.posx = x
        self.posy = y
        self.initHitbox(self.posx,self.posy)
    def initHitbox(self,x,y):
        self.hitbox.x = x
        self.hitbox.y = y
    def getHitbox(self):
        return self.hitbox
    def setAlive(self):
        self.alive = False
