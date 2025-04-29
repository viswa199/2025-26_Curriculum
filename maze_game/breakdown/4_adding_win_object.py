import pygame

green = (0, 255, 0)
brown = (110, 38, 14)
blue = (0, 0, 255)

pygame.init()
window_width, window_height = 500, 500
window = pygame.display.set_mode((window_width, window_height))
window.fill((255, 255, 255))
pygame.display.set_caption('Maze')


obstacles = [
    pygame.Rect(0, 0, 400, 50),
    pygame.Rect(60, 90, 50, 200),
    pygame.Rect(200, 150, 400, 50),
    pygame.Rect(60, 280, 150, 50),
    pygame.Rect(180, 350, 200, 50),
    pygame.Rect(450, 420, 30, 200)
]

#We need a player to find the maze. Here we are setting the
#initial position of the player i.e; (0, 450)
player_x, player_y = 0, 450
player_speed = 1

#Here we are initializing pygame.font module.
#This line is unnecessary as pygame.init() already initialized this module.
pygame.font.init()
#We created a custom font of size 36.
font = pygame.font.Font(None, 36)

running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  window.fill((255, 255, 255))
  
  #Here, we are drawing player to the screen.
  player = pygame.draw.rect(window, green, (player_x, player_y, 50, 50))

  #we need a maze for player to find, so we are drawing maze to the screen
  #at (450, 0).
  win = pygame.draw.rect(window, blue, (450, 0, 70, 70))


  for object in obstacles:
    pygame.draw.rect(window, brown, object)

  pygame.display.update()

pygame.quit()