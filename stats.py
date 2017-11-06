#Import Every Class and Modules That Will be Used

from pygame.sprite import Sprite
import pygame

class Stats():
    def __init__(self): #Initialize the class
        self.game_active = False    #Set the game_active at False so the Game Won't Start at First
        self.score = 0  #Set the Score at 0 
        self.enemypoints = 50   #Set Every Points For Killing Enemy
        self.lives = 3  #Set the Lives Count
        self.speed = 1  #Set the Enemy and Hostage Moving Speed
    
    def reset(self,enemies,hostage):    #Reset the Stats
        self.game_active = False
        self.lives = 3
        self.score = 0
        #Empty the Enemies and Hostage Group
        enemies.empty()
        hostage.empty()
        
