import pygame

from Level import Level
from Player import Player
from StartScreen import StartScreen


pygame.init()


screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))

start_screen = StartScreen(screen)

start_screen.run()
level = Level('1.png') 
player = Player(2,2,int(48*1.5),int(34*1.5),level)








running = True
clock = pygame.time.Clock()
while running:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.setLeft(True)
            elif event.key == pygame.K_RIGHT:
                player.setRight(True)
            elif event.key == pygame.K_UP:
                player.setUp(True)
            elif event.key == pygame.K_DOWN:
                player.setDown(True)
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.setLeft(False)
            elif event.key == pygame.K_RIGHT:
                player.setRight(False)
            elif event.key == pygame.K_UP:
                player.setUp(False)
            elif event.key == pygame.K_DOWN:
                player.setDown(False)
        
            

    
    player.update()

   
    screen.fill((0, 0, 0))
   
    player.updateAnimationTick()
    player.draw(screen)
    level.draw(screen)


 
    pygame.display.flip()


    clock.tick(60)

pygame.quit()
