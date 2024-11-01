calls = 0
# Создаём функцию count_calls и изменять в ней значение переменной calls.
def count_calls ():
    global calls
    calls+=1
# Создаём функцию string_info с параметром string
def string_info (string):
    count_calls()
    return (len(string), string.upper(), string.lower())
# Создаём функцию is_contains с двумя параметрами string и list_to_search
def is_contains (string, list_to_search):
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]
# Вывод результата
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)