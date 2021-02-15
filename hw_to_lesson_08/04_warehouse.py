# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
# и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
#
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

from datetime import datetime
import random
import warnings


class Warehouse:
    DB_list = {}
    myName = "Склад оргтехники"

    def __init__(self, name):
        self.name = name

    def add_printer(self, equip_attr):
        print(f"Добавлен принтер {equip_attr} в {self.name} на {self.myName}")
        equip_attr.append(self.name)
        self.DB_list[equip_attr[0]] = equip_attr[1:]

    def add_scaner(self, equip_attr):
        print(f"Добавлен сканер {equip_attr} в {self.name} на {self.myName}")
        equip_attr.append(self.name)
        self.DB_list[equip_attr[0]] = equip_attr[1:]

    def add_copier(self, equip_attr):
        print(f"Добавлен ксерокс {equip_attr} в {self.name} на {self.myName}")
        equip_attr.append(self.name)
        self.DB_list[equip_attr[0]] = equip_attr[1:]

    def __str__(self):
        str_a = ""
        for key, value in self.DB_list.items():
            str_a.join(f"{key, ' : ', value} \n")
        return str_a

    def update(self, db_another):
        db_another.update(self.DB_list)
        return db_another


class Floor1(Warehouse):
    myName = "1 этаж склада оргтехники"


class Floor2(Warehouse):
    myName = "2 этаж склада оргтехники"


class OfficeEquip:
    office_eq_list = []

    @staticmethod
    def rand_id():

        # datetime object containing current date and time
        now = datetime.now()
        rand_num = random.sample(range(9), 5)
        rand_num_str = "".join([str(elem) for elem in rand_num])
        dt_string = now.strftime("%d%m%Y%H%M%S") + rand_num_str
        return dt_string

    def __init__(self, name, volume, quantity):
        self.id = OfficeEquip.rand_id()
        self.name = name
        self.volume = volume
        self.quantity = quantity

    def __str__(self):
        return f"{self.id, self.name, self.volume, self.quantity}"

    def list(self):
        return [self.id, self.name, self.volume, self.quantity]


class Printer(OfficeEquip):
    pass


class Scanner(OfficeEquip):
    pass


class Copier(OfficeEquip):
    pass


class Check:

    @staticmethod
    def numbs(arg):
        if not arg.isnumeric():
            warnings.simplefilter('always', UserWarning)  # warning call always, not once
            warnings.warn(f'{arg} не является числом')
            return False
        else:
            return True


printer_1 = Printer("Canon MXL50", 1, 3)
print(printer_1.list())

floor_1 = Floor1("Отделение_1")
floor_1.add_printer(printer_1.list())
print(floor_1.DB_list)


while True:
    i = input("Выберите что добавить в первое подразделение:\n"
              "1 - принтер, 2 - сканер, 3 - ксерокс, \n"
              "либо введите 0, чтобы завершить программу\n")

    if Check.numbs(i):
        i = int(i)
        if i == 0:
            print(f"Программа завершена, были получены данные")
            print(Warehouse.DB_list)
            break

        if i == 1:
            eq_tmp = input(f"Введите данные для принтера через пробел: \n"
                           f"название модели, объем упаковки, количество:\n")
            eq_tmp_list = eq_tmp.split(" ")
            if Check.numbs(eq_tmp_list[1]) and Check.numbs(eq_tmp_list[2]):
                temp_obj = Printer(eq_tmp_list[0], eq_tmp_list[1], eq_tmp_list[2])
                floor_1.add_printer(temp_obj.list())
            else:
                print("Объем и количество должны быть числами, попробуйте заново")

        elif i == 2:
            eq_tmp = input(f"Введите данные для сканера через пробел: \n"
                           f"название модели, объем упаковки, количество:\n")
            eq_tmp_list = eq_tmp.split(" ")
            if Check.numbs(eq_tmp_list[1]) and Check.numbs(eq_tmp_list[2]):
                temp_obj = Printer(eq_tmp_list[0], eq_tmp_list[1], eq_tmp_list[2])
                floor_1.add_scaner(eq_tmp_list)
            else:
                print("Объем и количество должны быть числами, попробуйте заново")

        elif i == 3:
            eq_tmp = input(f"Введите данные для ксерокса через пробел: \n"
                           f"название модели, объем упаковки, количество:\n")
            eq_tmp_list = eq_tmp.split(" ")
            if Check.numbs(eq_tmp_list[1]) and Check.numbs(eq_tmp_list[2]):
                temp_obj = Printer(eq_tmp_list[0], eq_tmp_list[1], eq_tmp_list[2])
                floor_1.add_copier(eq_tmp_list)
            else:
                print("Объем и количество должны быть числами, попробуйте заново")

        else:
            print(f"Введенное число должно быть от 0 до 3 включительно")
    else:
        print("Вы должны ввести число, попробуйте еще")
