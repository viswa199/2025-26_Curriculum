#Task: Change the code, Add event handling for UP and DOWN arrow keys. If the user presses the UP arrow, decrement the y-coordinate by 1. 
# If the user presses the DOWN arrow, increment the y-coordinate by 1.

#Hint: rect.y = rect.y + 1 and rect.y = rect.y - 1


import pygame
pygame.init()
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Moving Rect Object")
clock = pygame.time.Clock()
#creating a rect object
rect = pygame.Rect(0, 0, 50, 50)
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Here, we get the keys that are pressed on the keyboard.
        keys = pygame.key.get_pressed()
        #If the left arrow key is pressed, we move the rect to the left.
        if keys[pygame.K_LEFT]:
            #rect.x returns the x-coordinate of the rect object.
            #we change the x-coordinate of the rect by -1
            rect.x = rect.x - 1
        #If the right arrow key is pressed, we move the rect to the right.
        if keys[pygame.K_RIGHT]:
            #we change the x-coordinate of the rect by 1
            rect.x = rect.x + 1
    window.fill((255, 255, 255))
    pygame.draw.rect(window, (255, 0, 0), rect)
    pygame.display.update()
pygame.quit()

