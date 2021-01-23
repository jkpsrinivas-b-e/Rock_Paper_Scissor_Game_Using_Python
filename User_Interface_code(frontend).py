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
