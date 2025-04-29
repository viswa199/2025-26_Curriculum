import pygame

green = (0, 255, 0)
brown = (110, 38, 14)
blue = (0, 0, 255)

pygame.init()
window_width, window_height = 500, 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Maze')

clock = pygame.time.Clock()

obstacles = [
    pygame.Rect(0, 0, 400, 50),
    pygame.Rect(60, 90, 50, 200),
    pygame.Rect(200, 150, 400, 50),
    pygame.Rect(60, 280, 150, 50),
    pygame.Rect(180, 350, 200, 50),
    pygame.Rect(450, 420, 30, 200)
]

player_x, player_y = 0, 450
player_width, player_height = 50, 50
player_speed = 1

pygame.font.init()
font = pygame.font.Font(None, 36)

running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  #We add the logic to move the player 
  #if we press any of the four keys(up, down, right, left).

  #This function returns the keys pressed by the user.
  keys = pygame.key.get_pressed()

  #If you press the right arrow, we will move the player right by 1 pixel.
  if keys[pygame.K_RIGHT] and player_x < (window_width-player_width):
    player_x = player_x + player_speed
  #If you press the left arrow, we will move the player left by 1 pixel.
  if keys[pygame.K_LEFT] and player_x > 0:
    player_x = player_x - player_speed
  #If you press the up arrow, we will move the player up by 1 pixel.
  if keys[pygame.K_UP] and player_y > 0:
    player_y = player_y - player_speed
  #If you press the down arrow, we will move the player down by 1 pixel.
  if keys[pygame.K_DOWN] and player_y < (window_height-player_height):
    player_y = player_y + player_speed

  window.fill((255, 255, 255))

  player = pygame.draw.rect(window, green, (player_x, player_y, player_width, player_height))

  win = pygame.draw.rect(window, blue, (450, 0, 70, 70))


  for object in obstacles:
    pygame.draw.rect(window, brown, object)
  
  clock.tick(60)
  pygame.display.update()

pygame.quit()