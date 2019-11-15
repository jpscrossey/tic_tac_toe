# tic tac toe

# BOARD DESIGN
from IPython.display import clear_output

def display_board(board):
    print("\n"*50)
    print("     |"+"     |"+"     ")
    print("  "+board[1]+"  |"+"  "+board[2]+"  |"+"  "+board[3]+"   ")
    print("_ _ _|"+"_ _ _|"+"_ _ _")
    print("     |"+"     |"+"     ")
    print("  "+board[4]+"  |"+"  "+board[5]+"  |"+"  "+board[6]+"   ")
    print("_ _ _|"+"_ _ _|"+"_ _ _")
    print("     |"+"     |"+"     ")
    print("  "+board[7]+"  |"+"  "+board[8]+"  |"+"  "+board[9]+"   ")
    print("     |"+"     |"+"     ")

# ASSIGN SYMBOLS TO PLAYERS
def player_input():
    
    symbol = []
    
    # KEEP ASKING PLAYER 1 TO CHOOSE 'X' OR 'O'
    while symbol != "X" and symbol != "O":
        symbol = input("\nPlayer 1 select a symbol of 'X' or 'O': ").upper()
    
    # ASSIGN PLAYER 2 OPPOSITE SYMBOL
    player1 = symbol
    
    if symbol == "X":
        return ("X","O")
    else:
        return ("O","X")

# ASSIGN SYMBOL TO POSITION ON BOARD
def place_symbol(board,symbol,position):
    board[position] = symbol

# CHECK FOR WINNING SYMBOL
def win_check(board,mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or # ACROSS THE TOP
            (board[4] == mark and board[5] == mark and board[6] == mark) or # ACROSS THE MIDDLE
            (board[7] == mark and board[8] == mark and board[9] == mark) or # ACROSS THE BOTTOM
            (board[1] == mark and board[4] == mark and board[7] == mark) or # DOWN THE LEFT
            (board[2] == mark and board[5] == mark and board[8] == mark) or # DOWN THE MIDDLE
            (board[3] == mark and board[6] == mark and board[9] == mark) or # DOWN THE RIGHT
            (board[1] == mark and board[5] == mark and board[9] == mark) or # DIAGONAL 1
            (board[3] == mark and board[5] == mark and board[7] == mark))   # DIAGONAL 2

# SELECT A PLAYER TO GO FIRST
import random

def first_turn():
    if random.randint(0,1) == 0:
        return "Player 2"
    else:
        return "Player 1"
    
# CHECK IF SPACE ON BOARD IS FREE
def space_check(board,position):
    return board[position] == " "

# CHECK IF BOARD IS FULL
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

# ASK FOR PLAYERS NEXT POSITION
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Choose your next position 1-9 "))
        
    return position

# ASK IF THEY WANT TO PLAY AGAIN
def replay():
    return input("\nWould you like to play again... Y / N ? ").upper().startswith("Y")

# RUNNING THE GAME
print("Lets play TIC TAC TOE!")

while True:
    # RESET THE BOARD
    theBoard = [" "] * 10
    player1_symbol,player2_symbol = player_input()
    turn = first_turn()
    print("\n" + turn + " will go first.")
    
    play_game = input("\nAre you ready to play... Y / N ? ").upper()
    
    if play_game == "Y":
        game_on = True
    else:
        game_on = False
        
    while game_on:
        if turn == "Player 1":
            # PLAYER 1'S TURN
            display_board(theBoard)
            print("\n")
            position = player_choice(theBoard)
            place_symbol(theBoard,player1_symbol,position)
            
            if win_check(theBoard,player1_symbol):
                display_board(theBoard)
                print("\nCongrats Player 1, you have won the game!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("\nThe game has ended in a draw!")
                    break
                else:
                    turn = "Player 2"
                    
        else:
            # PLAYER 2'S TURN   
            display_board(theBoard)
            print("\n")
            position = player_choice(theBoard)
            place_symbol(theBoard,player2_symbol,position)
            
            if win_check(theBoard,player2_symbol):
                display_board(theBoard)
                print("\nWell done Player 2, you have won the game!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("\nThe game has ended in a draw!")
                    break
                else:
                    turn = "Player 1"

    if not replay():
        break
        