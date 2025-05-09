#Task1: You have created the bricks list in your last assignment.
#Now, Draw all the bricks to the screen using a for loop. Loop through every brick in the bricks list and draw each brick.

#You can find where to start your tasks by going through the code.

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

clock = pygame.time.Clock()

# Create game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Brick Game')


# Paddle properties
paddle_width = 100
paddle_height = 20
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - paddle_height - 20
paddle_speed = 10

# Bricks
brick_rows = 5
brick_cols = 9
brick_width = 78
brick_height = 20
brick_padding = 10

bricks = []

# Create bricks
for row in range(brick_rows):
    for col in range(brick_cols):
        brick_x = col * (brick_width + brick_padding) + brick_padding
        brick_y = row * (brick_height + brick_padding) + brick_padding
        bricks.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))

# Main game loop
running = True
while running:
    clock.tick(60)
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

    #Draw all the bricks using for loop
    #Task1

    # Update display
    pygame.display.update()
    

# Quit pygame
pygame.quit()