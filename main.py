import random

game_grid = []
player_choice_history = []
computer_choice_history = []

def ComputerChoose():
    global game_grid
    choice = -1
    while True:
        random_choice = random.randint(0, 9) # choosing a random number from the valid cells in the grid
        if(game_grid[random_choice] != "X" or game_grid[random_choice] != "O"): # checking if the random choice collides with a previous choice
            choice = random_choice # if it doesnt, choose this cell and break out of the loop. else repeat until it doesn't collide
            break

def GenGameGrid():
    global player_choice_history
    global computer_choice_history

    to_return = ""
    for j in range(9):
        if(j in player_choice_history):
            i = "X"
        elif(j in computer_choice_history):
            i = "O"
        else:
            i = j + 1
        
        if((j+1)%3 == 0):
            to_return += f"{i}\n"
        else:
            to_return += f"{i} | "
    
    return to_return

print(GenGameGrid())
