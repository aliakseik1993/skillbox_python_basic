print('Задача 1. Кубы чисел')

# Любителю математики Паше снова стало мало распечатанных табличек,
# включая последнюю со степенями двойки.
# Теперь он хочет взять третью степень чисел от 1 до абсолютно любого!

# Напишите программу,
# которая возводит в третью степень каждое число от 1 до N
# и выводит результат на экран.




# Не совсем понял условие, тоесть надо создать бесконечный цикл, где числа подряд вводятся в 3 степень, или мы вводит число которое надо ввести в третью степень и запрашиваем следующие число
number = int(input("Введите число: "))
while number != 0:
  print("Ваше число в третье степени =", number * number * number)
  number = int(input("Введите следующее число или для выхода из программы введите 0: "))

# Ввариант бесконечного цикла
number = 1
print('Задача 1. Кубы чисел, бесконечный цикл')
while number != 0:
  print("Число", number, "В третье степени =", number * number * number)
  number += 1