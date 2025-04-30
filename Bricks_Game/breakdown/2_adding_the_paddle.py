#This is an end-to-end task that you have to finish by yourself.
#This is basically extending the previous program, so you can use the previous python file.

#Task1: Create a rect object named "paddle" with the following properties.
#paddle_width = 100, paddle_height = 20, paddle_x = (WIDTH - paddle_width) // 2, paddle_y = HEIGHT - paddle_height - 20
#paddle_speed = 10

#Task2: Draw this rect object onto the window screen.

#Task3: Using event handling, move the paddle horizontally using left and right arrow keys.

import pygame

# Initialize pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 800, 600
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Font setup
font = pygame.font.Font(None, 36)

# Create game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Brick Game')


# Paddle properties
paddle_width = 100
paddle_height = 20
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - paddle_height - 20
paddle_speed = 10

# Main game loop
running = True
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Handle keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += paddle_speed
    
    # Fill screen with white
    window.fill(WHITE)
    
    # Draw paddle
    pygame.draw.rect(window, BLUE, [paddle_x, paddle_y, paddle_width, paddle_height])
    
    # Update display
    pygame.display.update()
    

# Quit pygame
pygame.quit()