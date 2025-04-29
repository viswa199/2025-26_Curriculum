#This is an end-to-end task, that you should complete.
#Task1: Create a pygame window, give it a title and make the window persist.
#Task2: Create a Rect object of your own on the bottom of the window.
#Task3: Using event handling, move the rect object using arrow keys.(You have learned pygame coordinate system.)
#Task4: Implement boundary restriction on that rect object such that It's position should not leave the window.
import pygame
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Brick Game')
paddle_x = 200
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= 5
    if keys[pygame.K_RIGHT] and paddle_x < 500 - 100:
        paddle_x += 5
    window.fill((0,0,0))
    pygame.draw.rect(window, (255, 0, 0), (paddle_x, 400, 100, 50))
    pygame.display.update()
pygame.quit()