#6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
# что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from argparse import ArgumentParser
from itertools import count
import time

parser = ArgumentParser()
parser.add_argument('--count', type=int, help='указывается целое числа, начиная с которого идет счет')
parser.add_argument('--max', type=int, help='сколько раз выполнить счет в дополнение к стартовому числу')
args = parser.parse_args()

for el in count(args.count):
    print(el)
    time.sleep(1)
    if el >= args.count + args.max:
        break
