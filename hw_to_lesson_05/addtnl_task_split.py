import re

f = open("data/for_lesson_5.txt", "a")
data_for_file = ['Milk\n', 'Bread\n', 'Sugar\n', 'Salad']
f.writelines(data_for_file)
f.close()

with open("data/for_lesson_5.txt", 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        else:
            res_list = re.findall('[A-Z][^A-Z]*', line)
            for elem in res_list:
                print(elem.rstrip())  # rstrip убирает перевод на новую строку



