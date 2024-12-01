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


#  7. Создаем объект класса House с названием и количеством этажей из примера.
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

#  Выводим на консоль строки
# __str__
print(h1)
print(h2)

#  Выводим на консоль кол-ва этажей зданий
# __len__
print(len(h1))
print(len(h2))