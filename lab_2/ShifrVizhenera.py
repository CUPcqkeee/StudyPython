#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  szyfr_viegenera2.py

def msg_and_key():
    msg = input("Wprowadź wiadomość: ").upper()
    key = input("Wprowadź klucz: ").upper()

    # zmienna przechowująca zmapowany klucz
    key_map = ""

    j = 0
    for i in range(len(msg)):
        if ord(msg[i]) == 32:  # ord zamienia litery na znaki w kodzie ASCII
            # ignorowanie spacji
            key_map += " "
        else:
            if j < len(key):
                key_map += key[j]
                j += 1
            else:
                j = 0
                key_map += key[j]
                j += 1

    return msg, key_map


def tabela_vigenera():
    table = []
    for i in range(33):
        table.append([])

    for row in range(33):
        for column in range(33):
            if (row + 65) + column > 90:
                # gdy dojdzie do końca alfabetu zaczyna znów od A
                # po pierwszym rzędzie, każda litera będzie przesunięta o jedną pozycję w lewo względem górnego rzędu
                table[row].append(chr((row + 65) + column - 33))
            else:
                # po pierwszym rzędzie, każda litera będzie przesunięta o jedną pozycję w lewo względem górnego rzędu
                table[row].append(chr((row + 65) + column))

    # drukowanie tablicy
    # for row in table:
    #     for column in row:
    #         print(column, end=" ")
    #     print(end="\n")

    return table


def szyfrowanie(message, mapped_key):
    table = tabela_vigenera()
    szyfrowany_tekst = ""

    for i in range(len(message)):
        if message[i] == chr(32):
            # ignorowanie spacji
            szyfrowany_tekst += " "
        else:
            # branie elementu za pomocą specjalnego indeksu z tabeli
            row = ord(message[i]) - 65
            column = ord(mapped_key[i]) - 65
            szyfrowany_tekst += table[row][column]

    print("Zaszyfrowana wiadomość: {}".format(szyfrowany_tekst))


def zlicz(mapped_key, message):
    licznik = 0
    wynik = ""

    # gdy dojdzie do końca alfabetu zaczyna znów od A
    for i in range(33):
        if mapped_key + i > 90:
            wynik += chr(mapped_key + (i - 33))
        else:
            wynik += chr(mapped_key + i)

    # zliczaanie interacji od mapped_key do szyfrowania
    for i in range(len(wynik)):
        if wynik[i] == chr(message):
            break
        else:
            licznik += 1

    return licznik


def deszyfrowanie(message, mapped_key):
    table = tabela_vigenera()
    deszyfrowany_tekst = ""

    for i in range(len(message)):
        if message[i] == chr(32):
            # ignorowanie spacji
            deszyfrowany_tekst += " "
        else:
            deszyfrowany_tekst += chr(65 + zlicz(ord(mapped_key[i]), ord(message[i])))

    print("Odszyfrowana wiadomość: {}".format(deszyfrowany_tekst))


def main(args):
    print("Klucz i wiadomość muszą być ciągiem znaków")
    wybor = int(input("1. Szyfrowanie\n2. Deszyfrowanie\nWybierz(1,2): "))
    if wybor == 1:
        print("---Szyfrowanie---")
        message, mapped_key = msg_and_key()
        szyfrowanie(message, mapped_key)

    elif wybor == 2:
        print("---Deszyfrowanie---")
        message, mapped_key = msg_and_key()
        deszyfrowanie(message, mapped_key)


if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))