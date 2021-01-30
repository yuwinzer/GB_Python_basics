# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json
from statistics import mean

names = []  # список имен фирм
profits = []  # список прибылей и убытков фирм
ave_prof = [] # список только прибылей
with open("input_for_07.txt") as f:
    while True:
        line = f.readline()
        if not line:
            break
        else:
            line = line.split()
            profit = int(line[2]) - int(line[3])
            if profit >= 0:
                ave_prof.append(profit)
            names.append(line[0])
            profits.append(profit)

average_profit = round(mean(ave_prof))

dict_prof = dict(zip(names, profits))
dict_ave = {"average_profit": average_profit}

res_list = [dict_prof, dict_ave]
print(res_list)

with open('output_from_07.json', 'w') as f:
    json.dump(res_list, f)
