#Task1: Using event handling, move the paddle horizontally using left and right arrow keys.
#apply boundary restrictions, so that the paddle does not leave the window screen.

#Task2: Add clock functionality to the program. keep 60 frames per second.

#You can find the where to do the Task1 by going through the program.

import pygame

# Initialize pygame
pygame.init()

# # Define constants
WIDTH, HEIGHT = 800, 600
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# # Font setup
font = pygame.font.Font(None, 36)

# # Create game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Brick Game')


# Paddle properties
paddle_width = 100
paddle_height = 20
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - paddle_height - 20
paddle_speed = 10


# # Main game loop
running = True
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Add Event Handling for paddle
    #Task1
    
    # # Fill screen with white
    window.fill(WHITE)
    
    # Draw paddle
    pygame.draw.rect(window, BLUE, (paddle_x, paddle_y, paddle_width, paddle_height))
    
    # Update display
    pygame.display.update()
    

# # Quit pygame
pygame.quit()