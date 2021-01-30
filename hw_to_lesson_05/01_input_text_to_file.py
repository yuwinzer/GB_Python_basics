# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

import time

file_name = time.strftime("data/output_from_01_%Y%m%d-%H%M%S.txt")
print(f"Был создан файл {file_name}")

inp_line = "0"

try:
    f = open(file_name, "w")
    while inp_line != "":
        inp_line = (input("Введите строку для записи в файл, либо просто Enter для закрытия файла:\n"))
        f.writelines(f"{inp_line}\n")
except:
    print("Что-то пошло не так")
finally:
    f.close()
    print(f"Файл {file_name} закрыт")
