#Task1: Create these below variables from line 33 onwards.
#paddle_width = 100, paddle_height = 20, paddle_x = (WIDTH - paddle_width) // 2, paddle_y = HEIGHT - paddle_height - 20
#paddle_speed = 10

#Task2: Create a rect object named "paddle" using above variables.

#Task3: Draw this rect object onto the window screen.

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
#Task1

# # Main game loop
running = True
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # # Fill screen with white
    window.fill(WHITE)
    
    # Draw paddle
    
    # Update display
    pygame.display.update()
    

# # Quit pygame
pygame.quit()