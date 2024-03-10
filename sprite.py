import pygame

from Level import Level
from Player import Player
from StartScreen import StartScreen


pygame.init()


screen_width, screen_height = 1280, 736
screen = pygame.display.set_mode((screen_width, screen_height))

start_screen = StartScreen(screen)

start_screen.run()
level = Level('test.png') 
player = Player(50,2,int(48*1.5),int(34*1.5),level)
level_size = (level.width * level.tile_size, level.height * level.tile_size)
space = pygame.Rect(0, 0, *level_size)

frame = screen.get_rect()
camera = frame.copy()





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
    camera.center = player.getHitbox().center
    camera.clamp_ip(space) 
  

   
    screen.fill((0, 0, 0))
   
    player.updateAnimationTick()
    player.draw(screen,camera)
    level.draw(screen,camera)


 
    pygame.display.flip()


    clock.tick(60)

pygame.quit()
