"""
Атрибуты класса Figure: sides_count = 0
Каждый объект класса Figure должен обладать следующими атрибутами:
Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
Атрибуты(публичные): filled(закрашенный, bool)
"""

class Figure:
    __sides = []
    __color = []
    filled = True

    def __init__(self, rgb, * side): # устанавливаем начальные значения атрибутов класса: цвета и стороны
        self.color = list(rgb) # присваиваем значению атрибута self.color список list(rgb)
        self.side = side[0] # присваиваем значению атрибута self.side первое значение списка side
        self.filled = True # присваиваем значению атрибута filled True - закрашено

    """
    Метод get_color, возвращает список RGB цветов.
    """
    def get_color(self):
        self.__color = self.color
        self.filled = True
        return self.__color

    """
    Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных
    значений перед установкой нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне
    от 0 до 255 (включительно).
    """
    def __is_valid_color(self, r, g, b):
        self.r, self.g, self.b = r, g, b
        if 0 <= self.r <= 255 and 0<= self.g <= 255 and 0 <= self.b <= 255:
            return True
        else:
            return False

    """
    Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения,
    предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
    """
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.color = [self.r, self.g, self.b]

    """
    Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все
    стороны целые положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
    """
    def __is_valid_sides(self, *args):
        for side in self.sides:
            if len(self.sides) == self.sides_count and side > 0 and type(side) == int:
                return  True
            else:
                return  False
    """
    Метод get_sides должен возвращать значение я атрибута __sides.
    """
    def set_sides(self, *args):
        massive_lst = []
        self.sides = list(args)
        if self.__is_valid_sides(self, *args):
            self.get_sides()
        else:
            for i in range(self.sides_count):
                massive_lst.append(self.side)
            self.sides = massive_lst
            self.get_sides()

    """
    Метод __len__ должен возвращать периметр фигуры.
    """
    def __len__(self):
        return sum(self.__sides)

    """
    Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count,
    то не изменять, в противном случае - менять.
    """
    def get_sides(self):
        self.__sides = self.sides
        return self.__sides

"""
Атрибуты класса Circle: sides_count = 1
Каждый объект класса Circle должен обладать следующими атрибутами и методами:

Все атрибуты и методы класса Figure
"""
class Circle(Figure):
    sides_count = 1
    __radius = None

    """
    Аттрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
    """
    def set_radius(self):
        self.__radius = self.__len__() / (2 * 141569)
        return self.__radius

    """
    Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
    """
    def get_square(self):
        self.set_radius()
        return (self.__radius ** 2) * 3.141569 # через радиус
        # return ((self.side)**2)/(4 * 3.141569) # через длину окружности

"""
Атрибуты класса Triangle: sides_count = 3
Каждый объект класса Triangle должен обладать следующими атрибутами и методами:

Все атрибуты и методы класса Figure
"""
class Triangle(Figure):
    sides_count = 3
    __height = None

    """
    Метод get_square возвращает площадь треугольника. (можно рассчитать по формуле Герона)
    """
    def get_square(self):
        return (self.side ** 2) * (3 ** 0.5) / 4

    def set_height(self):
        self.__height = self.side * (3 ** 0.5) / 2
        return self.__height

"""
Атрибуты класса Cube: sides_count = 12
Каждый объект класса Cube должен обладать следующими атрибутами и методами:

Все атрибуты и методы класса Figure.
"""

class Cube(Figure):
    sides_count = 12

    """
    Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
    """
    def set_side_lst(self):
        set_side_lst = []
        for element in range(self.sides_count):
            set_side_lst.append(self.side)
        self.__sides = set_side_lst
        return self.__sides

    """
    Метод get_volume, возвращает объём куба.
    """
    def get_volume(self):
        return self.side ** 3

# Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())