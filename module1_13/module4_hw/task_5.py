print('Задача 5. Модуль числа')

# Математик Саша пишет программу, которая должна строить график функции y = |x|.
# Для этого ему нужно находить модуль очередного числа x,
# то есть если число x отрицательное, то переводить его в положительное.
# Напишите программу, которая выводит на экран модуль введённого числа.
# 
# Пример:
# Ввели 5, ответ 5
# Ввели −7, ответ 7
# 
# Подсказка: достаточно в некоторых случаях переприсвоить переменную со знаком минус.
number_input = int(input("Введите число: "))
if number_input < 0:
  number_back = -number_input
  print("Ответ", number_back)
else:
  print("Ответ", number_input)