# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
# и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

# def int_func(arg):
#     letters = list(arg)  # разбиваем слово на буквы
#     upper_word = letters[0].upper() + ''.join(letters[1:])  # увеличиваем первую букву,
#                                                             # остальные прибавляем
#     return upper_word

def int_func(text='No text'):
    char = ord(text[0])
    return chr(char - 32) + text[1:] if char in range(97, 123) else text


word = input("Введите слова: \n")
splitted_w = ''
for i in word.split():
    splitted_w += ' ' + int_func(i)

print(splitted_w)
