print('Задача 6. Метеостанция')

# Для удобства работы сотрудников международной метеостанции
# каждый день нужно распечатывать различные таблицы
# соответствия градусов по шкале Цельсия и Фаренгейта.
#
# Напишите программу,
# которая принимает на вход три целых числа
# в градусах Цельсия: нижняя граница температуры, верхняя граница температуры и шаг.
#
# Программа выводит на экран
# таблицу соответствия градусов Цельсия градусам Фаренгейта
# от нижней до верхней границы с указанным шагом.
#
# Обеспечьте контроль ввода.
# Верхняя граница должна печататься, даже если последний шаг “перепрыгнул “ ее.
# Известно, что 0С соответствует 32F,
# а каждый градус Цельсия эквивалентен 1.8 градусам Фаренгейта.
#
# Пример:
#
# Ввод:
# Нижняя граница: 0
# Верхняя граница: 50
# Шаг: 20
#
# Вывод:
# C        F

# 0        32
# 20       68
# 40       104
# 50       122
import math
low_number = int(input("Нижняя граница: "))
hight_number = int(input("Верхняя граница: "))
step = int(input("Шаг: "))
if hight_number < low_number or step < 0:
  print("Нижняя граница должна быть > 0, а значение верхней границы > нижний границы, и шаг > 0")
  low_number = int(input("Нижняя граница: "))
  hight_number = int(input("Верхняя граница: "))
  step = int(input("Шаг: "))
print("C", "   ", "F", end = "\n")
number_1 = 0
for number in range (low_number, hight_number, step):
  number_1 += step
  if number == 0:
    print(low_number, "   ", "32")
    continue
  print(number, "  ", int(number * 1.8 + 32))
if number_1 >= hight_number:
  print(hight_number, "  ", int(hight_number * 1.8 + 32))
    