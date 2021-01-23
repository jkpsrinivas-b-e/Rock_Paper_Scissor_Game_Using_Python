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


#Preparing game window
game_window = tk.Tk()
game_window.title("Rock Paper Scissor")

#This will make the font size default wherever we apply(your options, score, you selected, computer selected)
app_font = font.Font(size = 12)

#Displaying Game title
game_title = Label (text = "Rock Paper Scissor", font = font.Font(size=20), fg = 'blue', pady = 5)
game_title.pack()

#Displaying winner label
winner_label = Label(text = "Let's begin the Game...", fg = 'green', font = font.Font(size = 15), pady = 10)
winner_label.pack()

#It is used to place the window we made in the rectuangular area(tkinter area)
input_frame = Frame(game_window)
input_frame.pack()

#Displaying player options
player_options = Label(input_frame, text = "Your Options : ", font = app_font, fg = 'grey')
player_options.grid(row = 0, column = 0, pady = 8)

#Setting up the buttons
#Rock buttom
rock = Button(input_frame, text = 'Rock', width = 15, bd = 2, bg = 'yellow', pady = 5, command = lambda: player_choice(options[0]))
rock.grid(row = 1, column = 1, padx = 7, pady = 5)

#Paper button
paper = Button(input_frame, text = 'Paper', width = 15, bd = 2, bg = 'lightblue', pady = 5, command = lambda: player_choice(options[1]))
paper.grid(row = 1, column = 2, padx = 7, pady = 5)

#Scissor button
scissors = Button(input_frame, text = 'Scissors', width = 15, bd = 2, bg = 'pink', pady = 5, command = lambda: player_choice(options[2]))
scissors.grid(row = 1, column = 3, padx = 7, pady = 5)

#Displaying score option
score_label = Label(input_frame, text = 'Score : ', font = app_font, fg = 'grey')
score_label.grid(row = 2, column = 0)

#Setting up the options to display various forms of score
player_choice_label = Label(input_frame, text = 'You Selected : - ', font = app_font)
player_choice_label.grid(row = 3, column = 1, pady = 5)

player_score_label = Label(input_frame, text = 'Your Score : - ', font = app_font)
player_score_label.grid(row = 3, column = 2, pady = 5)

computer_choice_label = Label(input_frame, text = 'Computer Selected : - ', font = app_font, fg = 'black')
computer_choice_label.grid(row = 4, column = 1, pady = 5)

computer_score_label = Label(input_frame, text = 'Computer Score : - ', font = app_font, fg = 'black')
computer_score_label.grid(row = 4, column = 2, padx = 10, pady = 5)

#Setting up the window size
game_window.geometry('720x320')
game_window.mainloop()

#END#
