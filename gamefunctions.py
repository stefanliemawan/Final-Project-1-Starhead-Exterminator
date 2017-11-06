#Import Every Class and Modules That Will be Used
import pygame
import sys
import pygame.font
from players import Enemy
from players import Hostage

#Enemy is the One You Have to Shoot in the Game
#Hostage is the One You Must NOT Shoot

#Display Before the Game Actually Starts
def firstscreen(screen,button,stats,gun,enemies,hostage,score):    
    screen.fill((0, 0, 1))  # Fill the Screen with Color
    for event in pygame.event.get():

        #Close the Window When the ESC Key is Pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:        
                sys.exit()

        #Start the Motion of the Game When the Play Button is Clicked...
        if event.type == pygame.MOUSEBUTTONDOWN:   
            if button.is_clicked() == True:         
                stats.game_active=True

            #Loop the Enemies Sprite Group
            for enemy in enemies:                   
                if enemy.is_clicked() == True:  #When the Sprite is Clicked...
                    starheadsfx()   #Play the Sound Effect
                    enemies.remove(enemy)   #Kill the Sprite
                    stats.score += stats.enemypoints    #Increase the Score
                    score.prep_score()  #Update the Score and Display the New One the Screen

            #Loop the Hostage Sprite Group
            for host in hostage:  # When the Sprite is Clicked...
                if host.is_clicked() == True:  
                    greenheadsfx()  # Play the Sound Effect  
                    hostage.remove(host)    #Kill the Sprite
                    stats.lives-=1  #Reduce the Lives Count by 1
                    score.prep_lives()    #Update and Display the New Lives Count
        
#Display When the Game is in Motion
def gametrue(screen,stats,gun,enemies,hostage,score):   
    screen.fill((224, 255, 255))  # Change the Screen Color
    create_players(screen,stats,enemies,hostage)    #Function to Create the Enemy

    #Check if the Enemy Has Hit the Bottom of the Screen
    for enemy in enemies:
        if enemy.check_bottom() == True:
            enemies.remove(enemy)  # Delete the Enemy
            stats.lives -= 1    #Reduce the Lives Count by 1
            score.prep_lives()    #Update the Lives Count Again
    #Check if the Hostage Has Hit the Bottom of the Screen
    for host in hostage:
        if host.check_bottom() == True:
            hostage.remove(host)    #Delete the Hostage

    #Now Update and Display The Objects to the Screen
    enemies.update()
    hostage.update()
    enemies.draw(screen)
    hostage.draw(screen)
    score.prep_score()
    score.prep_lives()
    score.showscore()
    gun.update()
    gun.blitme()

#When the Game is Not in Motion
def update_screen(screen,gun,enemies,hostage,button,stats):
    #Draw The Button Before the Game Starts
    if not stats.game_active:
        pygame.mouse.set_visible(True)  #Show the Cursor
        button.draw_button()    
    #Check Whether the Player Lost All of the Lives
    if stats.lives == 0:
        pygame.time.delay(500)  #Delay 500 miliseconds
        stats.reset(enemies, hostage)   #Reset The Game Stats
    pygame.display.flip()   #Update the Display

#Create the Enemies and Hostage
def create_players(screen,stats,enemies,hostage):
    time = pygame.time.get_ticks()  #Get the Time Since the Initialization of Pygame
    #Add Enemy and Hostage to Their Group After Some Time
    if time % 300 == 0:     
        enemies.add(Enemy(screen,stats))
    if time % 800 == 0:
        hostage.add(Hostage(screen,stats))

#Play the Sound Effects When Its Called
def starheadsfx():
    sound = pygame.mixer.Sound('starhead.wav')  #Load the Sound Effect File
    sound.play()
def greenheadsfx():
    sound = pygame.mixer.Sound('greenhead.wav') #Load the Sound Effect File
    sound.play()
