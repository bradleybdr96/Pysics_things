# IMPORT
import numpy as np
from random import randint
import pygame as pygame
import sys

import wall.py
imoport collison.py


# VARIABLES



# CONSTANTS
sun_radius = 30

Black = (0, 0, 0) #BLACK
Yellow = (255, 255, 0)
Skyblue = (0, 192, 255)
GREEN = (0, 255, 0)




# FUNCTIONS

def draw_enviorment
    draw walls
    pygame.draw.circle(screen, GRAY, (400, 300), 100)


# MAIN GAME

# Initalize and set up pygame and pygame window
pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
screen.fill(GREEN)

whhile game is not over:


    Start the game:

    On player turn:
        Stage 1:

        CLick on the grey circle 
            if click anywhere else, do nothing
        spawn a ball on the click

        Stage 2:

        draw a line from ball to mouse
        when play clicks:
            start charging the hit
            the longer the click is held the faster the ball goes (up to 1000 px/s)
            when button is relesesed, move the ball based in speed, moving in the direction of the mouse was when relesed
            when all balls stop moving, repeat

    When all balls stop moving, decided which player will go based on didtance from the scroring zone

    Once all balls have been thrown, calulate score based on the scoring zone and display the winner