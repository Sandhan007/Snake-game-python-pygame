# -*- coding: utf-8 -*-
"""
Created on Tue May 26 19:36:44 2015

@author: sandhan
"""
import pygame
from colors import *

class Box:
    def __init__(self,x,y,size):
        self.box = pygame.Rect(x,y,size,size) #the x,y, and size parameters are formed into a pygame>rect object
        self.color = BLUE
        self.animation = False
        self.count = 0
        self.delay = 0.01
        self.death = False
        
    def update(self):#method to update the parameters of the object according to changes in the game    
        #if death is true the disable animation color the box red
        if(self.death):
            self.animation = False
            self.color = RED
        else:
            self.color = BLUE
            
    def display(self,surface):#method to display the object on the pygame screen
        surface.lock()
        if(self.animation): #check if animation is enabled
        
            #inflate the box size by 4 during the first 5 counts
            if (self.count<5):
                pygame.draw.rect(surface,self.color,self.box.inflate(4,4),1)
                self.count+=self.delay
            #display the box normally for next 5 counts
            elif(self.count>4 and self.count <10):
                pygame.draw.rect(surface,self.color,self.box,1)
                self.count+=self.delay
            #reset count to zero if count >= 10
            else:
                self.count=0
        #display normally  if animation disabled
        else:
            pygame.draw.rect(surface,self.color,self.box,1)
        surface.unlock()