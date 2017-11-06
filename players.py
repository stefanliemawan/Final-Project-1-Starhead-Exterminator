#Import Every Class and Modules That Will be Used
import pygame
import sys
import random
from pygame.sprite import Sprite

class Enemy(Sprite):

    def __init__(self,screen,stats):    #Initialize the Class
        super(Enemy,self).__init__()    #Initialize the Sprite Class
        self.stats = stats
        self.screen = screen
        self.image = pygame.image.load("starhead.png")      #Load the Enemy Image
        self.rect = self.image.get_rect()       #Get the Rectangle of the Enemy Image
        
        #Place the Enemy at Random Spot at the Top of the Screen
        self.rect.x = random.randrange(30,470)
        self.rect.y = 0

    #Function to Draw the Enemy to the Screen
    def blitme(self):
        self.screen.blit(self.image,self.rect)

    #Check Whether the Enemy is Clicked
    def is_clicked(self):
        mousex, mousey = pygame.mouse.get_pos()     # Get the Coordinates of the Mouse
        # Check if the Rectangle Collide with the Mouse
        if self.rect.collidepoint(mousex, mousey):
            return True
        else:
            return False
    
    #Update the Enemy Coordinates to Move it
    def update(self):
        self.rect.y += self.stats.speed

    #Check Whether the Enemy Has Hit the Bottom of the Screen
    def check_bottom(self):
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True

        

class Hostage(Sprite):

    def __init__(self,screen,stats):    #Initialize the Class
        super(Hostage,self).__init__()  #Initialize the Sprite Class
        self.stats = stats
        self.screen=screen
        self.image=pygame.image.load('greenhead.png')   #Load the Hostage Image
        self.rect=self.image.get_rect()     #Get the Rectangle of the Hostage Image

        #Place the Hostage at Random Spot at the Top of the Screen
        self.rect.centerx=random.randrange(30,470)
        self.rect.centery=0

    #Function to Draw the Hostage to the Screen
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    #Check Whether the Hostage is Clicked
    def is_clicked(self):
        mousex, mousey = pygame.mouse.get_pos()     # Get the Coordinates of the Mouse
        if self.rect.collidepoint(mousex, mousey):  #Check if the Rectangle Collide with the Mouse
            return True
        else:
            return False
    
    #Update the Hostage Coordinates to Move it
    def update(self):
        self.rect.y += self.stats.speed
    
    #Check Whether the Hostage Has Hit the Bottom of the Screen
    def check_bottom(self):
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True


            
