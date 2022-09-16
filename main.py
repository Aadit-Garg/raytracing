# IMPORTS
import pygame
from vars import *
from matrix import *
PLAYER_X,PLAYER_Y = PLR_X,PLR_Y
PLR_LIS = [[65,65]]
map = get_lis_map()

pygame.init()
screen = pygame.display.set_mode((SCREEN_X*2,SCREEN_Y))
# FUNC
def move(direc):
    global PLAYER_X,PLAYER_Y
    if direc == "u" and PLAYER_Y > 60:
        PLAYER_Y -= Y_VEL
    if direc == "d" and PLAYER_Y < 440:
        PLAYER_Y += Y_VEL
    if direc == "r" and PLAYER_X < 440:
        PLAYER_X += X_VEL
    if direc == "l" and PLAYER_X > 60:
        PLAYER_X -= X_VEL

    # print(PLAYER_X,PLAYER_Y)
def draw_map():
    for y in range(len(map)):
        for x in range(len(map)):
            if map[y][x] == 0:colour = (0,0,0)
            else:colour = (255,255,255)
            DRAW_RECT(pygame,screen,colour,((BOX_SIZE*x),(BOX_SIZE*y)))

# LOOP

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    key_input =  pygame.key.get_pressed() 
    if key_input[pygame.K_LEFT]:
        move("l")
    if key_input[pygame.K_UP]:
        move("u")
    if key_input[pygame.K_RIGHT]:
        move("r")
    if key_input[pygame.K_DOWN]:
        move("d")

    DRAW_RECT(pygame,screen,(155,155,155),(0,0),(SCREEN_SIZE))
    draw_map()
    
    PLR_LIS.append([PLAYER_X,PLAYER_Y])
    while len(PLR_LIS) > 20:
        PLR_LIS.remove(PLR_LIS[0])
    for coord in PLR_LIS:
        DRAW_CIRC(pygame,screen,(255,100,100),coord)
    pygame.display.update()