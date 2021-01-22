words_str = input("Введите через пробел несколько слов: \n")
words_list = words_str.split(' ')
print(f"Вы ввели слова: {words_list}\nОни же по порядку:")
for i in range(1, len(words_list) + 1):
    print(f"{i}. {(words_list[i-1])[:10]}")