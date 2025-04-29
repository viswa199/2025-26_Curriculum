#Task: Change the first two numbers in the rect argument in the function pygame.draw.rect and observe the relative change in output.
import pygame

pygame.init()
width, height = 500, 500
window = pygame.display.set_mode((width, height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #Here we are drawing a rectangle with top left corner at (50, 50) and width 100, height 100
    pygame.draw.rect(surface=window, color=(0, 255, 0), rect=(100, 100, 100, 100))
    pygame.display.update()

    