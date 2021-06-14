print('Задача 10. Максимальное число (по желанию)')
""""
# Пользователь вводит три числа.
# Напишите программу,
# которая выводит на экран максимальное из этих трёх чисел (все числа разные).
# Можно использовать дополнительные переменные, если нужно 
number_input_1 = int(input("Введите первое число: "))
number_input_2 = int(input("Введите второе число: "))
number_input_3 = int(input("Введите третье число: "))
if number_input_1 > number_input_2:
  number_input_1 > number_input_3
  print("Самое большое число =",number_input_1)
if number_input_2 > number_input_1:
  number_input_2 > number_input_3
  print("Самое большое число =",number_input_2)
if number_input_3 > number_input_2:
  number_input_3 > number_input_1
  print("Самое большое число =",number_input_3)
  """

# Пользователь вводит три числа.
# Напишите программу,
# которая выводит на экран максимальное из этих трёх чисел (все числа разные).
# Можно использовать дополнительные переменные, если нужно 
number_input_1 = int(input("Введите первое число: "))
number_input_2 = int(input("Введите второе число: "))
number_input_3 = int(input("Введите третье число: "))
if number_input_1 > number_input_2:
  if number_input_1 > number_input_3:
    print("Самое большое число =",number_input_1)
if number_input_2 > number_input_1:
  if number_input_2 > number_input_3:
    print("Самое большое число =",number_input_2)
if number_input_3 > number_input_2:
  if number_input_3 > number_input_1:
    print("Самое большое число =",number_input_3)
    # Ураа получилось, думал правильно ли делать вложенный if или надо через and, и есть ли такой and в синтаксисе пайтона, но в итоге обошолся без гугла, чему еще больше рад