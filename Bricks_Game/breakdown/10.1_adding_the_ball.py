# pygame.draw.ellipse() → This function draws an oval or circle shape on line 72.
# window → The game screen where we draw the ball.
# RED → The color of the ball.
# [ball_x, ball_y, ball_size, ball_size] → This is the position and size:
# ball_x and ball_y are the coordinates of the ball (where it appears).
# ball_size is both the width and height, so the ball looks like a circle.

# Task : Pass the parameter to draw the ball on the screen on line 72.

import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)  # RGB value for red

font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Brick Game')

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

ball_size = 20
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 5
ball_speed_y = 5

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

    # Task : Pass the parameter to draw ball using ellipse.
    #pygame.draw.ellipse()


    for brick in bricks:
        pygame.draw.rect(window, BLACK, brick)

    pygame.display.update()

pygame.quit()
