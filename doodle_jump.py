#Layden Halcomb   March 13, 2023
#Practicing game development by taking curious ideas and implementing them as my own. Enjoy the content!

import pygame, random

pygame.init()

#Library of Game Content

#Color Palletes
white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
gray = (128, 128, 128)
brown = (165,42,42)
red = (255,0,0)
background = white
#Screen Constants
width = 400
height = 600

player = pygame.transform.scale(pygame.image.load('froggy.png'), (50,50))
#rocket_jump = pygame.transform.scale(pygame.image.load('rocket.png'), (10,10))
fps = 60
font = pygame.font.Font('freesansbold.ttf', 16)
game_overfont = pygame.font.Font('freesansbold.ttf', 40)
restart = pygame.font.Font("freesansbold.ttf", 12)
timer = pygame.time.Clock()

#game variables
player_x, player_y = 200, 530
platforms = [[200, 580, 70, 10], [100, 480, 70, 10], [300, 480, 70, 10],[200, 380, 70, 10], [100, 280, 70, 10], [300, 280, 70, 10], [200, 180, 70 ,10], [100,80, 70, 10]]
jump = False
y_change = 0 
x_change = 0
player_speed = 2
score = 0
high_score = 0
game_over = False
score_change = 0 
power_jump = 2
powerup_last = 0 

#create window
window = pygame.display.set_mode([width, height])
pygame.display.set_caption('Froggy Jump!')

#player functions

def check_collisions(rect_list, j):
    """Check block collisions with player"""
    global player_x, player_y, y_change

    for i in range(len(rect_list)):
        if rect_list[i].colliderect([player_x + 5, player_y + 30, 40, 7]) and jump is False and y_change >  0: 
            j = True
    return j 

def update_player(y_pos):
    """Updates players y position for very loop"""
    global jump, y_change

    jump_height = 11
    gravity = .4

    if jump:
        y_change =  -jump_height 
        jump = False
    y_pos += y_change
    y_change += gravity 
    return y_pos

def update_platforms(platform_list, y_pos, change):
    """Updates platform locations"""
    global height, score
    if y_pos < 250 and change < 0:
        for i in range(len(platform_list)):
            platform_list[i][1] -= change
    else:
        pass
    for item in range(len(platform_list)):
        if platform_list[item][1] > height:
            platform_list[item] = [random.randint(50,350),random.randint(-50,-10), 70, 10]
            score += 1

    return platform_list

#def rocketpowerup():
    global rocket_jump, player_x, player_y, y_change
    power_jump -= 1
    y_change = -15






gaming = True 

while gaming:
    timer.tick(fps)
    window.fill(background)
    window.blit(player, (player_x, player_y))
    bloks = []

    score_board = font.render("Score: " + str(score), True, black, background)
    window.blit(score_board, (300, 30))
    highscore_board = font.render("HiScore!: " + str(high_score), True, black, background)
    window.blit(highscore_board, (30, 30))
    game_overdisplay = game_overfont.render("GAME OVER", True, red, background)
    restartdisplay = restart.render("Tap 'SPACE' to restart!", True, blue, background)
    jumpsleft = font.render("SUPA JUMPS: " +str(power_jump), True, black, background)
    window.blit(jumpsleft, (30, 50))

    

    for i in range(len(platforms)):
        blok = pygame.draw.rect(window, brown, platforms[i], 0, 3)
        bloks.append(blok)



    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            gaming = False
        if event.type == pygame.KEYDOWN:
            if event.key is pygame.K_SPACE and game_over:
                game_over = False
                score = 0 
                player_x, player_y = 200, 530
                background = white
                platforms = [[200, 580, 70, 10], [100, 480, 70, 10], [300, 480, 70, 10],[200, 380, 70, 10], [100, 280, 70, 10], [300, 280, 70, 10], [200, 180, 70 ,10], [100, 80, 70, 10]]
                score_change = 0
                power_jump = 3 
                powerup_last = 0 

            if event.key is pygame.K_SPACE and not game_over and power_jump > 0:
                power_jump -= 1
                y_change = -15

            if event.key is pygame.K_a:
                x_change = -player_speed
            if event.key is pygame.K_d:
                x_change = player_speed
        if event.type == pygame.KEYUP:
            if event.key is pygame.K_a:
                x_change = 0
            if event.key is pygame.K_d:
                x_change = 0
    
    jump = check_collisions(bloks, jump)
    player_x += x_change
    
    if player_y < 580:
        player_y = update_player(player_y)
    else:
        game_over = True 
        y_change = 0
        x_change = 0
        window.blit(game_overdisplay, (75,275))
        window.blit(restartdisplay, (100,325))


    platforms = update_platforms(platforms, player_y, y_change)

    if player_x < -10:
        player_x = -10
    elif player_x > 360:
        player_x = 360

    if score > high_score:
        high_score = score
    if score - score_change >= 50:
        score_change = score 
        background = (random.randint(1,255),random.randint(1,255),random.randint(1,255))

    if score - powerup_last >= 50:
        powerup_last = score
        power_jump += 1
    
    pygame.display.flip()
pygame.quit()