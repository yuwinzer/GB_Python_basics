revenue = int(input("Введите прибыль вашей фирмы за произвольный промежуток времени: "))
costs = int(input("Введите издержки вашей фирмы за тот же промежуток времени: "))
print(f"Вы ввели прибыль: {revenue} и расходы: {costs}")
if revenue > costs:
    print(f"Прибыль вашей фирмы составляет {revenue - costs}!")
    employees_num = int(input("Введите число сотрудников в вашей фирме: "))
    print(f"На каждого сотрудника прибыль составляет: {int((revenue - costs)/employees_num)}")
elif revenue < costs:
    print(f"Ваша фирма работает в убыток")
else:
    print(f'Ваш бизнес работает в "ноль"')
