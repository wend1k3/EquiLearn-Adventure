from people.Enemy import Enemy

class EnemyManager:
    def __init__(self,level):
        self.loc = [[14*32,24*32],[53*32,20*32]]
        self.ene = []
        self.level = level
    def loadEnemy(self):
        for loc in self.loc:
            new_enemy = Enemy(loc[0], loc[1], int(48*1.5), int(48*1.5), self.level)
            self.ene.append(new_enemy)  
    def updateAnimation(self):
        for ene in self.ene:
            ene.updateAnimationTick()

            
    def drawEnemy(self,surface,camera):
        for ene in self.ene:
            if ene.isAlive():
                ene.draw(surface,camera)
                

            
