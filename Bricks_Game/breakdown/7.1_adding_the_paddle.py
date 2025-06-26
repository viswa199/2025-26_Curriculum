# pygame.draw.rect → This is a function used to draw rectangles.
# window → The screen where you want to draw the rectangle.
# BLUE → The color of the rectangle (you must define it like BLUE = (0, 0, 255)).

# Task 1 : Draw the paddle on the screen using following syntax on line 46:
#         pygame.draw.rect(window, BLUE, (paddle_x, paddle_y, paddle_width, paddle_height))


import pygame

# Initialize pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)  # RGB value for blue

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

    # Fill screen with white
    window.fill(WHITE)

    # Task 1 - Draw paddle (using BLUE color)


    # Update display
    pygame.display.update()

# Quit pygame
pygame.quit()
