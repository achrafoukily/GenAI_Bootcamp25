#Mini-Project - Tic Tac Toe :
#Instructions:
#Tic Tac Toe is played on a 3x3 grid. Players take turns marking empty squares with their symbol (‘O’ or ‘X’). The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins. If all squares are filled and no player has three in a row, the game is a tie.

#Step 1: Representing the Game Board
#You’ll need a way to represent the 3x3 grid.
#A list of lists (a 2D list) is a good choice.
#Initially, each cell in the grid should be empty (e.g., represented by a space ‘ ‘).

#Step 2: Displaying the Game Board
#Create a function called display_board() to print the current state of the game board.
#The output should visually represent the 3x3 grid.
#Think about how to format the output to make it easy to read.

#Step 3: Getting Player Input
#Create a function called player_input(player) to get the player’s move.
#The function should ask the player to enter a position (e.g., row and column numbers).
#Validate the input to ensure it’s within the valid range and that the chosen cell is empty.
#Think about how to ask the user for input, and how to validate that input.

#Step 4: Checking for a Winner
#Create a function called check_win(board, player) to check if the current player has won.
#The function should check all possible winning combinations (rows, columns, diagonals).
#If a player has won, return True; otherwise, return False.
#Think about how to check every possible winning combination.

#Step 5: Checking for a Tie
#Create a function to check if the game has resulted in a tie.
#The function should check if all positions of the board are full, without a winner.

#Step 6: The Main Game Loop
#Create a function called play() to manage the game flow.
#Initialize the game board.
#Use a while loop to continue the game until there’s a winner or a tie.
#Inside the loop:
#Display the board.
#Get the current player’s input.
#Update the board with the player’s move.
#Check for a winner.
#Check for a tie.
#Switch to the next player.
#After the loop ends, display the final result (winner or tie).


board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

current_player = "X"
game_running = True
winner = None

def display_board(board):
  print("***********")
  print(board[0] + " | " + board[1] + " | " + board[2])
  print("--|---|---")
  print(board[3] + " | " + board[4] + " | " + board[5])
  print("--|---|---")
  print(board[6] + " | " + board[7] + " | " + board[8])
  print("***********")


def player_input(board):
  print(f"It's your turn player {current_player}")
  inp = int(input("Enter a number 1-9: "))
  if 1 <= inp <= 9 and board[inp-1] == "-":
    board[inp-1] = current_player
  else :
    print("Taking spot ! ! ! Try again.")
    switch_player()

def check_win(board):
  global game_running
  global winner
  if board[0] == board[1] == board[2] != "-":
    winner = board[0]
    display_board(board)
    print(f"the winner is player :{winner}")
    game_running = False
  elif board[3] == board[4] == board[5] != "-":
    winner = board[3]
    display_board(board)
    print(f"the winner is player :{winner}")
    game_running = False
  elif board[6] == board[7] == board[8] != "-":
    winner = board[6]
    display_board(board)
    print(f"the winner is player :{winner}")
    game_running = False
  elif board[0] == board[3] == board[6] != "-":
    winner = board[0]
    display_board(board)
    print(f"the winner is player :{winner}")
    game_running = False
  elif board[1] == board[4] == board[7] != "-":
    winner = board[1]
    display_board(board)
    print(f"the winner is player :{winner}")
    game_running = False
  elif board[2] == board[5] == board[8] != "-":
    winner = board[2]
    display_board(board)
    print(f"the winner is player :{winner}")
    game_running = False
  elif board[0] == board[4] == board[8] != "-":
    winner = board[0]
    display_board(board)
    print(f"the winner is player :{winner}")
    game_running = False
  elif board[2] == board[4] == board[6] != "-":
    winner = board[2]
    display_board(board)
    print(f"the winner is player :{winner}")
    game_running = False

def check_tie(board):
  global game_running
  global winner
  if "-" not in board and winner == None :
    display_board(board)
    print("it's a tie")
    game_running = False

def switch_player():
  global current_player
  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"


while game_running :
  display_board(board)
  player_input(board)
  check_win(board)
  check_tie(board)
  switch_player()
  