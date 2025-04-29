#Task: Keep rect1 fixed and control the rect2 using event handling and then check the collision handling between them.

import pygame
pygame.init()
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Collision Handling")
clock = pygame.time.Clock()
#creating two rect objects at different positions.
rect1 = pygame.Rect(0, 0, 50, 50)
rect2 = pygame.Rect(100, 100, 50, 50)
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
        #We are controlling the rect1. rect2 is fixed.
        if keys[pygame.K_LEFT]:
            rect1.x = rect1.x - 5
        if keys[pygame.K_RIGHT]:
            rect1.x = rect1.x + 5
        if keys[pygame.K_UP]:
            rect1.y = rect1.y - 5
        if keys[pygame.K_DOWN]:
            rect1.y = rect1.y + 5
    window.fill((255, 255, 255))
    #drawing two rect objects on the window.
    pygame.draw.rect(window, (255, 0, 0), rect1)
    pygame.draw.rect(window, (0, 255, 0), rect2)
    #checking if the two rect objects are colliding.
    if rect1.colliderect(rect2):
        print("Collision Detected")
    pygame.display.update()
pygame.quit()






