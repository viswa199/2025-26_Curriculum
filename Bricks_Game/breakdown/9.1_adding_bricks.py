# Set brick settings – number of rows, columns, brick size, and space between bricks on line 41 to 45.
# Create an empty list called bricks to store all the brick blocks on line 48.
# Use a nested loop to go through each row and column from line no 51:
# Calculate the position (x, y) for each brick.
# Create a rectangle for each brick using pygame.Rect().
# Add that brick to the list using bricks.append()
#Brick padding adds space between bricks so they don’t touch each other and look neatly arranged on line 54 and 55.

# Task 1 : Create an empty list name bricks to hold all bricks on line 48.
# Task 2 : Add the brick to the bricks list using append on line 60.


import pygame

# Initialize pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 800, 600
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Font setup
font = pygame.font.Font(None, 36)

# Clock to control the speed (60 FPS)
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

#Brick layout settings
brick_rows = 5
brick_cols = 9
brick_width = 78
brick_height = 20
brick_padding = 10

# Task 1: Create an empty list to hold all bricks


#Create and store each brick using nested loops
for row in range(brick_rows):  # Loop through each row
    for col in range(brick_cols):  # Loop through each column
        # Calculate brick's x and y position
        brick_x = col * (brick_width + brick_padding) + brick_padding
        brick_y = row * (brick_height + brick_padding) + brick_padding

        # Create a brick as a rectangle
        brick = pygame.Rect(brick_x, brick_y, brick_width, brick_height)

        # Task 2 : Add the brick to the bricks list


running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += paddle_speed

    window.fill(WHITE)
    pygame.draw.rect(window, BLUE, [paddle_x, paddle_y, paddle_width, paddle_height])

    # Draw all bricks using a loop
    for brick in bricks:
        pygame.draw.rect(window, BLUE, brick)

    pygame.display.update()
pygame.quit()
