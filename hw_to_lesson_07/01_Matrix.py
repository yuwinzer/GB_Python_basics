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
        matrix_p = ""
        for i in range(len(self.body)):
            matrix_temp = '\t'.join(str(j) for j in self.body[i])
            matrix_p += matrix_temp + "\n"
        return f'{matrix_p}'

    def __add__(self, other_matrix):
        """
        в результате сложения двух матриц, вторая обнуляется!
        """
        new_matrix = []
        for i in range(len(self.body)):
            new_line = []
            for j in range(len(self.body[i])):
                new_line.append(self.body[i][j] + other_matrix.body[i][j])
            new_matrix.append(new_line)
        return Matrix(new_matrix)

print("first matrix:")
matr_a = Matrix([[10, 20, 30], [40, 50, 60]])
print(matr_a)

print("second matrix:")
matr_b = Matrix([[100, 200, 300], [400, 500, 600]])
print(matr_b)

print("result of a sum:")
matr_c = matr_a + matr_b
print(matr_c)
