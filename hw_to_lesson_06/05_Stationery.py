# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

class Stationery:

    def draw(self):
        print('Запуск отрисовки')

    def __init__(self, title):
        self.title = title


class Pen(Stationery):
    myName = __qualname__

    def draw(self):
        print(f'Запуск отрисовки {self.myName} {self.title}, средняя линия')


class Pencil(Stationery):
    myName = __qualname__

    def draw(self):
        print(f'Запуск отрисовки {self.myName} {self.title}, тонкая линия')


class Handle(Stationery):
    myName = __qualname__

    def draw(self):
        print(f'Запуск отрисовки {self.myName} {self.title}, толстая линия')


item_1 = Pen("Pilot")
item_1.draw()

item_2 = Pencil("Конструктор")
item_2.draw()

item_3 = Handle("Stels")
item_3.draw()