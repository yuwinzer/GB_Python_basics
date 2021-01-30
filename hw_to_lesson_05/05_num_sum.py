# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random
out_filename = "data/output_from_05.txt"

r_num = []
for i in range(10):
    r_num.append(random.randrange(100))
print(f"Сгенерированные числа: {r_num}")
r_num_str= (" ".join([str(elem) for elem in r_num]))
with open(out_filename, "w") as f:
    f.write(r_num_str)  # пробелы между словами, но не в конце строки

with open(out_filename) as f:
    nums = f.readline()

nums = nums.split(' ')
nums = (int(num) for num in nums)
print(sum(nums))