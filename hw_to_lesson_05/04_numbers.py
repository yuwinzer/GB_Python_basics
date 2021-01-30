# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
# в новый текстовый файл.

eng_w = []
numbers = []
with open("data/input_for_04.txt") as f:
    while True:
        line = f.readline()
        if not line:
            break
        else:
            line = line.split()
            eng_w.append(line[0])
            numbers.append(line[2])

eng_nums = dict(zip(eng_w, numbers))  # собираем словарь из двух списков
eng_rus = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}  # перевод англ на рус

rus_nums = {value: eng_nums.get(key) for key, value in eng_rus.items()} #  из eng_rus ,берет key и value
                                                                        # собирает в rus_nums словарь в виде:
                                                                        # "value из eng_rus": "value из eng_nums"

with open("data/output_from_04.txt", 'w') as f:
    for k, v in rus_nums.items():
        f.write(f"{str(k)} - {str(v)} \n")
