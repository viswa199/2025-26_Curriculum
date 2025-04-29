#import pygame module
import pygame
#init function initializes all the pygame module that needs initialization.
#when you call this function, it sets up the necessary components for using Pygame
#features like graphics, sound, and input handling.
pygame.init()
window_width, window_height = 500, 500
#set_mode function returns a Surface object. This is the actual window you see.
window = pygame.display.set_mode((window_width, window_height))
window.fill((255, 255, 255))
#set_caption sets the title for the window.
pygame.display.set_caption('Maze')
#We run an infinite loop and wait for any events to happen.
#If the user presses the close button, we call pygame.quit().
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #setting running=False will exit out of the loop.
            running=False
    #we set the framerate to 60(60 frames per second.)
    #after every frame, we update the screen if any changes.
    pygame.display.update()
#once we exit out of the loop, we will call pygame.quit.
#This function closes the window.
pygame.quit()