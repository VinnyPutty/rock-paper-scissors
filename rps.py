__author__ = 'VinnyPutty'

import random

userChoice = raw_input("Rock, Paper, or Scissors? ")

compNum = random.random()

compChoice = ""

if compNum <= .33:
    compChoice = "Rock"
elif compNum <= .66:
    compChoice = "Paper"
else:
    compChoice = "Scissors"

print "Your choice: " + userChoice
print "Computer's choice: " + compChoice

if userChoice == "Rock" and compChoice == "Paper" or userChoice == "Paper" and compChoice == "Rock":
    print "Paper wins"
elif userChoice == "Paper" and compChoice == "Scissors" or userChoice == "Scissors" and compChoice == "Paper":
    print "Scissors wins"
elif userChoice == "Rock" and compChoice == "Scissors" or userChoice == "Scissors" and compChoice == "Rock":
    print "Rock wins"








