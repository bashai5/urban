"""
Создаем класс Vehicle - это любой транспорт.
"""

class Vehicle:
    """
    I. Каждый объект Vehicle должен содержать следующие атрибуты объекта:
    1. Атрибут класса __COLOR_VARIANTS, в который записан список допустимых цветов для окрашивания.
    (Цвета написать свои)
    """

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    """
    I. Каждый объект Vehicle должен содержать следующие атрибуты объекта:
    1. Атрибут owner(str) - владелец транспорта. (владелец может меняться);
    2. Атрибут __model(str) - модель (марка) транспорта. (мы не можем менять название модели);
    3. Атрибут __engine_power(int) - мощность двигателя. # (мы не можем менять мощность двигателя самостоятельно);
    4. Атрибут __color(str) - название цвета. (мы не можем менять цвет автомобиля своими руками).
    """

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    """
    Каждый объект Vehicle должен содержать следующий методы:
    1. Метод get_model - возвращает строку: "Модель: <название модели транспорта>";
    2. Метод get_horsepower - возвращает строку: "Мощность двигателя: <мощность>";
    3. Метод get_color - возвращает строку: "Цвет: <цвет транспорта>";
    4. Метод print_info - распечатывает результаты методов (в том же порядке): get_model, get_horsepower, get_color;
    а так же владельца в конце в формате "Владелец: <имя>";
    5. Метод set_color - принимает аргумент new_color(str), меняет цвет __color на new_color, если он есть в списке
    __COLOR_VARIANTS, в противном случае выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>".
    
    Взаимосвязь методов и скрытых атрибутов:
    1. Методы get_model, get_horsepower, get_color находятся в одном классе с соответствующими им атрибутами:
    __model, __engine_power, __color. Поэтому атрибуты будут доступны для методов.
    2. Атрибут класса __COLOR_VARIANTS можно получить обращаясь к нему через объект(self).
    3. Проверка в __COLOR_VARIANTS происходит не учитывая регистр ('BLACK' ~ 'black').
    """

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

"""
Создаем класс Sedan(седан) - наследник класса Vehicle.
II. Класс Sedan наследуется от класса Vehicle, а так же содержит следующие атрибуты:
1. Атрибут __PASSENGERS_LIMIT = 5 (в седан может поместиться только 5 пассажиров).
"""

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Исходный код:
# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()