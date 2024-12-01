#  1. Создаем класс House.
class House:
    #  2. Внутри класса House определяем метод __init__, в который передаем название и кол-во этажей.
    def __init__(self, name, number_of_floors):
        #  3. Внутри метода __init__ создаем атрибуты объекта self.name и self.number_of_floors,
        #  присваиваем им переданные значения.
        self.name = name
        self.number_of_floors = number_of_floors

    #  4. Создаем метод go_to с параметром new_floor и записываем логику внутри него на основе описания задачи 5_1.
    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

    # 5. Дополняем класс House методом возврата кол-ва этажей здания self.number_of_floors
    def __len__(self):
        return self.number_of_floors

    # 6. Дополняем класс House методом возврата строки: # "Название: <название>, кол-во этажей: <этажи>"
    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'

    # 7. Дополняем класс House следующими специальными методами:
    # 7.1 Методом сравнения на равенства: возвращаем True, если количество этажей self == other
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            return False

    # 7.2 Методом сравнения "меньше чем" (Lower than) __lt__(<)
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            return NotImplemented

    # 7.3 Методом сравнения "меньше или равно" __le__(<=)
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            return NotImplemented

    # 7.4 Методом сравнения "больше чем" (Greater than) __gt__(>)
    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            return NotImplemented

    # 7.5 Методом сравнения "больше или равно" __ge__(>=)
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            return NotImplemented

    # 7.5 Методом сравнения на неравенство __ne__(!=)
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            return NotImplemented

    # 7.6 Методом добавления элемента в множество __add__
    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)
        elif isinstance(value, House):
            return House(self.name, self.number_of_floors + value.number_of_floors)
        else:
            return NotImplemented

    # 7.7 Методом симметричного сложения __radd__
    def __radd__(self, value):
        return self.__add__(value)

    # 7.8 Методом сложения с присваиванием += __iadd__
    def __iadd__(self, value):
        return self.__add__(value)



#  8. Создаем объект класса House с названием и количеством этажей из примера.
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# Вывод на консоль:
print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__