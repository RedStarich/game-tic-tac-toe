# крестики - нолики, простейший вариант

# размер поля, количество клеток
board_size = 3
# игровое поле
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def draw_board():
    '''Выводим игровое поле'''
    print('_' * 4 * board_size)
    for i in range(board_size):
        print((' ' * 3 + '|')*3)
        print('', board[i*3], '|', board[1 + i*3], '|', board[2 + i*3], '|')
        print(('_' * 3 + '|')*3)

    pass

def game_step(index, char):
    '''выполняем ход'''

    if (index > 9 or index <1 or board[index-1] in ('X', 'O')):
        return False
    
    board [index-1] = char
    return True
    

def check_win():
    '''проверка при победе'''
    win = False

    win_combination = ((0, 1, 2), (3, 4, 5), (6, 7, 8), 
                       (0, 3, 6), (1, 4, 7), (2, 5, 8),
                       (0, 4, 8), (2, 4, 6))
    for pos in win_combination:
        if (board[pos[0]] == board[pos[1]] and board[pos[1]]==board[pos[2]]):
            win = board[pos[0]]

    return win


def start_game():
    #текущий игрок
    current_player = 'X'
    # номер шага
    step = 1
    draw_board()

    while (step<=9) and (check_win()==False):
        # Валидация входа значения для index
        while True:
            index = input('Ходит игрок ' + current_player + '. Введите номер поля (0 - выход): ')

            if index.isdigit():
                num = int(index)
                if 0 <= num <= 9:
                    break
            print('Неправильный ввод, попробуйте использовать число от 0 до 9')

        # Выход из игры если index = 0
        if (index == 0):
            break
        
        # Если получилось сделать шаг
        if (game_step(int(index), current_player)):
            print('Удачный ход')

            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'

            draw_board()
            #увеличим номер хода
            step += 1
        else:
            print('Неверный номер!')
    
    if step == 10:
        print('The game ends in a draw')
        
    else:
        print('The winner is: ' + check_win())
        
        
        
        
    

print("Let's play!")
start_game()
