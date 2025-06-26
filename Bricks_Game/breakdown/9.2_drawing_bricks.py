#for brick in bricks:
#This goes through each brick in the bricks list one by one on line 62.
#pygame.draw.rect(window, BLACK, brick)
#This draws each brick rectangle on the screen (window) using the BLACK color on line 63.

#Task: Create a variable BLACK to and assign (0,0,0) to it.

import pygame

# Initialize pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 800, 600
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
#Task : Create a variable BLACK to and assign (0,0,0) to it.

font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Brick Game')

paddle_width = 100
paddle_height = 20
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - paddle_height - 20
paddle_speed = 10

brick_rows = 5
brick_cols = 9
brick_width = 78
brick_height = 20
brick_padding = 10

bricks = []

for row in range(brick_rows):
    for col in range(brick_cols):
        brick_x = col * (brick_width + brick_padding) + brick_padding
        brick_y = row * (brick_height + brick_padding) + brick_padding
        bricks.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))

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

    # Draw all bricks using BLACK color
    for brick in bricks:
        pygame.draw.rect(window, BLACK, brick)

    pygame.display.update()

pygame.quit()
