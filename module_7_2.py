"""
Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name - название файла для записи,
strings - список строк для записи.
Функция должна:
1. Записывать в файл file_name все строки из списка strings, каждая на новой строке.
2. Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>), а значением
- записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.
"""
def custom_write(file_name, strings):
    dict_srtings = {}
    strings_positions = 0
    file = open(file_name, 'a', encoding='utf-8')
    for string in strings:
        strings_positions += 1
        cursor = file.tell()
        dict_srtings[(strings_positions, cursor)] = string
        file.write(string + '\n')
    file.close()
    return dict_srtings

"""
Пример полученного словаря:
{(1, 0): 'Text for tell.', (2, 16): 'Используйте кодировку utf-8.'}
Где:
1, 2 - номера записанных строк.
0, 16 - номера байт, на которых началась запись строк.
'Text for tell.', 'Используйте кодировку utf-8.' - сами строки.
"""

# Пример выполняемого кода:

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)