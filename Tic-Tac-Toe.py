# Создание структуры карты в консоли
from KrestikiNoliki import NUM_SQUARES, EMPTY

maps = [1, 2, 3,
        4, 5, 6,
        7, 8, 9,
        "――――――",
        "|"]

# Вывод победных линий
victory = [[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8],
           [0, 3, 6],
           [1, 4, 7],
           [2, 5, 8],
           [0, 4, 8],
           [2, 4, 6]]


# Вывод карты на экран
def print_maps():
    print(maps[9])

    print(maps[0], end=" ")
    print(maps[10], end=" ")
    print(maps[1], end=" ")
    print(maps[10], end=" ")
    print(maps[2])

    print(maps[3], end=" ")
    print(maps[10], end=" ")
    print(maps[4], end=" ")
    print(maps[10], end=" ")
    print(maps[5])

    print(maps[6], end=" ")
    print(maps[10], end=" ")
    print(maps[7], end=" ")
    print(maps[10], end=" ")
    print(maps[8])

    print(maps[9])


# Функция хода в ячейки
def move_maps(move, value):
    ind = maps.index(move)
    maps[ind] = value


# Ядро программы
game_over = False
player1 = True


# Получить текущий результат игры
def get_result():
    win = ""

    for i in victory:
        if maps[i[0]] == "☒" and maps[i[1]] == "☒" and maps[i[2]] == "☒":
            win = "Игрок 1"
        if maps[i[0]] == "🄾" and maps[i[1]] == "🄾" and maps[i[2]] == "🄾":
            win = "Игрок 2"

    return win


while game_over == False:

    # Выводим карту перед началом игры
    print_maps()

    # Функция, вопроса хода
    if player1:
        value = "☒"
        move = int(input("Игрок 1, ваш ход: "))
    else:
        value = "🄾"
        move = int(input("Игрок 2, ваш ход: "))

    move_maps(move, value)  # делаем ход в указанную ячейку
    win = get_result()  # определим победителя
    if win != "":
        game_over = True
    else:
        game_over = False

    player1 = not (player1)


def error_step(maps, player1):
    legal = legal_moves(maps)
    step = None
    while step not in legal:
        if step not in legal:
            print("\nДанной поле занято, выбирайте другое\n")
    print("Хорошо.....")
    return step


def legal_moves(board):
    """Создает список доступных ходов """
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


# Конец игры
print_maps()
print("Победил", win)
