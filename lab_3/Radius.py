import math


def lenght(x, y):
    if x != 0 and y and x != 0 and y != 0:
        formula = int(math.sqrt(abs(x) ** 2 + abs(y) ** 2 + abs(x) ** 2 + abs(y) ** 2))
    else:
        formula = 0
    return formula


def math_forumla(x, y, R):
    if x and y > R:
        formula = int(math.sqrt(x ** 2 + (abs(y) - R) ** 2 + (x) ** 2 + (abs(y))))
    elif x and y < R:
        formula = int(math.sqrt(x ** 2 + (R - abs(y)) ** 2 + (R - x) ** 2 + (abs(y))))
    elif x and y == R:
        formula = x and y
    return formula


while True:
    x = int(input('Введите координату X: '))
    y = int(input('Введите координату Y: '))
    if x == 0 and y == 0 and len(x) and len(y) == 1:
        break
    else:
        R = int(input('Введите координату R: '))
        if lenght(x, y) == 0:
            print('расстоояние до контура полукоружности равно', R)
        elif x and y > 0:
            print('расстоояние до контура полукоружности равно', math_forumla(x, y, R))
        elif lenght(x, y) < R:
            print('расстоояние до контура полукоружности равно', R - lenght(x, y))
        else:
            print('расстоояние до контура полукоружности равно', lenght(x, y) - R)
