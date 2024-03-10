import pygame

from Level import Level
from Player import Player
from StartScreen import StartScreen


pygame.init()


screen_width, screen_height = 1280, 736
screen = pygame.display.set_mode((screen_width, screen_height))

start_screen = StartScreen(screen)
canvas = pygame.Surface((screen_width,screen_height))
start_screen.run()
level = Level('test.png') 
player1 = Player(50,2,int(48*1.5),int(34*1.5),level)
player2 = Player(1000,40,int(48*1.5),int(34*1.5),level)
level_size = (level.width * level.tile_size, level.height * level.tile_size)
space = pygame.Rect(0, 0, *level_size)
'''
frame = screen.get_rect()
camera = frame.copy()
'''

p1_cam = pygame.Rect(0,0,screen_width//2,screen_height)
p2_cam = pygame.Rect(screen_width//2,0,screen_width//2,screen_height)

sub1 = canvas .subsurface(p1_cam)
sub2 = canvas .subsurface(p2_cam)


running = True
clock = pygame.time.Clock()
while running:
    screen.fill((0, 0, 0))
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player1.setLeft(True)
                print("A pressed")
            elif event.key == pygame.K_RIGHT:
                player1.setRight(True)
            elif event.key == pygame.K_UP:
                player1.setUp(True)
            elif event.key == pygame.K_DOWN:
                player1.setDown(True)
            if event.key == pygame.K_a:

                player2.setLeft(True)
            elif event.key == pygame.K_d:
                player2.setRight(True)
            elif event.key == pygame.K_w:
                player2.setUp(True)
            elif event.key == pygame.K_s:
                player2.setDown(True)
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player1.setLeft(False)
            elif event.key == pygame.K_RIGHT:
                player1.setRight(False)
            elif event.key == pygame.K_UP:
                player1.setUp(False)
            elif event.key == pygame.K_DOWN:
                player1.setDown(False)
            if event.key == pygame.K_a:
                player2.setLeft(False)
            elif event.key == pygame.K_d:
                player2.setRight(False)
            elif event.key == pygame.K_w:
                player2.setUp(False)
            elif event.key == pygame.K_s:
                player2.setDown(False)
                
            

    
    player1.update()
    player2.update()
    p1_cam.center = player1.getHitbox().center
    p2_cam.center = player2.getHitbox().center
    p1_cam.clamp_ip(space) 
    p2_cam.clamp_ip(space)
    
    canvas.fill((0, 0, 0))
  

   
    
   
    player1.updateAnimationTick()
    level.draw(sub1,p1_cam)
    player1.draw(sub1,p1_cam)
    player2.draw(sub1,p1_cam)

    player2.updateAnimationTick()
    level.draw(sub2,p2_cam)
    player2.draw(sub2,p2_cam)
    player1.draw(sub2,p2_cam)
    


    screen.blit(sub1, (0, 0))
    screen.blit(sub2, (screen_width // 2, 0))
    pygame.display.flip()
    
    

    clock.tick(60)

pygame.quit()
