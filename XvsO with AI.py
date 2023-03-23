# X vs O, simple game with AI

# size of the board, number of rows
board_size = 3

# identification of positions in the table
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

MODE_HUMAN_VS_HUMAN = '1'
MODE_HUMAN_VS_AI = '2'


#------------------------------------------------------------------------------------------
# define our functions

def draw_board():
    '''draw the table'''
    print('_' * 4 * board_size)
    for i in range(board_size):
        print((' ' * 3 + '|')*3)
        print('', board[i*3], '|', board[1 + i*3], '|', board[2 + i*3], '|')
        print(('_' * 3 + '|')*3)

#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
def game_step(index, char):
    '''move management between two players'''

    if (index > 9 or index <1 or board[index-1] in ('X', 'O')):
        return False
    
    board [index-1] = char
    return True
    
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
def check_win(board):
    '''condition of winning by one of the players'''

    win = False
    
    win_combination = ((0, 1, 2), (3, 4, 5), (6, 7, 8), 
                       (0, 3, 6), (1, 4, 7), (2, 5, 8),
                       (0, 4, 8), (2, 4, 6))
    for pos in win_combination:
        if (board[pos[0]] == board[pos[1]] and board[pos[1]]==board[pos[2]]):
            win = board[pos[0]]

    return win

#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
def computer_step(human, ai):
    '''simple AI script for the XvsO game'''

    # find available moves
    available_steps = [i-1 for i in board if type(i) == int]

    # set the best options in priority order
    win_steps = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    for char in (ai, human):
        for pos in available_steps:
            # clone the game board for AI
            board_ai = board[:]
            board_ai[pos] = ai
            if (check_win(board_ai) != False):
                return pos
            

    # in case no winning moves
    for pos in win_steps:
        if (pos in available_steps):
            return pos
        
   

    # combination calculation
    
    return False        # if everything is bad

#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
def next_player(current_player):
    '''find who's move is next: AI or a second human'''
    if (current_player == 'X'):
        return 'O'
    return 'X'



#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
def start_game(mode):
    
    current_player = 'X'    # first move by the player X
    ai_player = 'O'
    step = 1                # count of the step/move order
    draw_board()

    while (step<10) and (check_win(board)==False):

        while True:
            # check if index input is valid
            # index is a variable that defines which position is chosen by a player
            index = input('Player ' + current_player 
            + ', choose your position, (press 0 to leave the game): ')
            if index.isdigit():
                num = int(index)
                if 0 <= num <= 9:
                    break
            print('Incorrect input, try numbers from 0 to 9')


        if (index == 0):        # leave the game if index is '0'
            break        
        
        if (game_step(int(index), current_player)):
            
            print('Success')                # if the step is successful
            current_player = next_player(current_player)          

            
            
# AI script
            if (mode == MODE_HUMAN_VS_AI):
                ai_step = computer_step('X', 'O')
                if (type(ai_step) == int):
                    # if AI chooses a position

                    board[ai_step] = ai_player
                    current_player = next_player(current_player)
                    # computer acts
                print('Bot acitvated')

            step += 1                       # next step
            draw_board()                    # update the board

        else:
            print('Incorrect number!')      # if the input index is taken or invalid
    
    if step == 10:
        # if we reached maximum step count and no one has won
        print('The game ends in a draw')
        
    elif check_win(board) != False:
        # if someone has won, we show the result
        print('The winner is: ' + check_win(board))

#----------------------------------------------------------------------------------------        
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------        
# main game

print("Let's play!")
mode = 0
while mode not in (MODE_HUMAN_VS_HUMAN, MODE_HUMAN_VS_AI):
    mode = input("Choose game mode: \n1 - play with a friend, \n2 - play with a` bot \n")

start_game(mode)