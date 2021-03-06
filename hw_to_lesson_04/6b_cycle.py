#6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
# что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from argparse import ArgumentParser
from itertools import cycle

parser = ArgumentParser()
parser.add_argument('--max', type=int,  help='нужен для ограничения строк повтора цикла')
args = parser.parse_args()

random_str = [num for num in range(4)]
iter_str = cycle(random_str)

for i in range(args.max):
    print(next(iter_str))