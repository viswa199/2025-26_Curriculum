#Task1: Try to draw a rectangle using the Rect object as above. The positioning of the rectangle 
# should be at the top-left corner of the window.
#Hint: The top-left corner of the rectangle should be the top-left corner of the window.

#Task2: Try to draw a rectangle using the Rect object as above. The top-right corner of the rectangle 
#should be the top-right corner of the window and the width of the rectangle should be 100.


import pygame
pygame.init()
width, height = 500, 500
window = pygame.display.set_mode((width, height))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #Here we are storing and managing rectangular coordinates in a Rect object.
    rect = pygame.Rect(0, 50, 100, 150)
    #Here we are drawing a rectangle with top left corner at (0, 50) and width 100, height 150
    pygame.draw.rect(window, (0, 255, 0), rect)
    pygame.display.update()


    