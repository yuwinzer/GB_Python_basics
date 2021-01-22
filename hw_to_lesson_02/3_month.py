month = int(input("Введите номер месяца от 1 до 12 \n"))
quarter_list = ['зима', 'весна', 'лето', 'осень']
quarter_dict = {1: 'зима',
                2: 'зима',
                3: 'весна',
                4: 'весна',
                5: 'весна',
                6: 'лето',
                7: 'лето',
                8: 'лето',
                9: 'осень',
                10: 'осень',
                11: 'осень',
                12: 'зима'}

print("\nреализация через список:")
if month == 1 or month == 2 or month == 12:
    print(f"{month} относится к зиме")
elif month == 3 or month == 4 or month == 5:
    print(f"{month} относится к весне")
elif month == 6 or month == 7 or month == 8:
    print(f"{month} относится к лету")
else:
    print(f"{month} относится к осени")

print("\nреализация через словарь:")
print(f"{month}-й месяц относится к времени года: {quarter_dict[month]}")