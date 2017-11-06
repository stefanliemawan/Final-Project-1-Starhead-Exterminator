#Import Every Class and Modules That Will be Used
import pygame
import sys

class Gun():
    def __init__(self,screen):      #Initialize the Class
        self.screen=screen
        self.image=pygame.image.load('crosshair.png')   #Load the Gun Image
        self.rect=self.image.get_rect()     #Get the Rectangle of the Gun Image
    
    #Function to Draw the Gun to the Screen
    def blitme(self):
        self.screen.blit(self.image,self.rect)

    #Update the Gun so It Follows the Cursor
    def update(self):
        pygame.mouse.set_visible(False)     #Hide the Cursor
        pygame.event.set_grab(True)     #Lock all Input into the Game
        mousex,mousey = pygame.mouse.get_pos()  #Get the Coordinates of the Mouse
        coorx,coory=mousex-23,mousey-23
        self.rect = coorx,coory     #Place the Rectangle at the Mouse Coordinates
        
                
        
