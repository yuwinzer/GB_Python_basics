from functools import reduce
# Task попробовать заменить на лямбда функцию my_f
# Task попробовать сделать рекурсивный вызов

# решение с лямбда функкцией
random_str = ['a', 'b', 'c', 'b', 'd']
print(reduce(lambda symbol_1, symbol_2: symbol_1 + symbol_2, random_str))


# рекурсивная функция
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


user_inp = int(input("Введите значение числа, факториал которого требуется вычислить: "))
print(factorial(user_inp))
