	
"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SKIN = (255,205,148)
BROWN = (43,30,13)
BLUE = (82,61,137)
NOSE_BROWN = (106,64,48)
SHIRT_BLUE = (0,150,150)
YELLOW = (255, 255, 0)
SKY_BLUE = (81,185,248)
PANTS_BLUE = (117,105,171)
GRASS_GREEN = (128,186,66)

# Initialise the game engine 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Animation")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
    
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(SKY_BLUE)
 
    # --- Drawing code should go here

    x_move = 0
    y_move = 0
    change_x = 1
    change_y = 1

    while True:
        
        ## The Sky
        pygame.draw.rect(screen, SKY_BLUE, [0, 0, 700, 400])

        ## The Ground (Grass)
        pygame.draw.rect(screen, GRASS_GREEN, [0, 400, 700, 100])

        ## Steve's Head
        pygame.draw.rect(screen, SKIN, [350 + x_move, 120 + y_move, 80, 80])

        ## Steve's Hair
        pygame.draw.rect(screen, BROWN, [350 + x_move, 120 + y_move, 80, 20])
        pygame.draw.rect(screen, BROWN, [350 + x_move, 140 + y_move, 10, 10])
        pygame.draw.rect(screen, BROWN, [420 + x_move, 140 + y_move, 10, 10])

        ## Steve's Eyes
        pygame.draw.rect(screen, WHITE, [360 + x_move, 160 + y_move, 10, 10])
        pygame.draw.rect(screen, WHITE, [410 + x_move, 160 + y_move, 10, 10])
        pygame.draw.rect(screen, BLUE, [370 + x_move, 160 + y_move, 10, 10])
        pygame.draw.rect(screen, BLUE, [400 + x_move, 160 + y_move, 10, 10])

        ## Steve's Nose
        pygame.draw.rect(screen, NOSE_BROWN, [380 + x_move, 170 + y_move, 20, 10])

        ## Steve's Shirt
        pygame.draw.rect(screen, SHIRT_BLUE, [340 + x_move, 200 + y_move, 100, 150])
        pygame.draw.rect(screen, SHIRT_BLUE, [305 + x_move, 200 + y_move, 35, 35])
        pygame.draw.rect(screen, SHIRT_BLUE, [440 + x_move, 200 + y_move, 35, 35])

        ## Steve's Arms
        pygame.draw.rect(screen, SKIN, [310 + x_move, 235 + y_move, 30, 80])
        pygame.draw.rect(screen, SKIN, [440 + x_move, 235 + y_move, 30, 80])

        ## Steve's Pants
        pygame.draw.rect(screen, PANTS_BLUE, [350 + x_move, 350 + y_move, 35, 100])
        pygame.draw.rect(screen, PANTS_BLUE, [395 + x_move, 350 + y_move, 35, 100])

        ## The Sun
        pygame.draw.ellipse(screen, YELLOW, [20,20,100,100], 50)

        x_move += change_x
        y_move += change_y
        
        if x_move > 200:
            change_x *= -1

        if x_move < -200:
            change_x *= -1

        if y_move > 20:
            change_y *= -1

        if y_move < -20:
            change_y *= -1
        
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
        # --- Limit to 60 frames per second
        clock.tick(60)
 
# Close the window and quit.
pygame.quit()
