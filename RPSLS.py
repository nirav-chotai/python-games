'''
Created on Sep 25, 2014
Mini-project # 1: Rock-paper-scissors-lizard-Spock  
Python MOOC @ Coursera
@author: nirav.chotai

The key idea of this program is to equate the strings
"rock", "paper", "scissors", "lizard", "Spock" to numbers
as follows:

0 - rock
1 - Spock
2 - paper
3 - lizard
4 - scissors
'''

import random

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "Wrong choice!"

def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "Wrong choice!"

def rpsls(player_choice):
    # print a blank line to separate consecutive games
    print " "
    
    # print out the message for the player's choice
    print "Player chooses", player_choice
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses", comp_choice
    
    # compute difference of comp_number and player_number modulo five
    score = (player_number - comp_number) % 5
    
    # use if/elif/else to determine winner, print winner message
    if score == 1 or score == 2:
        print "Player wins!"
    elif score == 3 or score == 4:
        print "Computer wins!"
    else:
        print "Player and computer tie!"
    
# testing    
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")