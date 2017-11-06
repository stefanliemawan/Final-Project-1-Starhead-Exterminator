#inspired from Python Crash Course by Eric Matthes Chapter 14

#Import Every Class and Modules That Will be Used
import pygame.font
from players import Hostage
from pygame.sprite import Group

class Score():
    def __init__(self,screen,stats):    #Initialize the Class
        self.screen = screen
        self.screen_rect = screen.get_rect()    #Get the rectangle of the Screen
        self.stats = stats
        self.text_color = (30,30,30)    #Set the Text Color
        self.font = pygame.font.SysFont('freesansbold', 30)  # Set the Font Type

        self.prep_score()
        self.prep_lives()

    def prep_score(self):   #Function to Set the Score
        score_str = str(self.stats.score)   #Convert into STR
        self.score_image = self.font.render(score_str,True,     #Render the Text
            self.text_color)
        self.score_rect = self.score_image.get_rect()   #Get the Rectangle of the Score Image

        #Place the Score Rectangle at the Top Right of the Screen
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def prep_lives(self):   #Function to Set the Lives Count
        self.lives = Group()    #Place the Lives Inside a Group

        #Place the Lives Image at the Top Left of the Corner
        for lives_num in range (self.stats.lives):
            lives = Hostage(self.screen,self.stats)
            lives.rect.x = 10 + lives_num * lives.rect.width
            lives.rect.y = 10
            self.lives.add(lives)

    #Function to Draw the Score and Lives to the Screen
    def showscore(self):    
        self.screen.blit(self.score_image,self.score_rect)
        self.lives.draw(self.screen)
