import random

# Function to create the board
def create_board(length=30, penalty_prob=0.3):
    return ['P' if random.random() < penalty_prob else '_' for _ in range(length)]

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)

# Function to print the current state of the board
def print_board(board, player_a_pos, player_b_pos, player_a_penalty, player_b_penalty):
    board_copy = board[:]
    for i in range(len(board_copy)):
        if i == player_a_pos and i == player_b_pos:
            board_copy[i] = 'X' if board[i] == '_' else 'x'
        elif i == player_a_pos:
            board_copy[i] = 'A' if board[i] == '_' else 'a'
        elif i == player_b_pos:
            board_copy[i] = 'B' if board[i] == '_' else 'b'
    
    print("Board: ", " ".join(board_copy))

# Function to print the final state of the board with penalty squares revealed
def print_final_board(board):
    print("Final Board: ", " ".join(['P' if square == 'P' else '_' for square in board]))

# Main game loop
def play_game():
    board_length = 30
    board = create_board(board_length)
    player_a_pos = 0
    player_b_pos = 0
    player_a_penalty = False
    player_b_penalty = False
    
    while player_a_pos < board_length - 1 and player_b_pos < board_length - 1:
        if not player_a_penalty:
            move_a = roll_dice()
            player_a_pos += move_a
            if player_a_pos >= board_length - 1:
                player_a_pos = board_length - 1
            player_a_penalty = board[player_a_pos] == 'P'
        else:
            player_a_penalty = False
        
        if not player_b_penalty:
            move_b = roll_dice()
            player_b_pos += move_b
            if player_b_pos >= board_length - 1:
                player_b_pos = board_length - 1
            player_b_penalty = board[player_b_pos] == 'P'
        else:
            player_b_penalty = False
        
        print_board(board, player_a_pos, player_b_pos, player_a_penalty, player_b_penalty)
        
        if player_a_pos == board_length - 1 and player_b_pos == board_length - 1:
            print("Both players reach the end. Both win!")
            break
        elif player_a_pos == board_length - 1:
            if player_b_penalty:
                print("Player A reaches the end. Player A wins!")
                break
        elif player_b_pos == board_length - 1:
            print("Player B reaches the end. Player B wins!")
            break

    print_final_board(board)

# Start the game
play_game()