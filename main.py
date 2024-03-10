import pygame

from map.Level import Level
from people.Player import Player
from Screen.StartScreen import StartScreen
from Screen.PlayerSelectionScreen import PlayerSelectionScreen as PSS

from people.EnemyManager import EnemyManager
from item.ItemManager import ItemManager

pygame.init()



screen_width, screen_height = 1280, 736
screen = pygame.display.set_mode((screen_width, screen_height))

start_screen = StartScreen(screen)
PS = PSS(screen)
canvas = pygame.Surface((screen_width,screen_height))
start_screen.run()
player_choices = PS.run()

level = Level('test1.png') 
player1 = Player(50,2,int(48*1.5),int(34*1.5),level,10,player_choices[0])
player2 = Player(1000,40,int(48*1.5),int(34*1.5),level,10,player_choices[1])
level_size = (level.width * level.tile_size, level.height * level.tile_size)
space = pygame.Rect(0, 0, *level_size)


p1_cam = pygame.Rect(0,0,screen_width//2,screen_height)
p2_cam = pygame.Rect(screen_width//2,0,screen_width//2,screen_height)

sub1 = canvas .subsurface(p1_cam)
sub2 = canvas .subsurface(p2_cam)

#enemy = Enemy(50,100,int(48*1.5),int(48*1.5),level)
em = EnemyManager(level)
em.loadEnemy()
im = ItemManager()
level.generate_random_items(8)
im.loadItems(level.getObject())
running = True
clock = pygame.time.Clock()
last_path_update_time = pygame.time.get_ticks()
path_update_interval = 1000

while running:
    current_time = pygame.time.get_ticks()
    screen.fill((0, 0, 0))
   

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player2.setLeft(True)
              
            elif event.key == pygame.K_RIGHT:
                player2.setRight(True)
            elif event.key == pygame.K_UP:
                player2.setUp(True)
            elif event.key == pygame.K_DOWN:
                player2.setDown(True)
            if event.key == pygame.K_a:

                player1.setLeft(True)
            elif event.key == pygame.K_d:
                player1.setRight(True)
            elif event.key == pygame.K_w:
                player1.setUp(True)
            elif event.key == pygame.K_s:
                player1.setDown(True)
            if event.key == pygame.K_e:
                
              
                im.checkCollision(player1)
                print(player1.knowledge)
            if event.key == pygame.K_p:
                im.checkCollision(player2)
                    
           
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player2.setLeft(False)
            elif event.key == pygame.K_RIGHT:
                player2.setRight(False)
            elif event.key == pygame.K_UP:
                player2.setUp(False)
            elif event.key == pygame.K_DOWN:
                player2.setDown(False)
            if event.key == pygame.K_a:
                player1.setLeft(False)
            elif event.key == pygame.K_d:
                player1.setRight(False)
            elif event.key == pygame.K_w:
                player1.setUp(False)
            elif event.key == pygame.K_s:
                player1.setDown(False)
                
            
   
    
    player1.update()
    player2.update()
 
    p1_cam.center = player1.getHitbox().center
    p2_cam.center = player2.getHitbox().center
 
    p1_cam.clamp_ip(space) 
    p2_cam.clamp_ip(space)
    

    canvas.fill((0, 0, 0))
    


    
   
    player1.updateAnimationTick()
    #enemy.updateAnimationTick()
    player2.updateAnimationTick()
    level.draw(sub1,p1_cam)
    im.drawItem(sub1,p1_cam)
    em.drawEnemy(sub1,p1_cam)
    player1.draw(sub1,p1_cam)
    player2.draw(sub1,p1_cam)
    #enemy.draw(sub1,p1_cam)
    im.drawItem(sub2,p2_cam)
    em.drawEnemy(sub2,p2_cam)
    

    
    level.draw(sub2,p2_cam)

    player2.draw(sub2,p2_cam)
    player1.draw(sub2,p2_cam)
   
  



    screen.blit(sub1, (0, 0))
    screen.blit(sub2, (screen_width // 2, 0))
    pygame.display.flip()
    
    

    clock.tick(60)
    

pygame.quit()
