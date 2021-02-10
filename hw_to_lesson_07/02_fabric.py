# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    v = 0

    @property
    def consumption(self):
        return round(self.v / 6.5 + 0.5, 2)

    def __add__(self, other):
        new_c = self.consumption + other.consumption
        return new_c


class Costume(Clothes):
    h = 0

    @property
    def consumption(self):
        return round(2 * self.h + 0.3, 2)

    def __add__(self, other):
        new_c = self.consumption + other.consumption
        return new_c


new_coat = Coat('Пальто')
new_coat.v = 50
print(new_coat.consumption)

new_costume = Costume("Смокинг")
new_costume.h = 180
print(new_costume.consumption)

overal_consumption = new_coat + new_costume


def beautiful(func):
    def some_func():
        print('\n-----------------------------')
        func()
        print('-----------------------------')

    return some_func


@beautiful
def print_results():
    print(f"{overal_consumption = }")


print_results()
