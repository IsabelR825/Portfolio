#---GLOBAL VARIABLES ----

#if game is still going
game_still_going = True

#Who won? or tie
winner = None

#Who's turn is it?
current_player = "X"


#board
board = ["-", "-", "-",
         "-", "-", "-", 
         "-", "-", "-"]

#function to display board
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


#definition to play game
def play_game():
    
    #Display board
    display_board()

    while game_still_going:

        #takes player value (see function which takes player value also)
        handle_turn(current_player)

        check_if_game_over()

        #flip to next player
        flip_player()

   #The game has ended
    if winner == "X" or winner == "0":
       print(winner +  "won!")
    elif winner == None:
        print("Tie.")


#choose position on game board
#handle_tur(player) means that it takes a value depending on the player
def handle_turn(player):
    position = input("Choose a position from 1-9: ")
    position = int(position) - 1

    board[position] = 'X'
    display_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():

    #setup global variables
    global winner

    #check rows
    row_winner = check_rows
    #check columns
    column_winner = check_columns
    #check diagonals
    diagonal_winner = check_diagonals

    if row_winner:
        #there was a win
        winner = row_winner
    elif column_winner:
        #there was a winner
        winner = column_winner
    elif diagonal_winner:
        #there was a win
        winner = diagonal_winner
    else:
        #there was no win
        winner = None
    
def check_rows():
    #set up global variable (check if game is still going)
    global game_still_going
    #check if any rows have the same player value
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    
    if row_1 or row_2 or row_3:
        game_still_going = False
    #return winner X or O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    #set up global variable (check if game is still going)
    global game_still_going
    #check if any rows have the same player value
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    
    if column_1 or column_2 or column_3:
        game_still_going = False
    #return winner X or O
    if column_1:
        return board[0]
    elif column_2:
        return board[3]
    elif column_3:
        return board[6]
    return
    return

def check_diagonals():
    #set up global variable (check if game is still going)
    global game_still_going

    #check if any rows have the same player value
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"
    
    if diagonal_1 or diagonal_2:
        game_still_going = False
    #return winner X or O
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return

def check_if_tie():
    return

def flip_player():
    return


play_game()


#check win
    
#check tie
#flip player