import grimoire
import pygame
from pygame.locals import *
from organisms import Food

# Initialise pygame window
pygame.init()
displaysurf = pygame.display.set_mode((1600, 900), pygame.FULLSCREEN)

status = "running"

# Colour settings
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gray = (100, 100, 100)
yellow = (255, 255, 0)
orange = (255, 128, 0)
purple = (255, 0, 255)
cyan = (0, 255, 255)


while True:
    
    # Refresh screen for pygame window
    displaysurf.fill(black)
    pygame.draw.rect(displaysurf, white, (0, 0, 1600, 900), 1)
    pygame.draw.line(displaysurf, white, (1400, 0), (1400, 900), 1)

    # Main section for displayed content
    



    # Update pygame window
    pygame.display.update()

    # Event loop
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.__dict__['key'] == 27:
                status = "quit_game"
        # Exit if window is closed
        if event.type == QUIT:
            status = "quit_game"

    # quit_game event
    if status == "quit_game":
        break