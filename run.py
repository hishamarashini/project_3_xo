import os
import random

game_grid = []
player_choice_history = []
computer_choice_history = []


def check_target_status(_target):
    for i in range(3):
        # if the cell is to the absolute left:
        if i % 3 == 0:
            # check if 3 consecutive cells are selected. eg: (123, 456, 789)
            if i in _target and i + 1 in _target and i + 2 in _target:
                return True
        # if the value is below 3. Reason being, to check if any vertically
        # consecutive cells are selected from top to bottom eg: (147, 258, 369)
        if i < 3:
            if i in _target and i + 3 in _target and i + 6 in _target:
                return True

    # checking diagonal top left to bottom right
    if 0 in _target and 4 in _target and 8 in _target:
        return True
    # checking diagonal top right to bottom left
    if 2 in _target and 4 in _target and 6 in _target:
        return True
    # if none of the above returned true, then no winning scenarios were achieved
    return False


def computer_choose():
    global player_choice_history
    global computer_choice_history
    choice = -1
    while True:
        # choosing a random number from the valid cells in the grid
        random_choice = random.randint(0, 8)
        # checking if the random choice collides with a previous choice
        if random_choice not in player_choice_history and random_choice not in computer_choice_history:
            # if it doesn't, choose this cell and break out of the loop. else repeat until it doesn't collide
            choice = random_choice
            break
    return choice


def gen_game_grid():
    global player_choice_history
    global computer_choice_history

    to_return = ""
    for j in range(9):
        if j in player_choice_history:
            i = "X"
        elif j in computer_choice_history:
            i = "O"
        else:
            i = j + 1

        if (j + 1) % 3 == 0:
            to_return += f"{i}\n"
        else:
            to_return += f"{i} | "

    return to_return


print("Welcome to X||O (The Game)).")
while True:
    print(gen_game_grid())
    user_input = input("Choose a number from the grid to make a move; or q to quit game: \n")
    if user_input == "q":
        print("Thanks for playing the game.")
        break
    if user_input.isdigit:
        user_input = int(user_input)

    player_choice_history.append(user_input - 1)
    if check_target_status(player_choice_history):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You won. Good job.")
        print(gen_game_grid())
        break

    if len(computer_choice_history) + len(player_choice_history) >= 9:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("It's a tie, better luck next time.")
        print(gen_game_grid())
        break

    computer_choice_history.append(computer_choose())
    if check_target_status(computer_choice_history):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Computer won. Better luck next time.")
        print(gen_game_grid())
        break
    os.system('cls' if os.name == 'nt' else 'clear')
