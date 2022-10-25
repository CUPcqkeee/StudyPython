# a = 5
# b = 6

# def name_function_multiply(num_1, num_2):
#    result = num_1 * num_2
#    return result
#
# print(name_function_multiply(a, b))

def create_field(size: int = 3) -> list:
    game_field = []
    for i in range(0, size):
        temp_arr = []
        for o in range(0, size):
            temp_arr.append('_')
        game_field.append(temp_arr)
    return game_field


def render_game_field(field: list) -> None:
    for i in field:
        for l in i:
            print(l + " ", end="")
        print()


def create_player(name: str, char: str) -> dict:
    dict = {}
    dict['name'] = name
    dict['char'] = char
    return dict


def switch_player():
    global flag_player
    if flag_player == True:
        flag_player == False
    else:
        flag_player == True


def is_empty_cell(game_field, index_row, index_column):
    if game_field[index_row][index_column] == 'X' or game_field[index_row][index_column] == '0':
        return False
    else:
        return True


def check_horizontally_line(g_f, i_r, i_c, s_f):
    if s_f == 3:
        if g_f[i_r][i_c] == g_f[i_r][i_c + 1] and g_f[i_r][i_c] == g_f[i_r][i_c + 2]:
            return True
    return False


def game_logic(game_field, index_row, index_column, size_field):
    check_h_line = check_horizontally_line(game_field, index_row, index_column, size_field)


def player_turn(game_field):
    index_row = int(input('row: ')) - 1
    index_column = int(input('column: ')) - 1

    size_field = len(game_field)

    # game_field[row - 1][column - 1] = 'X'

    if index_row > size_field or index_column > size_field:
        print('out of range')
        return 0
    else:
        if is_empty_cell(game_field, index_row, index_column):
            if flag_player == True:
                game_field[index_row][index_column] = 'X'
            else:
                game_field[index_row][index_column] = '0'
            switch_player()
            turn_game_count

    # cell = int(input('cell 1-9:'))
    # if cell > 0 and cell < 4:
    #     # print(game_field[2])
    #     # print("______________")
    #     # print(game_field[2][cell - 1])
    #
    #     game_field[2][cell - 1] = '?'
    # if cell > 3 and cell < 7:
    #     game_field[1][cell - 1] = '?'
    # if cell > 6 and cell < 10:
    #     game_field[0][cell - 1] = '?'
    # #game_field[?][?]


SIZE = 4

game_field = create_field()
render_game_field(game_field)

player_1 = create_player("First", "X")
player_2 = create_player("Second", "O")
flag_player = True
turn_game_count = 0
while True:
    player_turn(game_field)
    render_game_field(game_field)
