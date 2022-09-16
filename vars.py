# BASIC VARIABLES
SCREEN_SIZE = (500,500)
SCREEN_X,SCREEN_Y = SCREEN_SIZE[0],SCREEN_SIZE[1]
BOX_SIZE = (SCREEN_X/10)
PLR_X,PLR_Y = 65,65
X_VEL,Y_VEL = 1,1
RED = (255,122,100)



# FUNCTIONS
def DRAW_RECT(pygame,surface,colour,pos,size=(BOX_SIZE-2,BOX_SIZE-2)):
    pygame.draw.rect(surface,colour,(pos,size))
def DRAW_CIRC(pygame,surface,colour,pos,size=10):
    pygame.draw.circle(surface,colour,pos,size)