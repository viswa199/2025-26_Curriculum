#Task: Add two more rectangles to the obstacles list and observe the output screen. 
# (Any of the rectangles should not touch each other).


import pygame 
pygame.init()
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Drawing two rectangle objects")
#Here, we are creating a list named obstacles that contains 
#two Rect objects.
obstacles = [
    pygame.Rect(0, 0, 100, 150),
    pygame.Rect(150, 50, 70, 90)
]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    #We are using a for loop on obstacles list to draw the rectangles.
    for obstacle in obstacles:
        pygame.draw.rect(window, (197, 65, 23), obstacle)
    pygame.display.update()


    
