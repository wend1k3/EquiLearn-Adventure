import pygame

from map.Level import Level
from people.Player import Player
from Screen.StartScreen import StartScreen
from Screen.PlayerSelectionScreen import PlayerSelectionScreen as PSS

from people.EnemyManager import EnemyManager
from item.ItemManager import ItemManager
from LoadSave import LoadSave
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

font = pygame.font.Font('fonts/monogram.ttf', 40)
em = EnemyManager(level)
em.loadEnemy()
im = ItemManager()
level.generate_random_items(8)
im.loadItems(level.getObject())
running = True
clock = pygame.time.Clock()
last_path_update_time = pygame.time.get_ticks()
last_update_time = pygame.time.get_ticks()
path_update_interval = 1000
game_over = False
bg_img = LoadSave.get_bg_atlas(LoadSave.BG_ATLAS)
bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height))
def draw_end_screen(screen, winner):
    font = pygame.font.Font('fonts/monogram.ttf', 40)
    text_color = (250,35,35)  
    screen_width = 1280
    screen_height = 736

    game_over_text = font.render("End", True, text_color)
    text_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 4))
    screen.blit(game_over_text, text_rect)
    
    if winner:
        winner_text = font.render("Now you understand the importance of cooperation", True, text_color)
    else:
        winner_text = font.render("Nobody wins. Why?", True, text_color)

    winner_rect = winner_text.get_rect(center=(screen_width // 2, screen_height // 4 + 100))
    screen.blit(winner_text, winner_rect)
    
    
    # Display instructions for exiting or replaying
    instructions_font = pygame.font.Font('fonts/monogram.ttf', 40)
    instructions_text = instructions_font.render("Press 'Q' to Quit", True, text_color)
    instructions_rect = instructions_text.get_rect(center=(screen_width // 2, 3 * screen_height // 4))
    screen.blit(instructions_text, instructions_rect)
    
    pygame.display.flip()  # Update the screen with what we've drawn

    
while running:
    #screen.fill((0, 0, 0))
    
    current_time = pygame.time.get_ticks()
    if current_time - last_update_time > 1000:  
        player1.setTime(-1)
        player2.setTime(-1)
        last_update_time = current_time
    if (player1.win or player2.win):
        game_over = True
    elif (player1.time==0 or player2.time==0):
        game_over = True
    

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
              
            elif event.key == pygame.K_f:
                player1.useItem()
            if event.key == pygame.K_p:
                im.checkCollision(player2)
            elif event.key == pygame.K_l:
                player2.useItem()
                    
           
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
    canvas.blit(bg_img, (0, 0))


    
   
    player1.updateAnimationTick()
    
    
    player2.updateAnimationTick()
    em.updateAnimation()
    level.draw(sub1,p1_cam)
    im.drawItem(sub1,p1_cam)
    em.drawEnemy(sub1,p1_cam)
    player1.draw(sub1,p1_cam)
    player2.draw(sub1,p1_cam)
    
    im.drawItem(sub2,p2_cam)
    em.drawEnemy(sub2,p2_cam)
    

    
    level.draw(sub2,p2_cam)

    player2.draw(sub2,p2_cam)
    player1.draw(sub2,p2_cam)
   
  



    screen.blit(sub1, (0, 0))
    screen.blit(sub2, (screen_width // 2, 0))
    pygame.display.flip()
    
    

    clock.tick(60)
    if game_over:
        draw_end_screen(screen, (player1.win and player2.win))
        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting_for_input = False
                    exit(0)
         
                
       

    

pygame.quit()
