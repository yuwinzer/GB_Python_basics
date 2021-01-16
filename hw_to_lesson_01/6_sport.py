num_1day = int(input("Введите количество километров за первый день пробежки: "))
min_dist = int(input("Введите минимальное расстояние, которое должен пробежать спортсмен: "))
print(f"1-й день: {num_1day} км")

next_day_dist = num_1day
a = True
i = 2  # начинаем цикл со второго дня

while a:
    next_day_dist += next_day_dist * 0.1
    print(f"{i}-й день: {round(next_day_dist, 2)} км")
    if next_day_dist >= min_dist:
        print(f"На {i}-й день спортсмен достиг результата — не менее {min_dist} км.")
        break
    i += 1