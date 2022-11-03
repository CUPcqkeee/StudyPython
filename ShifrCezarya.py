print("Предупреждаем сразу, что доступен только Русский язык")
user_input = input("Введите текс для шифровки: ")
user_shag = int(input("Введите количество на которое перевести буквы: "))


def caesar_text(user_input, user_shag):
    result = ''
    for function_ru in user_input:
        if function_ru.isalpha():  # Проверка, что строка состоит из буквенных символом
            # Узнаёт число буквы введёной пользователем, и прибавляет к нему user_shag
            user_input = ord(function_ru) + user_shag
            if user_input > ord('я'):  # Если user_input вышел за грани числа "я"
                user_input -= 26  # user_input -=26
            final = chr(user_input)  # Конец программы, преобразовавыем численное в строку, обратная ord()
            result += final
    print("Шифр удался: ", result)
    return result  # Возвращаем result


caesar_text(user_input, user_shag)  # Вызов функции
