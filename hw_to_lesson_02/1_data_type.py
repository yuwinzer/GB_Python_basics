something = ['apple', 33, [54, 56, 76], 54, (11, 34, 7)]
print(f"Убедимся, что был создан список: {type(something)}")
for i in range (0, len(something)):
    print(f"Элемент {something[i]} имеет тип данных: {type(something[i])}")