# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

from statistics import mean

surname = []
salary = []
with open("data/input_for_03.txt") as f:
    while True:
        line = f.readline()
        if not line:
            break
        else:
            line = line.split()
            surname.append(line[0])
            salary.append(line[1])

sal_dict = dict(zip(surname, salary))

print("Список сотрудников с зарплатой менее 20000:")
for key, val in sal_dict.items():
    if int(val) < 20000:
        print(key)

print(f"Среднее значение зарплат: {mean(int(n) if n else 0 for n in salary)}")

