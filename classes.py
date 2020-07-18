import pygame
from random import choice

class turtle():
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.firstX = x
        self.firstY= y
        self.image = pygame.image.load(image)
        self.vel_list = [1,1,10,1,1,1,0.5,0.5,0.5,0.5,20]
        self.vel = choice(self.vel_list)
        

    def drawturtle(self, win):
        win.blit(self.image, (self.x, self.y))

    def moveturtle(self):
        self.vel = choice(self.vel_list)
        self.x -= self.vel
    
    def reset(self):
        self.x = self.firstX
        self.y = self.firstY

class line():
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)

    def drawline(self, win):
        win.blit(self.image, (self.x, self.y))
        
class textOnScreen():
    def __init__(self, text, font, x, y, size, color):
        self.text = text
        self.size = size
        self.font = pygame.font.SysFont("Arial", self.size)
        self.x = x
        self.y = y
        self.color = color
        
        
    
    def showText(self, win):
        textReady = self.font.render(self.text, True, self.color)
        win.blit(textReady, (self.x,self.y))
