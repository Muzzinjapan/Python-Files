##############################################
##############################################
######                                  ######
######      PYGAME CODING TEMPLATE      ######
######                                  ######
##############################################
##############################################

import pygame

## COLOURS
BLACK = (0,0,0)
BLUE = (0,0,255)
BROWN = (139,69,19)
GREEN = (0,255,0)
RED = (255,0,0)
WHITE = (255,255,255)

pygame.init()

## SET THE WIDTH AND HEIGHT OF THE SCREEN
x_speed = 0
y_speed = 0
x_coord = 0
y_coord = 0

size = (700,500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Chapter 11")

## LOOP UNTIL THE USER CLICKS THE CLOSE BUTTON
done = False

## USED TO MANAGE HOW FAST THE SCREEN UPDATES
clock = pygame.time.Clock()

## ADD FUNCTIONS HERE
def draw_snowman(screen, x, y):
    pygame.draw.ellipse(screen, WHITE, [35+x, 0+y, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [23+x, 20+y, 50, 50])
    pygame.draw.ellipse(screen, WHITE, [0+x, 65+y, 100, 100])

def draw_stick_figure(screen, x, y):
    pygame.draw.ellipse(screen, BLACK, [1+x, y, 10, 10], 0)
    pygame.draw.line(screen, BLACK, [5+x, 17+y], [10+x, 27+y], 2)
    pygame.draw.line(screen, BLACK, [5+x, 17+y], [x, 27+y], 2)
    pygame.draw.line(screen, RED, [5+x, 17+y], [5+x, 7+y], 2)
    pygame.draw.line(screen, RED, [5+x, 7+y], [9+x, 17+y], 2)
    pygame.draw.line(screen, RED, [5+x, 7+y], [1+x, 17+y], 2)

    
#### MAIN PROGRAM LOOP ####
while not done:
    #### MAIN EVENT LOOP ####

    #### GAME LOGIC SECTION ####

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0

    x_coord += x_speed
    y_coord += y_speed

    #### DRAWING SECTION ####

    ## CLEAR THE SCREEN TO WHITE
    screen.fill(WHITE)

    ## DRAWING CODE HERE
    draw_stick_figure(screen,x_coord,y_coord)
    
    ## UPDATE THE SCREEN
    pygame.display.flip()

    ## LIMIT TO 60 FRAMES PER SECOND
    clock.tick(60)

## CLOSE THE WINDOW AND QUIT
pygame.quit()
