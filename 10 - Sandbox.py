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

pygame.display.set_caption("Chapter 10")

## LOOP UNTIL THE USER CLICKS THE CLOSE BUTTON
done = False

## USED TO MANAGE HOW FAST THE SCREEN UPDATES
clock = pygame.time.Clock()

## TREE FUNCTION
def draw_tree(screen,x,y):
    pygame.draw.rect(screen, BROWN, [60+x,170+y,30,45])
    pygame.draw.polygon(screen, GREEN, [[150+x,170+y],[75+x,20+y],[x,170+y]])
    pygame.draw.polygon(screen, GREEN, [[140+x,120+y],[75+x,y],[10+x,120+y]])

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
    draw_tree(screen,0,230)
    draw_tree(screen,200,230)
    draw_tree(screen,400,230)

    ## UPDATE THE SCREEN
    pygame.display.flip()

    ## LIMIT TO 60 FRAMES PER SECOND
    clock.tick(60)

## CLOSE THE WINDOW AND QUIT
pygame.quit()
