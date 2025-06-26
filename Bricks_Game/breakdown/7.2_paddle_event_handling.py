# clock.tick(60) controls the speed of the game loop by setting the frame rate to 60 frames per second

# From line 50 to 54 code checks if the left arrow key is pressed
# and moves the paddle left by decreasing its x-position.
# From line 60 to 63 code makes sure the paddle stays inside the screen
# — it stops at the left and right edges so it doesn’t go outside.

# Task 1: Add code to move the paddle right when RIGHT arrow key is pressed

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
paddle_x = (WIDTH - paddle_width) // 2  # Center the paddle horizontally
paddle_y = HEIGHT - paddle_height - 20  # Place paddle near the bottom
paddle_speed = 10  # Speed at which paddle moves

# Add clock for controlling FPS
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    # clock.tick(60) controls the speed of the game loop by setting the frame rate to 60 frames per second
    clock.tick(60)

    # Check for events like closing the game window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle key presses
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:          # If LEFT arrow is pressed
        paddle_x -= paddle_speed     # Move paddle to the left

    # Task 1: Add code to move the paddle right when RIGHT arrow key is pressed


    # Restrict paddle within screen boundaries
    if paddle_x < 0:
        paddle_x = 0  # Stop at the left edge
    if paddle_x > WIDTH - paddle_width:
        paddle_x = WIDTH - paddle_width  # Stop at the right edge

    # Fill screen with white
    window.fill(WHITE)

    # Draw paddle (blue rectangle)
    pygame.draw.rect(window, BLUE, (paddle_x, paddle_y, paddle_width, paddle_height))

    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()
