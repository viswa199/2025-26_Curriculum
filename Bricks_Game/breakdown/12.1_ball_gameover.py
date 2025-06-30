# If you can remember, we implemented the ball collision with walls
#(but we left out ball collision with bottom wall) 
# because, We are using paddle to control the ball movement.
# If the ball misses the paddle, It will reach out of the window and the player loses.
# If the ball_y is greater than window height (ball_y > HEIGHT), the ball missed the player on line 96

#Task: You need to check, if the ball moves down the window screen i.e. ball missed the paddle on line 96.

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

# Set up game clock
clock = pygame.time.Clock()

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

# Ball properties
ball_size = 20
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 5
ball_speed_y = 5

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
    
    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    
    # Ball collision with walls
    if ball_x < 0 or ball_x > WIDTH - ball_size:
        ball_speed_x = -ball_speed_x
    if ball_y < 0:
        ball_speed_y = -ball_speed_y
    
    # Ball collision with paddle
    if pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height).colliderect(pygame.Rect(ball_x, ball_y, ball_size, ball_size)):
        ball_speed_y = -ball_speed_y
    
    # Check for game over
    #Task
    #remove True and add your condition by reading the instructions above carefully.
    if True:
        you_lost_text = font.render('You Lost', True, BLACK)
        window.blit(you_lost_text, (340, 300))
        pygame.display.update()
        pygame.time.delay(3000)
        running = False
    
    # Fill screen with white
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
