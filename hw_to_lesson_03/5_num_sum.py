# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме
# и после этого завершить программу.


def num_sum(string):
    '''Функция суммирует все числа до стоп-слова

    Стоп-слово quit
    На входе принимается строка с числами.
    Внимание! Имеется глобальная переменная no_exit
    '''
    global no_exit
    elements = string.split()  # разбиваем строку на элементы
    num_to_sum = 0
    for i in range(0, len(elements)):
        if elements[i].lstrip('-').isdigit():  # перед проверкой убирает минус, если он есть слева
            num_to_sum += int(elements[i])

        elif (elements[i]).lower() == "quit":
            no_exit = False
            break
    return num_to_sum


no_exit = True
result = 0
while no_exit:
    user_inp = input("Введите числа через пробел, которые хотите суммировать. \n"
                     "Напишите quit чтобы прекратить программу \n"
                     ":")
    result += num_sum(user_inp)
    print(result)

