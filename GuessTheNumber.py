'''
Created on Oct 3, 2014
Mini-project # 2: "Guess the number"  
Python MOOC @ Coursera
@author: nirav.chotai

Input will come from buttons and an input field
All output for the game will be printed in the console
'''
import simplegui
import random
import math

secret_number = 0
secret_number = random.randrange(0, 100)
counter = 7
i = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, counter    
    if counter == 7:
        print " "
        print "New game. Range is from 0 to 100"    
        print "Number of remaining guesses is", counter
    elif counter == 10:
        print " "
        print "New game. Range is from 0 to 1000"    
        print "Number of remaining guesses is", counter
    else:
        print " "
        print "New game. Range is from 0 to 100"            
        counter = 7 
        print "Number of remaining guesses is", counter
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number, counter
    secret_number = random.randrange(0, 100)
    counter = 7    
    new_game()
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number, counter
    secret_number = random.randrange(0, 1000)  
    counter = 10    
    new_game()  
    
def input_guess(guess):
    # main game logic goes here	
    guess = int(guess)
    print " "    
    global counter, i
    if counter == 10:
        i = 10 
    counter = counter - 1
    print "Guess was", guess           
    if secret_number == guess:            
        print "Correct!"           
        if i == 10:
            counter = 10
            new_game()
        else:
            counter = 7
            new_game()
    elif secret_number > guess:
        print "Number of remaining guesses is", counter
        if counter == 0:
            print "You ran out of guesses.  The number was",secret_number
            if i == 10:
                counter = 10
                new_game()
            else:
                counter = 7
                new_game()
        else:
            print "Higher!"            
    else:
        print "Number of remaining guesses is", counter
        if counter == 0:
            print "You ran out of guesses.  The number was",secret_number
            if i == 10:
                counter = 10
                new_game()
            else:
                counter = 7
                new_game()
        else:
            print "Lower!"            

# create frame
frame = simplegui.create_frame("Guess the Number",200,200)

# register event handlers for control elements and start frame
btn_range_1 = frame.add_button("Range is [0, 100)", range100, 200)
btn_range_2 = frame.add_button("Range is [0, 1000)", range1000, 200)
inp_guess = frame.add_input("Enter a Guess",input_guess,50)
frame.start()
# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
