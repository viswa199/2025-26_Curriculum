import pygame
pygame.init()
width, height = 500, 500
window = pygame.display.set_mode((width, height))
# The following line sets the title of the window to "Maze Game"
pygame.display.set_caption("Maze Game")
# The following line sets the background color of the window to white
window.fill((255, 255, 255)) #white
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.flip()


    