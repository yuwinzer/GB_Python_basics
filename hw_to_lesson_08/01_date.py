# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной
# структуры на реальных данных.

class Date:

    @classmethod
    def date_to_int(cls, date_str):
        return list(map(int, date_str.split('-')))

    @staticmethod
    def date_check(date_str):
        ddmmyy = list(map(int, Date.date_to_int(date_str)))
        big_months = [1, 3, 5, 7, 8, 10, 12]
        is_leap = 1 if ddmmyy[2] % 400 == 0 or (ddmmyy[2] % 4 == 0 and ddmmyy[2] % 100 != 0) else 0
        if 0 <= int(ddmmyy[2]) <= 9999 and 1 <= int(ddmmyy[1]) <= 12:
            if 1 <= int(ddmmyy[0]) <= (28 and is_leap if ddmmyy[1] == 2 else 31 if ddmmyy[1] in big_months else 30):
                print(f"Дата {date_str} введена верно")
            else:
                print(f"Дата {date_str} введена неверно")
        else:
            print(f"Дата {date_str} введена неверно")

date_1 = "07-05-1997"
Date.date_check(date_1)

date_1 = "29-02-2020"
Date.date_check(date_1)

date_1 = "29-02-2021"
Date.date_check(date_1)

date_1 = "20-02-19999"
Date.date_check(date_1)

date_1 = "99-02-2021"
Date.date_check(date_1)