# 1. Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()  # Вызов функции без аргументов
print_params(3, 'urban', False) # Вызов функции с тремя аргументами
print_params(364, 'module')    # Вызов функции с двумя аргументами + 1 по умолчанию
print_params(b = 'control') # Вызов функции с одним аргументом + 2 по умолчанию
print_params(b = 31)    # Вызов функции с одним аргументом + 2 по умолчанию
print_params(c = [1, 2, 3])     # Вызов функции с одним аргументом список + 2 по умолчанию

# 2. Распаковка параметров:
values_list = [1, 'строка', True]
values_dict = {'a': 12, 'b': 'Hello', 'c': False}
print_params(*values_list)
print_params(**values_dict)
# Одновременно передать values_list и values_dict в функцию print_params невозможно,
# не изменив количество элементов.

# 3. Распаковка + отдельные параметры:
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)    #работает
