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
size = (700,500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Pygame")

## LOOP UNTIL THE USER CLICKS THE CLOSE BUTTON
done = False

## USED TO MANAGE HOW FAST THE SCREEN UPDATES
clock = pygame.time.Clock()

## ADD FUNCTIONS HERE

#### MAIN PROGRAM LOOP ####
while not done:
    #### MAIN EVENT LOOP ####
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #### GAME LOGIC SECTION ####

    #### DRAWING SECTION ####

    ## CLEAR THE SCREEN TO WHITE
    screen.fill(WHITE)

    ## DRAWING CODE HERE

    
    ## UPDATE THE SCREEN
    pygame.display.flip()

    ## LIMIT TO 60 FRAMES PER SECOND
    clock.tick(60)

## CLOSE THE WINDOW AND QUIT
pygame.quit()
