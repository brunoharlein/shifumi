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
time.sleep(2)
print("Une mort certaine. Une faible chance de succès…")
time.sleep(2)
print("Un Anneau pour les gouverner tous.")
time.sleep(2)
print("Un Anneau pour les trouver.")
time.sleep(2)
print("Un Anneau pour les amener tous et dans les ténèbres les lier.")
time.sleep(1)
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

#display message winner or looser

if score["player"] > score["computer"]:
    pygame.mixer.music.load("final.mp3")  # load sound
    print("Bravo l'anneau est dans les flammes du Mordor !!")
    pygame.mixer.music.play()  # play sound
    time.sleep(10)
else:
    pygame.mixer.music.load("street.mp3")  # load sound
    pygame.mixer.music.play()  # play sound
    print("Sauron vient de mettre l'anneau magique c'est la fin !!")
    time.sleep(10)

#end program




