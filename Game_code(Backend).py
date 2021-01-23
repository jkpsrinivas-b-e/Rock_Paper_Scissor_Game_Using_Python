#Importing required modules and libraries
import tkinter as tk
from tkinter import font
from tkinter import *
from tkinter import ttk
import random
import time

#Game code
player_score = 0
computer_score = 0
options = [('rock',0), ('paper',1), ('scissors',2)]

#Function to select the option by user
def player_choice(player_input):
    global player_score, computer_score

    #Check if the score reached 10 already
    if computer_score == 10 or player_score == 10:
        time.sleep(0)
        exit(0)
    computer_input = get_computer_choice()
    player_choice_label.config(text = 'You Selected : ' + player_input[0])
    computer_choice_label.config(text = 'Computer Selected : ' + computer_input[0])
    if(player_input == computer_input):
        winner_label.config(text = "Tie")
    elif((player_input[1] - computer_input[1]) % 3 == 1):
        player_score += 1
        winner_label.config(text="You Won!!!")
        player_score_label.config(text = 'Your Score : ' + str(player_score))
    else:
        computer_score += 1
        winner_label.config(text="Computer Won!!!")
        computer_score_label.config(text='Computer Score : ' + str(computer_score))
#Function to Randomly Select Computer Choice
def get_computer_choice():
    return random.choice(options)
