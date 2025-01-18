"""
Реализовываем функцию add_everything_up, которая будет складывать числа(int, float) и строки(str)

Описание функции:
add_everything_up(a, b) принимает a и b, которые могут быть как числами(int, float), так и строками(str).
TypeError - когда a и b окажутся разными типами (числом и строкой), то возвращать строковое представление этих двух
данных вместе (в том же порядке). Во всех остальных случаях выполнять стандартные действия.
"""

def add_everything_up(a, b):
    try:
        return round(a + b, 3)
    except TypeError:
        return str(a) + str(b)

# Пример кода:
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))