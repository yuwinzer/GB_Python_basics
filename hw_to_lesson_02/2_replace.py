count = int(input("Сколько чисел вы хотите ввести? \n"))
input_list = []

if count > 1:
    for i in range (1, count + 1):
        item = int(input(f"Введите {i}-е число из {count}: "))
        input_list.append(item)
    print(f"Вы ввели следующий список: \n{input_list}")
else:
    print("Нечего переставлять, в таком случае список чисел будет создан автоматически:")
    input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print(input_list)

for i in range (1, len(input_list), 2):
    input_list[i-1], input_list[i] = input_list[i], input_list[i-1]

print(f"После перестановки был получен следующий список: \n{input_list}")