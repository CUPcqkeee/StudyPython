# Крестики-Нолики


def fun(line):
    if line.replace('*', 'x') == 'xxx':
        return 'x'
    if line.replace('*', '0') == '000':
        return '0'
    return 'x0'


result = 'x0'
board = []

n = int(input())

# получаем и сразу проверяем строки
for _ in range(n):
    line = input().replace(' ', '')
    result = fun(line)
    if result != 'x0':
        break
    board.append(line)

# если в строках нет выигрышной комбинации проверяем столбцы
if result == 'x0':
    for i in range(n):
        coll = ''
        for j in range(n):
            coll += board[j][i]
        result = fun(coll)
        if result != 'x0':
            break

# если в столбцах нет выигрышной комбинации проверяем диагонали
if result == 'x0':
    coll = ''
    for i in range(n):
        coll += board[i][i]
    result = fun(coll)

if result == 'x0':
    coll = ''
    for i in range(n):
        coll += board[i][-1 - i]
    result = fun(coll)

print(result)
