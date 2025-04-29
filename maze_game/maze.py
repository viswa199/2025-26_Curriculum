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
  clock.tick(60)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  keys = pygame.key.get_pressed()
  if keys[pygame.K_RIGHT] and (player_x<window_width-player_width):
    player_x = player_x + player_speed
  if keys[pygame.K_LEFT] and player_x > 0:
    player_x = player_x - player_speed
  if keys[pygame.K_UP] and player_y > 0:
    player_y = player_y - player_speed
  if keys[pygame.K_DOWN] and (player_y<window_width-player_height):
    player_y = player_y + player_speed

  window.fill((255, 255, 255))

  player = pygame.draw.rect(window, green, (player_x, player_y, player_width, player_height))

  win = pygame.draw.rect(window, blue, (450, 0, 70, 70))

  #This is for checking the losing status.
  #We use for loop to check, if our player collides with any of the obstacles.
  for obstacle in obstacles:
    #colliderect method tell us, if we collided with another rect object.
    if player.colliderect(obstacle):
      #If player collided with obstacle, we end the game by rendering a text on the screen.
      #font.render method creates a Surface object(like a screen)
      game_over_text = font.render('Game Over', True, (255, 0, 0))
      #blit method places one surface object on the other.
      window.blit(game_over_text, (230, 250))
      pygame.display.update()
      pygame.time.delay(2000)  #adding delay
      running = False #we set the running to False, we will exit the for loop.

  #We are checking win condition here.
  #If player collides with win object, we win the game.
  if player.colliderect(win):
    #Here we are rendering win message and placing it on window surface object.
    you_win_text = font.render('You Win', True, (0, 255, 0))
    window.blit(you_win_text, (230, 250))

  for object in obstacles:
    pygame.draw.rect(window, brown, object)

  pygame.display.update()

pygame.quit()