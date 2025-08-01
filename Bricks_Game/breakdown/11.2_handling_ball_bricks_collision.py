# change the y direction of the ball.(ball_speed_y = -ball_speed_y) on line 100.
# There are two things that you have to do when a ball collides with brick.
# 1. remove that particular brick from the bricks list.(line no 99)
# 2. change the y-direction of the ball. (line no 100)

#Task: You can find the tasks on line 98.

import pygame

# Initialize pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 800, 600
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Font setup
font = pygame.font.Font(None, 36)

# Create game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Brick Game')

# Set up game clock
clock = pygame.time.Clock()
FPS = 30  # Frames per second

# Paddle properties
paddle_width = 100
paddle_height = 20
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - paddle_height - 20
paddle_speed = 10

# Ball properties
ball_size = 20
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 5
ball_speed_y = 5

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

bricks = []

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
    
    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    
    # Ball collision with walls
    if ball_x < 0 or ball_x > WIDTH - ball_size:
        ball_speed_x = -ball_speed_x
    if ball_y < 0:
        ball_speed_y = -ball_speed_y
    
    # Ball collision with paddle
    if pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height).colliderect(
        pygame.Rect(ball_x, ball_y, ball_size, ball_size)):
        ball_speed_y = -ball_speed_y
    
    # Ball collision with bricks
    #Task(remove the pass line and write your logic)
    for brick in bricks:
        if brick.colliderect(pygame.Rect(ball_x, ball_y, ball_size, ball_size)):
            #Task: Uncomment lines 100 and 101 to observe the changes.
            # bricks.remove(brick)
            # ball_speed_y = -ball_speed_y
    
    # Check for game over
    if ball_y > HEIGHT:
        you_lost_text = font.render('You Lost', True, BLACK)
        window.blit(you_lost_text, (340, 300))
        pygame.display.update()
        pygame.time.delay(3000)
        running = False
    
    
    window.fill(WHITE)
    
    # Draw paddle
    pygame.draw.rect(window, BLUE, [paddle_x, paddle_y, paddle_width, paddle_height])
    
    # Draw ball
    pygame.draw.ellipse(window, RED, [ball_x, ball_y, ball_size, ball_size])
    
    # Draw bricks
    for brick in bricks:
        pygame.draw.rect(window, BLACK, brick)
    
    # Update display
    pygame.display.update()

# Quit pygame
pygame.quit()
