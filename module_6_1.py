# Создаем 2 класса родителя: Animal, Plant
# Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный),
# name - индивидуальное название каждого животного.
class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

# Метод eat должен работать следующим образом:
    def eat(self, food):
        # Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>",
        # меняется атрибут fed на True.
        if food.edible == True:
            Animal.fed = True
            print(f'{self.name} съел {food.name}')

        # Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>",
        # меняется атрибут alive на False.
        else:
            Animal.alive = False
            print(f'{self.name} не стал есть {food.name}')


# Для класса Plant атрибут edible = False(съедобность), name - индивидуальное название каждого растения
class Plant:
    edible = False

    def __init__(self, name):
        self.name = name

# Создаем 4 класса наследника:
# Mammal, Predator для Animal
class Mammal(Animal):
    pass

class Predator(Animal):
    pass

# Flower, Fruit для Plant
class Flower(Plant):
    edible = False

# У каждого объекта Fruit должен быть атрибут edible = True (переопределить при наследовании)
class Fruit(Plant):
    edible = True

# Вывод на консоль:
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)