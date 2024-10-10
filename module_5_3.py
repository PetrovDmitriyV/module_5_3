class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        if type(number_of_floors) != int:
            print('Ошибка ввода данных')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        isinstance(other, House)
        return self.number_of_floors == other.number_of_floors  # True если равенство этажей

    def __lt__(self, other):
        isinstance(other, House)
        return self.number_of_floors < other.number_of_floors  # True если этажей меньше с чем сравниваем

    def __gt__(self, other):
        isinstance(other, House)
        return self.number_of_floors > other.number_of_floors  # True если этажей больше с чем сравниваем

    def __le__(self, other):
        isinstance(other, House)
        return self.number_of_floors <= other.number_of_floors  # True если этажей меньше или равно с чем сравниваем

    def __ge__(self, other):
        isinstance(other, House)
        return self.number_of_floors >= other.number_of_floors  # True если этажей меньше или равно с чем сравниваем

    def __ne__(self, other):
        isinstance(other, House)
        return self.number_of_floors != other.number_of_floors  # True если этажей не равно с чем сравниваем

    def __add__(self, value):
        isinstance(value, int)
        self.number_of_floors = self.number_of_floors + value  # Увеличиваем этажи на value число
        return self

    def __iadd__(self, value):
        isinstance(value, int)
        self.number_of_floors += value  # Увеличиваем этажи на value число
        return self

    def __radd__(self, value):
        isinstance(value, int)
        self.number_of_floors = value + self.number_of_floors  # Увеличиваем этажи на value число
        return self


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)
print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__  10 + 10
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__     20 + 10
print(h1)

h2 = 10 + h2  # __radd__ 10 + 20
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
