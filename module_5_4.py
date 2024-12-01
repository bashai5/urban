# Задача "История строительства":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов" module_5_3.py.
# 1. Создаем класс House.
class House:
    # В классе House создаем атрибут houses_history = [], который будет хранить названия созданных объектов.
    houses_history = []

    # Дополняем метод __new__ так, чтобы:
    # 1. Название объекта добавлялось в список cls.houses_history.
    # 2. Название строения можно взять из args по индексу.
    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    # Переопределяем метод __del__(self) в котором будет выводиться строка:
    # "<название> снесён, но он останется в истории"
    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории ')

# Вывод результатов:
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)