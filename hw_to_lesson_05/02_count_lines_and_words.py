# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

# inp_name = input("Введите название файла вместе с расширением: \n")
inp_name = "data/input_for_02.txt"

try:
    with open(inp_name) as f:
        count = 0
        while True:
            line = f.readline()
            if not line:
                break
            else:
                line = line.split()
                count += 1
                print(f"В строке {count} слов: {len(line)}")

        print(f"Всего было строк: {count}")
except:
    print("Не удалось открыть файл")
