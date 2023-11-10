# A python based implementation of the game tic-tac-toe

from os import system

grid = ["_", "_", "_",
        "_", "_", "_",
        "_", "_", "_"]

player_turn = "X"


def displayGrid():
    # Clunky string operations: takes a whole row of the grid, makes it a string, then strips off the quotes and commas. 
    print(str(grid[0:3]).replace("'", "").replace(",", ""))
    print(str(grid[3:6]).replace("'", "").replace(",", ""))
    print(str(grid[6:9]).replace("'", "").replace(",", ""))

def checkConflict(player_choice):
    if grid[player_choice - 1] != "_":
        return True
    return False

def writeToGrid(player_choice):
    grid[player_choice - 1] = player_turn

def checkVictory():
    # Checks for horizontal matches
    if grid[0] == grid[1] == grid[2] != "_" or grid[3] == grid[4] == grid[5] != "_" or grid[6] == grid[7] == grid[8] != "_":
        return True
    # Checks for vertical matches
    if grid[0] == grid[3] == grid[6] != "_" or grid[1] == grid[4] == grid[7] != "_" or grid[2] == grid[5] == grid[8] != "_":
        return True
    # Checks for diagonal matches
    if grid[0] == grid[4] == grid[8] != "_" or grid[2] == grid[4] == grid[6] != "_":
        return True
    return False

def checkTie():
    return "_" not in grid


while True:
    system("clear")
    displayGrid()
    player_choice = input(f"It's {player_turn}'s turn. Input a number from 1-9: ")

    # Attempts to turn user input to a number from 1-9
    try:
        player_choice = int(player_choice)
        if player_choice not in range(1, 9):
            continue
    except ValueError:
        continue

    # Checks if user is trying to input on an already drawn square
    if checkConflict(player_choice):
        continue

    # Writes X or O to the user's selected space
    writeToGrid(player_choice)

    # Checks if a player won
    if checkVictory():
        system("clear")
        displayGrid()
        print(f"{player_turn} has won!!!")
        break

    # Checks if both players tied
    if checkTie():
        system("clear")
        displayGrid()
        print(f"Tie Game.")
        break

    # Switches turns for the next round
    if player_turn == "X":
        player_turn = "O"
    else:
        player_turn = "X"