#Inspired from Python Crash Course by Eric Matthes Chapter 14

#Import Every Class and Modules That Will be Used
import pygame.font
from stats import Stats

class Button():
    def __init__(self,screen,msg):  #Initialize the Class
        self.screen = screen

        #Set the Font Type, Button and Text Color
        self.buttoncolor = (100,50,200)
        self.textcolor = (255,255,255)
        self.font=pygame.font.SysFont('freesansbold', 35)
        
        # Draw the Rectangle of the Button
        self.rect = pygame.Rect(0, 0, 600, 200)
        self.rect.center = screen.get_rect().center     #Place the Button Rectangle at the Center of the Screen

        self.msg_image = self.font.render(msg,True,self.textcolor,  #Render the Text
            self.buttoncolor)
        self.msg_image_rect = self.msg_image.get_rect()   #Get the Rectangle of the Text
        self.msg_image_rect.center = self.rect.center     #Place the Text Rectangle at the Center of the Button Rectangle

    #Function to Draw the Button to the Screen
    def draw_button(self):  
        self.screen.fill(self.buttoncolor,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)

    #Check Whether the Button is Clicked
    def is_clicked(self):   
        mouse_x, mouse_y = pygame.mouse.get_pos()  # Get the Coordinates of the Mouse
        if self.rect.collidepoint(mouse_x, mouse_y):    #Check if the Rectangle Collide with the Mouse
            return True
        else:
            return False

