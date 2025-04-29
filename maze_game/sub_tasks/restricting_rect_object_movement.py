#Task: We have added the conditions for restricting the rect object’s movement in the left and right directions.
#Add the conditions to restrict the rect object in the up and down directions.
#Hint: rect.y → returns the y coordinate of the top-left corner of the rect object.
#rect.height → returns the height of the rect object.
#Using the above two variables and window_height, you can restrict the movement.


import pygame
pygame.init()
window_width, window_height = 500, 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Restricting Rect Object Movement')
clock = pygame.time.Clock()
rect = pygame.Rect(0, 0, 50, 50)
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
        #here we are checking if the x value of the top-left coordinate
        #is less than 450.
        if keys[pygame.K_RIGHT] and rect.x < (window_width-rect.width):
            rect.x = rect.x + 1
        #here we are checking if the x value of the top-left coordinate
        #is greater than zero.
        if keys[pygame.K_LEFT] and rect.x > 0:
            rect.x = rect.x -1
    window.fill((255, 255, 255))
    pygame.draw.rect(window, (255, 0, 0), rect)
    pygame.display.update()
pygame.quit()


