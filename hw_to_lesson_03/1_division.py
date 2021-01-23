# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def div_calc(int1, int2):
    """Делит 2 числа

    Второе число не должно быть равно нулю
    """
    try:
        div = round(int1 / int2, 2)
    except ZeroDivisionError:
        return "Нельзя делить на ноль! Попробуйте еще."
    return div


num_1 = int(input(f"Введите первое число: \n"))
num_2 = int(input(f"Введите первое число: \n"))

print(div_calc(num_1, num_2))
