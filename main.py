import os
import random

game_grid = []
player_choice_history = []
computer_choice_history = []

def CheckTargetStatus(_target):
    for i in range(3):
        if(i%3 == 0): #if the cell is to the absolute left:
            if(i in _target and i + 1 in _target and i + 2 in _target): # check if 3 consecutive cells are selected. eg: (123, 456, 789)
                return True
        
        if(i < 3): #if the value is below 3. Reason being, to check if any vertically consecutive cells are selected from top to bottom.
            if(i in _target and i + 3 in _target and i + 6 in _target): # eg: (147, 258, 369)
                return True
    
    if(0 in _target and 4 in _target and 8 in _target): #checking diagonal top left to bottom right
        return True
    if(2 in _target and 4 in _target and 6 in _target): #checking diagonal top right to bottom left
        return True
    return False #if none of the above returned true, then no winning scenarios where achieved.

def ComputerChoose():
    global player_choice_history
    global computer_choice_history
    choice = -1
    while True:
        random_choice = random.randint(0, 8) # choosing a random number from the valid cells in the grid
        if(random_choice not in player_choice_history and random_choice not in computer_choice_history): # checking if the random choice collides with a previous choice
            choice = random_choice # if it doesnt, choose this cell and break out of the loop. else repeat until it doesn't collide
            break
    return choice

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

while(True):
    print(GenGameGrid())
    user_input = input("Choose a number from the grid to make a move; or q to quit game: ")
    if(user_input == "q"):
        print("Thanks for playing the game.")
        break
    if(user_input.isdigit):
        user_input = int(user_input)
    
    player_choice_history.append(user_input - 1)
    if(CheckTargetStatus(player_choice_history)):
        print("You won. Good job.")
        break

    computer_choice_history.append(ComputerChoose())
    if(CheckTargetStatus(computer_choice_history)):
        print("Computer won. Better luck next time.")
        break

    if(len(computer_choice_history) + len(player_choice_history) == 9):
        print("It's a tie, better luck next time.")
        break
    os.system('cls' if os.name == 'nt' else 'clear')
