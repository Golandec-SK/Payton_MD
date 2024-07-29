"""
                Пвсевдокод
вывести на экран инструкцию для игрока
решить, кому принадлежит первый ход
создать пустую доскудля игры в "Крестики - нолики"
отобразить эту доску
до тех пор пока ни кто не выиграл или не состоялась ничья
    если сейчас ход пользователя
        получить ход из пользовательского ввода
        изменить вид доски
    иначе
        расчитать ход компьютера
        изменить вид доски
    вывести на экран обновленый вид доски
    осуществить переход хода
поздравить победителя или констатировать ничью
    """

# Крестики - нолики
# Компьютер играет в крестики-нолики против пользователя
# глобальные константы

X = 'X'
O = 'O'

EMPTY = ' '
TIE = 'Ничья'
NUM_SQUARES = 9


def display_instruct():
    """Выводит на экран инструкцию для игрока."""
    print(
        """
    Добро пожаловать на ринг грандиознейших интелектуальных состязаний всех
    времен. Твой мозг и мой процессор сойдеться в схватке за доской игры
    'Крестики-нолики'. Что бы сделать ход, введите число от 0 до 8. Числа
    однозначно соответствуют полям доски - так, как показана ниже:

                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8

    Приготовься к бою, жалкий белковый человечишка. Вот-вот начнется решающее
    сражение.\n
    """
    )


def ask_yes_no(question):
    """Задать вопрос с ответом 'Да' или 'Нет'."""
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower()
    return response


def ask_number(question, low, high, step = 1):
    """Просит ввести число из диапозона."""
    response = None
    while response not in range(low, high, step):
        response = int(input(question))
    return response


def pieces():
    """Определяет пренадлежность первого хода"""
    go_first = ask_yes_no('Хочешь оставить за собой первый ход?(y/n):')
    if go_first == 'y':
        print('\nНу что ж, даю тебе фору: играй крестиками.')
        human = X
        computer = O
    else:
        print('\nТвоя удаль тебя погубит... Буду начитнать я.')
        computer = X
        human = O
    return computer, human


def new_board():
    """Создает новую игровую доскку"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """Отображает игровую доску на экране"""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")


def legal_moves(board):
    """Создает список доступных ходов."""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    """Определяет победителя в игре"""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    # если все строки равны и не пусты, победителем
    # становится символ, заполняющий квадраты.
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        # если на доске нет пустых клеток, то это ничья
        if EMPTY not in board:
            return TIE


def human_move(board, human):
    """Получает ход человека."""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move? (0 - 8): ", 0, NUM_SQUARES)
        if move not in legal:
            print('\nСмешной человек! Это поле уже занято. Выбери другое.\n')
    print('Ладно...')
    return move


def computer_move(board, computer, human):
    """Делает ход за компьютерного противника"""
    # # создадим рабочую копию доски, потому что функция будет
    # # менятьнекоторые значения в списке
    # board = board[:]
    # # поля от лучшего к худшему
    # BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    # print('Я выберу поле номера', end=' ')
    # for move in legal_moves(board):
    #     board[move] = computer
    # # если следующий ход может победить компьютер, выбераем этот ход
    #     if winner(board) == computer:
    #         print(move)
    #         return move
    # # выполнив проверку, отменим внесенные изменения
    #     board[move] = EMPTY
    # for move in legal_moves(board):
    #     board[move] = human
    # # если следующий ходом может победить человек, блокируем этот ход
    #     if winner(board) == human:
    #         print(move)
    #         return move
    # # выполнить проверку, отменим внесения изменения
    #     board[move] = EMPTY
    # # поскольку следующий ходом ни одна сторона не может победить.
    # # выберем лучшее из доступных полей
    # for move in BEST_MOVES:
    #     if move in legal_moves(board):
    #         print(move)
    #         return move
 # make a copy to work with since function will be changing list
def computer_move(board, computer, human):
    """Делает ход за компьютерного противника"""
    # создадим рабочую копию доски, потому что функция будет
    # менятьнекоторые значения в списке
    board = board[:]
    # поля от лучшего к худшему
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Я выберу поле номера", end=" ")
    for move in legal_moves(board):
        board[move] = computer
        # если следующий ход может победить компьютер, выбераем этот ход
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY

    # выполнив проверку, отменим внесенные изменения
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # выполнить проверку, отменим внесения изменения
        board[move] = EMPTY

    # если доска пуста, возьмите край
    moves_left = len(legal_moves(board))
    if moves_left == 9:
        move = 7
        print(move)
        return move

    # в случае второго хода, берите центр, если угловой взят
    # берите угол, следующий за краем, или берите угол, если центр взят.
    
    elif moves_left == 8:
        if (0 not in legal_moves(board)) or (2 not in legal_moves(board)) or \
           (6 not in legal_moves(board)) or (8 not in legal_moves(board)):
            move  = 4
        elif (1 not in legal_moves(board)) or (3 not in legal_moves(board)):
            move = 0
        elif (5 not in legal_moves(board)) or (7 not in legal_moves(board)):
            move = 8
        else:
            move = 0
        print(move)
        return move
    
    
    # если сделать третий ход, то компьютер сделает 7 ход, а человек - еще один
    elif moves_left == 7:
        if 4 not in legal_moves(board):
            move = 0
        else:
            move = 4
        print(move)
        return move

    # если четвертый ход и центр еще не сделан, делайте его!
    # в противном случае, если оба угла на противоположных сторонах
    # центральной фигуры заняты, принимайте сторону.
    # в противном случае следуйте "лучшим ходам"
    elif moves_left == 6:
        if 4 in legal_moves(board):
            move = 4
            print(move)
            return move
        elif (0 not in legal_moves(board)) and (4 not in legal_moves(board)) \
             and (8 not in legal_moves(board)):
            move = 7
            print(move)
            return move
        elif (2 not in legal_moves(board)) and (4 not in legal_moves(board)) \
             and (6 not in legal_moves(board)):
            move = 1
            print(move)
            return move
    

    # если пятый ход и человек сделал глупый ход (значит, он не пытается выиграть)
    elif moves_left == 5:
        if (4 not in legal_moves(board)) and (1 not in legal_moves(board)):
            # обратите внимание, что 7 и 0 не будут использоваться,
            # так как компьютер уже принял их
            move = 6
        print('Используя пятый ход')
        print(move)
        return move
        
    
    # в противном случае, примите наилучшие меры
    BEST_MOVES = (0, 2, 4, 6, 8, 1, 3, 5, 7)
    for move in BEST_MOVES:
        print('Using best moves')
        if move in legal_moves(board):
            print(move)
            return move


def next_turn(turn):
    """Осуществляет переход хода."""
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner, computer, human):
    """Поздровляем победителя игры."""
    if the_winner != TIE:
        print(f'Три {the_winner} в ряд!\n')
    else:
        print('Ничья\n')
    if the_winner == computer:
        print('Как я и предсказывал, победа в очередной раз за мной. \n'
              'Вот еще один довод, что компьютеры превосходят людей во всем.')
    elif the_winner == human:
        print('Этого не может быть! Ты сумел перехитрить меня, белковый?\n'
              'Клянусь: я, компьютер, не допущу этого больше никогда!')
    elif the_winner == TIE:
        print('Тебе несказанно повезло, ты сумел свести игру вничью. \n'
              'Радуйсяже сегодняшнему успеху! В следующей раз тебе\
        уже не суждено его повторить')


def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


main()

input('\n\nНажмите Enter, что выйти.')