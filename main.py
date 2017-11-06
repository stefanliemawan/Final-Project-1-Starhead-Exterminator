#Import Every Class and Modules That Will be Used
import pygame
import sys
import gamefunctions as gf
from gun import Gun
from players import Enemy
from players import Hostage
from pygame.sprite import Group
from button import Button
from stats import Stats
from score import Score

def game():
    pygame.init()       #Initialize Pygame
    pygame.mixer.pre_init(44100, -16, 2, 2048)  # Reduce Lagging for the Music
    pygame.mixer.init()     #Initialize Mixer for Background Music
    pygame.mixer.music.load('bgm.wav')      #Load the BGM File
    pygame.mixer.music.play(-1)     #Play the BGM Infinitely
    screen=pygame.display.set_mode((500,650))       #Set the Pygame Window
    pygame.display.set_caption("STARHEAD EXTERMINATOR")     #Set the Window Caption

    #Call All the Classes
    txt = "DONT SHOOT THE GREEN ONE"
    button = Button(screen,txt)
    stats = Stats()
    gun = Gun(screen)
    enemy = Enemy(screen,stats)
    host = Hostage(screen,stats)
    score = Score(screen, stats)
    enemies = Group()
    hostage = Group()
    #Start the Game Loop
    while True:
        gf.firstscreen(screen,button,stats,gun,enemies,hostage,score)      #First Display of the Game 
        if stats.game_active:       #Start when the Player Click the Button
            gf.gametrue(screen,stats,gun,enemies,hostage,score)     #Update and Behaviour of Objects in the Game
        gf.update_screen(screen,gun,enemies,hostage,button,stats)       #Update the Screen and Flip


game()      #Call the Game
