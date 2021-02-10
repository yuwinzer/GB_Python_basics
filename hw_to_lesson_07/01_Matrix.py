# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения
# двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    body = list

    def __init__(self, body):
        self.body = body

    def __str__(self):
        """
        не требуется print для вывода списка списков в виде матрицы
        """
        def matrix_beauty(something):
            for i in range(len(something)):
                for j in range(len(something[i])):
                    print(f"{something[i][j]}", end="\t")
                print()
            print()
        return f"{matrix_beauty(self.body)}"

    def __add__(self, other_matrix):
        """
        в результате сложения двух матриц, вторая обнуляется!
        """
        for i in range(len(self.body)):
            for j in range(len(self.body[i])):
                self.body[i][j] += other_matrix[i][j]
                other_matrix[i][j] = 0  # обнуляем вторую матрицу


list_a = [[10, 20, 30], [40, 50, 60]]
list_b = [[100, 200, 300], [400, 500, 600]]
print(f"{len(list_a) = }")
print(f"{len(list_a[0]) = }")

new_matrix = Matrix(list_a)
print("first matrix:")
str(new_matrix)

print("second matrix:")
str(Matrix(list_b))

print("result of a sum:")
new_matrix + list_b
str(new_matrix)
