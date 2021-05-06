# IMPORT
import numpy as np
from random import randint
import pygame as pygame
import sys



# VARIABLES



# CONSTANTS
sun_radius = 30

Black = (0, 0, 0) #BLACK
Yellow = (255, 255, 0)
Skyblue = (0, 192, 255)




# FUNCTIONS

def drawStage():
    pygame.draw.circle(screen, Yellow, (300, 300), sun_radius)
    draw circle pick ups

def DearPlayer(pos_x, pos_y):
    pygame.draw.circle(screen, Skyblue, (pos_x, pos_y), 10)
    
def calucalte_Grav_Force():
    calulate for grav force:
        top = (M * m)
        bottom = (math.pow(abs(r), 2) )
        total = G * (top / bottom) * r

# MAIN GAME

# Initalize and set up pygame and pygame window
pygame.init()
size = (600, 600)
screen = pygame.display.set_mode(size)

whhile game is not over:
    Draw the game Enviorment
    intilize the game timer
    Draw the player 


    Start the game:
        stat pick_up movement

    When player hits W:
        apply thrust to move ship foward
    When player hits A:
        apply thrust to move ship left
    When player hits D: 
        apply thrust to move ship right
    When player hits S: 
        apply thrust to move ship backward

    If player hits sun:
        Game Over 
        Display messgage for Game over 
    If player hits pickip:
        destroy pickup
        if last pickup is destroyed (pickup list length = 0)
            game over - player Wins 
            display winner messge
    
    Display messege for player to play again:
        if player hits 'space' -> play again
        if player hits 'esc' -> end game
    
