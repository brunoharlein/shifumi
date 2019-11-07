#!/usr/bin/python3.7
# coding: utf8


from functions import * #import function in functions file

# start import
import pygame #import pygame for play mp3 sound
import time #import time for timing
# end import

#start music with pygame and display text
pygame.init()
pygame.mixer.music.load("lord.mp3") #load sound
pygame.mixer.music.play() #play sound
time.sleep(2) #2 seconds before start game
print("Dans quelques secondes le programme commencera")
time.sleep(4)
print("Ceci est le meilleur jeu du monde")
time.sleep(3)
print("Il est temps de rejoindre Golum")
time.sleep(3)
#end music program

#score user1 and computer in dictionary
score = {
    "player": 0,
    "computer": 0
}

#start program
#ask name player
user1 = playerName()

#start choice program with loop
while score["player"] != 3 and score["computer"] != 3:
    playerChoice = user1Choice()
    # generate random choice computer
    computerChoice = computerChoices()
    # update the scores dictionnary
    scores = calculateScore(score, playerChoice, computerChoice)
    print("L'ordinateur a fait {} comme choix".format(computerChoice))
    print("{} score : {} | ordinateur score : {}".format(user1, score["player"], score["computer"]))


