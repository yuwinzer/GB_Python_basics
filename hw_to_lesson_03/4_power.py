# 4. Программа принимает действительное положительное число x
# и целое отрицательное число y. Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func_1(x, y):
    """Возведение в степень через **"""
    return x ** y


def my_func_2(x, y):
    """Возведение в степень без **"""
    result = x
    if y < 0:
        for i in range(1, abs(y)):
            result *= x
        return 1 / result  # 1 / на result, т.к. степень отрицательная
    else:
        return 'Invalid value detected!'


arg_x = float(input(f'Введите действительное положительное число x: '))
arg_y = int(input(f'Введите целое отрицательное число y: '))
print(my_func_1(arg_x, arg_y))
print(my_func_2(arg_x, arg_y))