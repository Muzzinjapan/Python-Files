## IMPORT AND INITIALISE PYGAME
import pygame
import math
pygame.init()

## COLOURS
BLACK = (0,0,0)
BLUE = (0,0,255)
BROWN = (139,69,19)
GREEN = (0,255,0)
NOSE_BROWN = (106,64,48)
RED = (255,0,0)
SHIRT_BLUE = (0,150,150)
SKIN = (255,205,148)
PANTS_BLUE = (117,105,171)
WHITE = (255,255,255)


## SET THE WIDTH AND HEIGHT OF THE SCREEN
size = (1000,800)
screen = pygame.display.set_mode(size)

## SET THE CAPTION FOR THE GRAPHICS WINDOW
pygame.display.set_caption("Smiley Eyes")

## DEFINE ALL VARIABLES
clock = pygame.time.Clock()
done = False

## FUNCTIONS

def draw_smiley(screen, x, y, eyes):
    
    pygame.draw.circle(screen, BLUE, [500, 400], 300, 0)
    pygame.draw.arc(screen, WHITE, ((400,300),(450,300)), 0, math.pi/2, 20)
    



## MAIN PROGRAM LOOP

while not done:
    pos = pygame.mouse.get_pos()
    cursor_x = pos[0]
    cursor_y = pos[1]

#    if cursor_x - 390 > steve_x:
#        eyes = "right"
#    else:
#        eyes = "left"
#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

#        elif event.type == pygame.KEYDOWN:
#            if event.key == pygame.K_LEFT:
#                x_speed = -3
#            elif event.key == pygame.K_RIGHT:
#                x_speed = 3
#            elif event.key == pygame.K_UP:
#                y_speed = -3
#            elif event.key == pygame.K_DOWN:
#                y_speed = 3


#        elif event.type == pygame.KEYUP:
#            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#                x_speed = 0
#            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
#                y_speed = 0

    

    
    screen.fill(BLACK)

    draw_smiley(screen, 300, 300, 1)
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
