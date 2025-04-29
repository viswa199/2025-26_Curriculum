import pygame

green = (0, 255, 0)
brown = (110, 38, 14)
blue = (0, 0, 255)

pygame.init()
window_width, window_height = 500, 500
window = pygame.display.set_mode((window_width, window_height))
window.fill((255, 255, 255))
pygame.display.set_caption('Maze')


#The whole point of the maze game is to finish the game by escaping obstacles.
#We are creating obstacles using Rect objects.

#pygame.Rect stores and manages the coordinates of the rectangle.
#pygame.Rect(0, 0, 30, 50) --> Here (0, 0) is the top left of the rectangle. 30 is the width and 50 is the height.
obstacles = [
    pygame.Rect(0, 0, 400, 50),
    pygame.Rect(60, 90, 50, 200),
    pygame.Rect(200, 150, 400, 50),
    pygame.Rect(60, 280, 150, 50),
    pygame.Rect(180, 350, 200, 50),
    pygame.Rect(450, 420, 30, 200)
]

running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  window.fill((255, 255, 255))

  #Here we are drawing the obstacle rectangles on the window screen.
  #pygame.draw.rect(Surface, color, RectValue) -> the first argument is screen, the second argument is color, 
  # the third argument is coordinates i.e; Rect object.
  for object in obstacles:
    pygame.draw.rect(window, brown, object)

  pygame.display.update()

pygame.quit()