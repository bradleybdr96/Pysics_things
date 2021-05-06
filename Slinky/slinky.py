# IMPORT
import numpy as np
from random import randint
import pygame as pygame
import sys

import SingleForce.py
import PairForce.py 
import BondForce.py 



# VARIABLES



# CONSTANTS
sun_radius = 30

Black = (0, 0, 0) #BLACK
Yellow = (255, 255, 0)
Skyblue = (0, 192, 255)




# FUNCTIONS

def draw_speheres():
    pygame.draw.circle(screen, DARK_GERY, (400, 50), 30)
    pygame.draw.circle(screen, RED, (400, 150), 30)
    pygame.draw.cricle(screen, ORANGE, (400, 250), 30)
    pygame.draw.circle(screen, YELLOW, (400, 350), 30)
    pygame.draw.cricle(screen, BLUE, (400, 450), 30)



# MAIN GAME

# Initalize and set up pygame and pygame window
pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
screen.fill(Skyblue)

whhile game is not over:
    Draw the spheres


    Start the game:
        When player lefts click:
            if on a circle:
                drag the circle to follow the mouse

                calualte the forces based on the movement of the circles
    
