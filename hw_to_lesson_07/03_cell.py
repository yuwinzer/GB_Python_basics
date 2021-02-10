# Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться только
# к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.
#
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно
# равняться сумме ячеек исходных двух клеток.
#
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
# больше нуля, иначе выводить соответствующее сообщение.
#
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества
# ячеек этих двух клеток.
#
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
# количества ячеек этих двух клеток.
#
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
#
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
#
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
# *****\n*****\n**. Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.

class ZeroCellule(ValueError):
    def __init__(self, message):
        self.message = f'{message}. Please choose sells with different numbers of cellules'
        super().__init__(self.message)


class Cell:
    cellule_n = int

    def __init__(self, cellule_n):
        self.cellule_n = cellule_n

    def __add__(self, other):
        """
        содержимое второй клетки в результате процесса обнуляется
        """
        self.cellule_n += other.cellule_n
        other.cellule_n = 0  # ячейки второй клетки поглощены

    def __sub__(self, other):
        """
        содержимое второй клетки в результате процесса обнуляется
        """
        if abs(self.cellule_n - other.cellule_n) == 0:
            raise ZeroCellule('Zero cellules remain')
        if self.cellule_n >= other.cellule_n:
            self.cellule_n -= other.cellule_n
            other.cellule_n = 0  # ячейки второй клетки поглощены
        else:
            other.cellule_n -= self.cellule_n
            self.cellule_n = other.cellule_n
            other.cellule_n = 0  # ячейки второй клетки поглощены

    def __mul__(self, other):
        """
        содержимое второй клетки в результате процесса обнуляется
        """
        self.cellule_n *= other.cellule_n
        other.cellule_n = 0  # ячейки второй клетки поглощены

    def __truediv__(self, other):
        """
        содержимое второй клетки в результате процесса обнуляется
        """
        self.cellule_n //= other.cellule_n
        other.cellule_n = 0  # ячейки второй клетки поглощены

    def make_order(self, order_n):
        self.order_n = order_n
        repeat_ord_n = self.cellule_n // order_n
        symbols = "*" * order_n + "\n"
        last_symbols = self.cellule_n % order_n * "*"
        str_symbols = [symbols * repeat_ord_n, last_symbols] # наполняем список звездочками
        str_out = ''.join(str_symbols)  # преобразуем список в строку
        print(f"{str_out}")
        # print(f"{symbols * repeat_ord_n}")
        # print(f"{last_symbols}")

    def __str__(self):
        return f"{self.cellule_n}"


# тестирование:
cell_1 = Cell(5)
cell_2 = Cell(3)
print('\ninitial:')
print(f"{str(cell_1) =}")
print(f"{str(cell_2) =}")

cell_1 + cell_2  # первая клетка поглощает все ячейки второй
print('\nadd:')
print(f"{str(cell_1) =}")
print(f"{str(cell_2) =}")

cell_1.cellule_n = 5  # хилим первую клетку
cell_2.cellule_n = 3  # хилим вторую клетку
cell_1 - cell_2  # в первой клетке остается разница ячеек
print('\nsub:')
print(f"{str(cell_1) =}")
print(f"{str(cell_2) =}")

cell_1.cellule_n = 5  # хилим первую клетку
cell_2.cellule_n = 3  # хилим вторую клетку
cell_1 * cell_2  # в первой клетке остаются мутированные ячейки
print('\nmul:')
print(f"{str(cell_1) =}")
print(f"{str(cell_2) =}")

cell_1.cellule_n = 5  # хилим первую клетку
cell_2.cellule_n = 3  # хилим вторую клетку
cell_1 / cell_2  # в первой клетке остаются мутированные ячейки
print('\ntruediv:')
print(f"{str(cell_1) =}")
print(f"{str(cell_2) =}")

cell_1.cellule_n = 14  # хилим первую клетку

# print(f'\n{cell_1.order_n = }')
print('\nmake_order:')
cell_1.make_order(4)
print(f'{cell_1.cellule_n = }')
print(f'{cell_1.order_n = }')
