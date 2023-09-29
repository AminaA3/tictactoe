# Tic tac toe game in Python.
# Build the board
# Player inputs
# Switching players
# checking for win or draw
# End

import random


game_board = [" ", " ", " ",
        " ", " ", " ",
        " ", " ", " "]
currentP = "X"
winner = None
gameLoop = True

# 1. variable for player who will be starting the game
# 2. variable that initializes winner to no one at the beginning of the game
# 3. variable controlling loop that tells the computer if winner is X or O or a draw to break out of the loop


# function to print the game board
def printBoard(game_board):
    print(game_board[0] + " | " + game_board[1] + " | " + game_board[2])
    print("----------")
    print(game_board[3] + " | " + game_board[4] + " | " + game_board[5])
    print("----------")
    print(game_board[6] + " | " + game_board[7] + " | " + game_board[8])


# function to take in player input to the board
def playerInput(game_board):
    inp = int(input("Select a spot 1-9: "))
    if game_board[inp-1] == " ":
        game_board[inp-1] = currentP
    else:
        print("Oops player is already at that spot.")


# checking for win or draw in all sides
def checkHorizontal(game_board):
    global winner
    if game_board[0] == game_board[1] == game_board[2] and game_board[0] != " ":
        winner = game_board[0]
        return True
    elif game_board[3] == game_board[4] == game_board[5] and game_board[3] != " ":
        winner = game_board[3]
        return True
    elif game_board[6] == game_board[7] == game_board[8] and game_board[6] != " ":
        winner = game_board[6]
        return True

def checkVertical(game_board):
    global winner
    if game_board[0] == game_board[3] == game_board[6] and game_board[0] != " ":
        winner = game_board[0]
        return True
    elif game_board[1] == game_board[4] == game_board[7] and game_board[1] != " ":
        winner = game_board[1]
        return True
    elif game_board[2] == game_board[5] == game_board[8] and game_board[2] != " ":
        winner = game_board[3]
        return True


def checkDiagonal(game_board):
    global winner
    if game_board[0] == game_board[4] == game_board[8] and game_board[0] != " ":
        winner = game_board[0]
        return True
    elif game_board[2] == game_board[4] == game_board[6] and game_board[4] != " ":
        winner = game_board[2]
        return True

# checking for a win
def checkIfWin(game_board):
    global gameLoop
    if checkHorizontal(game_board):
        printBoard(game_board)
        print(f"The winner is {winner}!")
        gameLoop = False
        exit()

    elif checkVertical(game_board):
        printBoard(game_board)
        print(f"The winner is {winner}!")
        gameLoop = False
        exit()

    elif checkDiagonal(game_board):
        printBoard(game_board)
        print(f"The winner is {winner}!")
        gameLoop = False
        exit()

# checking for a draw
def checkIfDraw(game_board):
    global gameLoop
    if " " not in game_board:
        printBoard(game_board)
        print("It is a Draw!")
        gameLoop = False
        exit()


# function to switch player
def switchPlayer():
    global currentP
    if currentP == "X":
        currentP = "O"
    else:
        currentP = "X"

# function to have another player as o
def randomPlayer(game_board):
    while currentP == "O":
        pos = random.randint(0, 8)
        if game_board[pos] == " ":
            game_board[pos] = "O"
            switchPlayer()


while gameLoop:
    printBoard(game_board)
    playerInput(game_board)
    checkIfWin(game_board)
    checkIfDraw(game_board)
    switchPlayer()
    randomPlayer(game_board)
    checkIfWin(game_board)
    checkIfDraw(game_board)