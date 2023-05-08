import pprint
from time import sleep

# List comprehension
# Generator expression

# [ВЫРАЖЕНИЕ/ПРЕОБРАЗОВАНИЕ for element in ИСТОЧНИК if УСЛОВИЕ]

squares = [e ** 2 for e in range(10) if e % 2 == 0]  # Фильтрация и преобразование

text = 'hello world'
words = [word.capitalize() for word in text.split()]  # Только преобразование

ints = [-1, -2, 0, 3, -4]
positives = [e for e in ints if e > 0]  # Только фильтрация

letters = [letter for word in text.split() for letter in word if letter < 'l']

matrix = [list(range(x, x + 3)) for x in range(3)]

unique = {letter for word in text.split() for letter in word if letter < 'o'}  # Set comprehension

alphabet = {index: letter for index, letter in enumerate('abcdefghijklnop')}  # Dict comprehension

positives_gen = (e for e in ints if e > 0)


def some_source():
    print('!!!')
    sleep(3)
    return [1, 2, 3]


if __name__ == '__main__':
    # print(squares)
    # print(words)
    # print(positives)
    # print(letters)
    # pprint.pprint(matrix, indent=1, width=15)
    # print(unique)
    # print(alphabet)
    # print(positives_gen)  # generator
    gen = (e for e in some_source())  # Генератор проверяет свой источник
