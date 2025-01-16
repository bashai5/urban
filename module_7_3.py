"""
Домашнее задание по теме "Оператор "with".
Задача "Найдёт везде":

Создаем класс WordsFinder с объектами:
WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
Объект этого класса должен принимать при создании неограниченного количество названий файлов и записывать их
в атрибут file_names в виде списка или кортежа.

Также объект класса WordsFinder должен обладать следующими методами:
get_all_words - подготовительный метод, который возвращает словарь следующего вида:
{'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
Где:
    1. 'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
    2. ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.

Алгоритм получения словаря такого вида в методе get_all_words:
    1. Создаем пустой словарь all_words.
    2. Перебераем названия файлов и открываем каждый из них, используя оператор with.
    3. Для каждого файла считываем единые строки, переводя их в нижний регистр (метод lower()).
    4. Избавляемся от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке. (тире обособлено пробелами,
    это не дефис в слове).
    5. Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
    6. В словарь all_words записываем полученные данные, ключ - название файла, значение - список из слов этого файла.

find(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение
- позиция первого такого слова в списке слов этого файла.
count(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение
- количество слова word в списке слов этого файла.
В методах find и count пользуйтесь ранее написанным методом get_all_words для получения названия файла
и списка его слов.
Для удобного перебора одновременно ключа(названия) и значения(списка слов) можно воспользоваться методом словаря
- item().

for name, words in get_all_words().items():
    # Логика методов find или count
"""
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = file.read().lower()
                for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    words = words.replace(punct, '')
                all_words[file_name] = words.split()
        return all_words

    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        word_position = {}
        for file_name, words in all_words.items():
            if word in words:
                word_position[file_name] = words.index(word) + 1
        return word_position

    def count (self, word):
        word = word.lower()
        all_words = self.get_all_words()
        word_counts = {}
        for file_name, words in all_words.items():
            word_counts[file_name] = words.count(word)
        return word_counts

# Поисковое слово: 'TEXT'
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

print()
# Поисковое слово: 'child'
finder3 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder3.get_all_words())
print(finder3.find('Child'))
print(finder3.count('Child'))

print()
# Поисковое слово: 'if'
finder4 = WordsFinder('Rudyard Kipling - If.txt',)
print(finder4.get_all_words())
print(finder4.find('if'))
print(finder4.count('if'))

print()
# Поисковое слово: 'captain'
finder5 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder5.get_all_words())
print(finder5.find('captain'))
print(finder5.count('captain'))