def init_board():
    # Инициализация пустой доски
    board = [['1', '2', '3'],
             ['4', '5', '6'],
             ['7', '8', '9']]
    return board

def print_board(board):
    # Вывод игрового поля на экран
    for row in board:
        print(' | '.join(row))
        print('---------')

def check_winner(board, player):
    # Проверка, есть ли победитель
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    # Проверка, заполнена ли доска
    for row in board:
        for cell in row:
            if cell not in ['X', 'O']:
                return False
    return True

def play_game():
    board = init_board()
    current_player = 'X'

    while True:
        print_board(board)

        # Получение хода от пользователя
        move = input(f'Ход игрока {current_player}. Введите номер клетки (1-9): ')
        
        # Проверка на корректность ввода и доступность клетки
        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print('Некорректный ввод. Введите число от 1 до 9.')
            continue

        row = (int(move) - 1) // 3
        col = (int(move) - 1) % 3

        if board[row][col] in ['X', 'O']:
            print('Клетка уже занята. Выберите другую.')
            continue

        # Обновление доски
        board[row][col] = current_player

        # Проверка наличия победителя
        if check_winner(board, current_player):
            print_board(board)
            print(f'Игрок {current_player} победил!')
            break

        # Проверка на заполненность доски
        if is_board_full(board):
            print_board(board)
            print('Ничья!')
            break

        # Смена игрока
        current_player = 'X' if current_player == 'O' else 'O'

if __name__ == "__main__":
    play_game()
