goods = []  # создаем заготовку списка товаров с характеристиками
i = 1  # инициализируем начало счетчика
while True:
    name = input("Введите название товара: ")
    price = input(f"Введите цену товара {name}: ")
    quantity = input(f"Введите количество товара {name}: ")
    unit = input(f"Введите единицу измерения количества товара {name}, например шт.: ")
    ask_continue = input("Продолжить ввод товара? Введите Нет, чтобы прервать наполнение:\n")
    d_keys = ['Название', 'Цена', 'Количество', 'Ед. Изм.']
    d_values = [name, price, quantity, unit]
    cur_dict = {d_keys[i]: d_values[i] for i in range(len(d_keys))}  # создаем словарь из двух списков
    print(f"Данные по текущему товару (cur_dict): {cur_dict}")
    goods.append((i, cur_dict))  # вставляем в список i-й номер товара и его характеристики
    i += 1
    if ask_continue == 'нет' or ask_continue == 'Нет':
        break

print(f"Вы ввели товары (goods): {goods}")

temp_keys = list(goods[0][1])  # извлекаем список ключей первого товара

analytics = dict.fromkeys(temp_keys)  # создаем словарь c ключами из первого товара и пустыми значениями

for i in range(0, len(goods[0][1])):
    temp_values = []  # обнуляем список
    for n in range(0, len(goods)):
        temp_values_cur_good = list(goods[n][1].values())  # получаем список всех values n-го товара
        for repeat in range(len(temp_values)):  # проверяем есть ли повторяющиеся значения в списке
            if temp_values_cur_good[i] == temp_values[repeat]:
                temp_values.pop()
        temp_values.append(temp_values_cur_good[i])  # постепенно наполняем список i-ми values из n-го товара
    analytics[temp_keys[i]] = temp_values  # присваиваем i-му ключу присваиваем список характеристик
print(f"Получен аналитический список (analytics): {analytics}")
