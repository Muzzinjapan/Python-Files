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
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()


## Generate 50 snowflake positions
snow_list = []

for i in range(2000):
    x = random.randrange(0, 700)
    y = random.randrange(0, 700)
    snow_list.append([x, y])


x_min = -3
x_max = 4
size = 2
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # User pressed down on a key
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_min -= 1
                x_max -= 1
            elif event.key == pygame.K_RIGHT:
                x_max += 1
                x_min += 1
            elif event.key == pygame.K_UP:
                size += 1
            elif event.key == pygame.K_DOWN:
                size -= 1
                if size < 1:
                    size = 1
            
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here

    ## Process each snow flake in the list
    for i in range(len(snow_list)):
        # Draw the snow flake
        x_wiggle = random.randrange(x_min,x_max)
        y_wiggle = random.randrange(0,4)
        pygame.draw.circle(screen, WHITE, snow_list[i], size)

        # Move the snow flake down one pixel
        snow_list[i][1] += y_wiggle
        snow_list[i][0] += x_wiggle

        # If the snow flake has moved off the bottom of the screen
        if snow_list[i][1] > 500:
            # Reset it just above the top
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            # Give it a new x position
            x = random.randrange(0, 700)
            snow_list[i][0] = x
    
    
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
