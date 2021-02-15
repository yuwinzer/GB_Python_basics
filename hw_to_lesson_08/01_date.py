# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной
# структуры на реальных данных.

class Date:

    @classmethod
    def date_to_int(cls, date_str):
        return int(date_str.replace('-', ''))

    @staticmethod
    def date_check(date_str):
        numbers = date_str.split("-")
        print(f"{numbers = }")
        if not (13 > int(numbers[0]) > 0):
            print("число введено неправильно")
        elif not (13 > int(numbers[1]) > 0):
            print("месяц введен неправильно")
        elif not (9999 > int(numbers[2]) > 0):
            print("год введен неправильно")
        else:
            print(f"Формат даты введен правильно")


date_1 = "07-05-1997"
print(Date.date_to_int(date_1))

Date.date_check(date_1)
