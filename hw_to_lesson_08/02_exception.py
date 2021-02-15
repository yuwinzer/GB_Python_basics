# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class ZeroDivision(Exception):

    def __init__(self, message):
        self.message = f'{message}'


class Check:

    @staticmethod
    def delete(one, other):
        print(f'{one = }')
        print(f'{other = }')
        if other == 0:
            raise ZeroDivision('Нельзя делить на ноль')
        return one / other


a, b = 5, 0

print(Check.delete(a, b))
