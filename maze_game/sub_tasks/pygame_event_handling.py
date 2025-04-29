#Task: Modify the code, so that If the user presses space button, The program should quit
#Hint: pygame.K_SPACE is the space button.

import pygame
pygame.init()
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Event Handling")
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)
    #pygame.event.get() returns a list of all the events 
    # that have occurred since the last time it was called.
    for event in pygame.event.get():
        #Here, we are checking if the event is of type QUIT.
        #If the user presses the close button on the window,
        #the event is of type QUIT and we set running to False
        if event.type == pygame.QUIT:
            running = False
        #Here, we are checking if the event is of type KEYDOWN.
        #If the user presses any key on the keyboard,
        #the event is of type KEYDOWN and we print the key that was pressed.
        if event.type == pygame.KEYDOWN:
            print("Key pressed:", event.key) #prints the key that was pressed.
    pygame.display.update()
pygame.quit()