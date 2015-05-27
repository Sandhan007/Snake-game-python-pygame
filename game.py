# -*- coding: utf-8 -*-
"""
Created on Tue May 26 22:35:28 2015

@author: sandhan
"""

import random
from box import Box
from snake import Snake

class Game:
    def __init__(self,surface,boundary):
        self.boundary = boundary
        self.bait_present = False
        self.bait = Box(0,0,0)
        self.score=0
        self.state ="PLAYING"
        self.surface = surface
        self.x=random.choice([80,100,120,140,160,180,200,220,240,260,280,300,320])
        self.y=random.choice([80,100,120,140,160,180,200,220,240,260,280,300,320])
        self.mySnake = Snake(self.x,self.y,self.boundary)
        
    def get_random_pos(self):
        position_space = [0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380]
        x_choices = position_space[:]
        y_choices = position_space[:]
        
        for i in range(len(self.mySnake.snake)):
            try:
                x_choices.remove(self.mySnake.snake[i].box.left)
            except ValueError:
                pass
      
        for i in range(len(self.mySnake.snake)):
            try:
                y_choices.remove(self.mySnake.snake[i].box.top)
            except ValueError:
                pass
            
        x = random.choice(x_choices)
        y = random.choice(y_choices)
        
        return (x,y)
    
    def give_bait(self):
        if (not self.bait_present):
            pos = self.get_random_pos()
            self.bait = Box(pos[0],pos[1],20)
            self.bait.animation = True
            print("Score : {}".format(self.score))
            self.bait_present = True
            
    def caught_bait(self):   
        if(self.mySnake.direction == 'WEST'):
            if (self.mySnake.snake[0].box.left == self.bait.box.right and self.mySnake.snake[0].box.top == self.bait.box.top):
                self.score+=5
                self.mySnake.delay+=0.0005
                self.mySnake.snake[0].animation = False
                self.mySnake.snake.insert(0,self.bait)
                self.bait_present = False
        elif(self.mySnake.direction == 'EAST'):
            if (self.mySnake.snake[0].box.right == self.bait.box.left and self.mySnake.snake[0].box.top == self.bait.box.top):
                self.score+=5
                self.mySnake.delay+=0.0005
                self.mySnake.snake[0].animation = False
                self.mySnake.snake.insert(0,self.bait)
                self.bait_present = False
        elif(self.mySnake.direction == 'NORTH'):
            if(self.mySnake.snake[0].box.left == self.bait.box.left and self.mySnake.snake[0].box.top == self.bait.box.bottom):
                self.score+=5
                self.mySnake.delay+=0.0005
                self.mySnake.snake[0].animation = False
                self.mySnake.snake.insert(0,self.bait)
                self.bait_present = False
        elif(self.mySnake.direction == 'SOUTH'):
            if(self.mySnake.snake[0].box.left == self.bait.box.left and self.mySnake.snake[0].box.bottom == self.bait.box.top):
                self.score+=5
                self.mySnake.delay+=0.0005
                self.mySnake.snake[0].animation = False
                self.mySnake.snake.insert(0,self.bait)
                self.bait_present = False
                
    def update(self):
        self.give_bait()
        self.caught_bait()
        self.mySnake.update()
        if (self.mySnake.wall_hit or self.mySnake.self_hit):
            if(not self.state == "GAME OVER"):
                print("Game Over!")
            self.state = "GAME OVER"
            
    def display(self):
        self.mySnake.display(self.surface)   
        self.bait.display(self.surface)
