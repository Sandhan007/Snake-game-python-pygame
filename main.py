#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 19:19:25 2015

@author: sandhan
"""

import pygame
from colors import *
from pygame.locals import *
from game import Game

pygame.init()

(width,height) = (400,400)

DISPLAY = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake")

myGame = Game(DISPLAY,pygame.Rect(0,0,400,400))

RUNNING = True
while(RUNNING):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
            
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                myGame.mySnake.set_direction('WEST')
                
            elif event.key == K_RIGHT:
                myGame.mySnake.set_direction('EAST')
                
            elif event.key == K_UP:
                myGame.mySnake.set_direction('NORTH')       
                
            elif event.key == K_DOWN:
                myGame.mySnake.set_direction('SOUTH')
            
            elif event.key == K_ESCAPE:
                pygame.display.set_caption("Game Restart")
            
    DISPLAY.fill(WHITE)
    myGame.update()
    myGame.display()
    pygame.display.update()

exit()