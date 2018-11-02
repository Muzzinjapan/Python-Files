## IMPORT AND INITIALISE PYGAME
import pygame
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
pygame.display.set_caption("Lab 09")

## DEFINE ALL VARIABLES
clock = pygame.time.Clock()
done = False
steve_x = 0
steve_y = 0
x_speed = 0
y_speed = 0

## FUNCTIONS

def draw_steve(screen, x, y, eyes):
    ## Steve's Head
    pygame.draw.rect(screen, SKIN, [350+x, 120+y, 80, 80])
    ## Steve's Hair
    pygame.draw.rect(screen, BROWN, [350+x, 120+y, 80, 20])
    pygame.draw.rect(screen, BROWN, [350+x, 140+y, 10, 10])
    pygame.draw.rect(screen, BROWN, [420+x, 140+y, 10, 10])
    ## Steve's Eyes
    if eyes == "right":
        pygame.draw.rect(screen, WHITE, [360+x, 160+y, 10, 10])
        pygame.draw.rect(screen, WHITE, [400+x, 160+y, 10, 10])
        pygame.draw.rect(screen, BLUE, [370+x, 160+y, 10, 10])
        pygame.draw.rect(screen, BLUE, [410+x, 160+y, 10, 10])
    else:
        pygame.draw.rect(screen, WHITE, [370+x, 160+y, 10, 10])
        pygame.draw.rect(screen, WHITE, [410+x, 160+y, 10, 10])
        pygame.draw.rect(screen, BLUE, [360+x, 160+y, 10, 10])
        pygame.draw.rect(screen, BLUE, [400+x, 160+y, 10, 10])
    ## Steve's Nose
    pygame.draw.rect(screen, NOSE_BROWN, [380+x, 170+y, 20, 10])
    ## Steve's Shirt
    pygame.draw.rect(screen, SHIRT_BLUE, [340+x, 200+y, 100, 150])
    pygame.draw.rect(screen, SHIRT_BLUE, [305+x, 200+y, 35, 35])
    pygame.draw.rect(screen, SHIRT_BLUE, [440+x, 200+y, 35, 35])
    ## Steve's Arms
    pygame.draw.rect(screen, SKIN, [310+x, 235+y, 30, 80])
    pygame.draw.rect(screen, SKIN, [440+x, 235+y, 30, 80])
    ## Steve's Pants
    pygame.draw.rect(screen, PANTS_BLUE, [350+x, 350+y, 35, 100])
    pygame.draw.rect(screen, PANTS_BLUE, [395+x, 350+y, 35, 100])




## MAIN PROGRAM LOOP

while not done:
    pos = pygame.mouse.get_pos()
    cursor_x = pos[0]
    cursor_y = pos[1]

    if cursor_x - 390 > steve_x:
        eyes = "right"
    else:
        eyes = "left"

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

    

    steve_x += x_speed
    if steve_x < -310:
        steve_x = -310
    elif steve_x > 530:
        steve_x = 530
    steve_y += y_speed
    if steve_y < -120:
        steve_y = -120
    elif steve_y > 350:
        steve_y = 350
    screen.fill(WHITE)

    draw_steve(screen, steve_x, steve_y, eyes)
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
