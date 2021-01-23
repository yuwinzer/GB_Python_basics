# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('--hours', type=int)
parser.add_argument('--hourly_rate', type=int)
parser.add_argument('--prize', type=int, default=0)

args = parser.parse_args()

salary = args.hours * args.hourly_rate

print(f"Сотрудник работал {args.hours} ч. Его зарплата составила {salary}. Премия: {args.prize}")
