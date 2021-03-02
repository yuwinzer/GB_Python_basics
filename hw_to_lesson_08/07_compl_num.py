# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и
# умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplNum:

    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def __str__(self):
        if self.b < 0:
            return f"({self.a} - {abs(self.b)}i)"
        else:
            return f"({self.a} + {self.b}i)"

    def __add__(self, other):
        a_num = self.a + other.a
        b_num = self.b + other.b
        return ComplNum(a_num, b_num)

    def __mul__(self, other):
        a_num = (self.a * other.a) - (self.b * other.b)
        b_num = (self.b * other.a) + (self.a * other.b)
        return ComplNum(a_num, b_num)

num_1 = ComplNum(-1, -5)
print(f"Первое число: {num_1}")

num_2 = ComplNum(1, 5)
print(f"Второе число: {num_2}")

num_3 = num_1 + num_2
print(f"Сложение: {num_3}")

num_4 = num_1 * num_2
print(f"Умножение: {num_4}")