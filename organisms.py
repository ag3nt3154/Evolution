import pygame
import random
import time
import numpy as np


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

# Seed random
random.seed(time.time())


class Food:
    
    def __init__(self, displaysurf):
        self.size = 3
        self.pos = np.ndarray(random.randint(0, 1600 - self.size), random.randint(0, 900 - self.size))
        self.displaysurf = displaysurf
        
        
    def show(self):
        pygame.draw.rect(self.displaysurf, white, (self.pos[0], self.pos[1], self.size, self.size))
        
    