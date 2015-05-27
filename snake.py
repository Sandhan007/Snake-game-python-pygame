# -*- coding: utf-8 -*-
"""
Created on Tue May 26 21:10:56 2015

@author: sandhan
"""

from box import Box
import random

class Snake:
    def __init__(self,x,y,boundary): 
        self.snake = []
        self.snake.append(Box(x,y,20)) #creates the head of the snake
        self.snake[0].animation = True #animates the head
        self.length = 3
        self.boundary = boundary
        self.direction = random.choice(['NORTH','SOUTH','EAST','WEST'])
        self.wall_hit = False
        self.self_hit = False
        self.count = 0
        self.delay = 0.003
        
        #initialy creates the snake with default 3 boxes
        for i in range(1,self.length):
            if (self.direction == 'NORTH'):
                self.snake.append(Box(x,y+i*20,20))
            elif (self.direction == 'SOUTH'):
                self.snake.append(Box(x,y - i*20,20))
            elif (self.direction == 'EAST'):
                self.snake.append(Box(x - i*20,y,20))
            elif (self.direction == 'WEST'):
                self.snake.append(Box(x + i*20,y,20))
    
    #this function just copies position of a box and sets it to the next box, from tail to head.
    #the head of the snake being considered at index 0
    def crawl(self):      
        for i in range(1,len(self.snake))[::-1]:
            self.snake[i].box.left = self.snake[i-1].box.left
            self.snake[i].box.top = self.snake[i-1].box.top
    
    #sets the direction for the snake   
    def set_direction(self,direction):
        if(direction == 'NORTH'):
            if(self.snake[0].box.top != self.snake[1].box.bottom):
                self.direction = direction
        elif(direction == 'SOUTH'):
            if(self.snake[0].box.bottom != self.snake[1].box.top):
                self.direction = direction
        elif(direction == 'EAST'):
            if(self.snake[0].box.right != self.snake[1].box.left):
                self.direction = direction
        elif(direction == 'WEST'):
            if(self.snake[0].box.left != self.snake[1].box.right):
                self.direction = direction
    
    #moves the snake in the set direction   
    def move(self):
        if(self.direction == 'NORTH'):
            self.crawl()
            self.snake[0].box.top-=self.snake[0].box.height
        elif(self.direction == 'SOUTH'):
            self.crawl()
            self.snake[0].box.top+=self.snake[0].box.height
        elif(self.direction == 'EAST'):
            self.crawl()
            self.snake[0].box.left+=self.snake[0].box.width
        elif(self.direction == 'WEST'):
            self.crawl()
            self.snake[0].box.left-=self.snake[0].box.width
     
    #The following function checks if the snake hits itself, 
    #and sets self_hit variable true or false accordingly            
    def check_self_hit(self):
        if (self.direction == 'NORTH'):
            for i in range(1,len(self.snake)):
                if(self.snake[0].box.centerx == self.snake[i].box.centerx and self.snake[0].box.centery - self.snake[0].box.height == self.snake[i].box.centery):
                    self.self_hit = True
                    return
        elif (self.direction == 'SOUTH'):
            for i in range(1,len(self.snake)):
                if(self.snake[0].box.centerx == self.snake[i].box.centerx and self.snake[0].box.centery + self.snake[0].box.height == self.snake[i].box.centery):
                    self.self_hit = True
                    return
        elif (self.direction == 'EAST'):
            for i in range(1,len(self.snake)):
                if(self.snake[0].box.centerx + self.snake[0].box.width == self.snake[i].box.centerx and self.snake[0].box.centery == self.snake[i].box.centery):
                    self.self_hit = True
                    return
        elif (self.direction == 'WEST'):
            for i in range(1,len(self.snake)):
                if(self.snake[0].box.centerx - self.snake[0].box.width == self.snake[i].box.centerx and self.snake[0].box.centery == self.snake[i].box.centery):
                    self.self_hit = True
                    return

    #The following function checks if the snake hits a wall, 
    #and sets wall_hit variable true or false accordingly                
    def check_wall_hit(self):
        if(self.direction == 'NORTH'):
            if(self.snake[0].box.top ==self.boundary.top):
                self.wall_hit = True
                return
        elif(self.direction == 'SOUTH'):
            if(self.snake[0].box.bottom ==self.boundary.bottom):
                self.wall_hit = True
                return
                
        elif(self.direction == 'EAST'):
            if(self.snake[0].box.right ==self.boundary.right):
                self.wall_hit = True
                return
                
        elif(self.direction == 'WEST'):
            if(self.snake[0].box.left == self.boundary.left):
                self.wall_hit = True
                return
                    
    def update(self):
        #update length information of the snake
        self.length = len(self.snake)
        
        #counts upto 5, if greater then 5 performs the following and resets to zero
        if (self.count>5):
            self.check_self_hit()#check if snake hits itself
            self.check_wall_hit()#check if snake hits wall
            
            #move the snake only if it has not hit itself or wall
            if(not self.wall_hit and not self.self_hit):
                self.move()
                
            else: #if the snake hits itself or wall update 
                  #death variable for each box in the snake list as true
                for i in range(len(self.snake)):
                    self.snake[i].death = True
            self.count=0
        else:#increments count if not greater than 5
            self.count+=self.delay
            
       
        
        #Loop to update all the Box objects in the snake list            
        for i in range(len(self.snake)):
            self.snake[i].update()
            
    def display(self,surface):
        for i in range(len(self.snake)):
            self.snake[i].display(surface)     
