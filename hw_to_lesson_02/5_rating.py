my_list = [7, 5, 3, 3, 2]
print(my_list)
while True:
    num = input("Введите новое число, либо No если не хотите продолжать:\n")
    if num == 'No' or num == 'no':
        break
    else:
        num = int(num)
        for i in range(len(my_list), 0, -1):
            if num <= my_list[i-1]:
                my_list.insert(i, num)
                print(my_list)
                break
            elif num > my_list[0]:
                my_list.insert(0, num)
                print(my_list)
                break



