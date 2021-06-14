print('Задача 6. Недоделка 2')

# Вы всё так же работаете в конторе по разработке игр
# и смотрите различные программы прошлого горе-программиста.
# В одной из игр для детей, связанной с мультяшной работой с числами,
# вам нужно было написать код по следующим условиям:
# программа получает на вход два числа.
#
# В первом числе должно быть не меньше трёх цифр,
# во втором числе — не меньше четырёх,
# иначе программа выдаёт ошибку.
# Если всё нормально, то в каждом числе первая и последняя цифра меняются местами,
# а затем выводится их сумма.
#
#
# И тут вы натыкаетесь на программу,
# которая была написана прошлым программистом и которая как раз решает такую задачу!
# Однако старший программист сказал вам немного переписать этот код,
# чтобы он не выглядел так ужасно.
# Да и вам самим становится, мягко говоря, не по себе от него.
#
# Разбейте приведённую ниже программу на функции.
# Повторений кода должно быть как можно меньше.
# Также сделайте,
# чтобы в основной части программы был только ввод чисел, затем изменённые числа и вывод их суммы.

def restart():
  number_one = int(input("Введите первое число: "))
  number_two = int(input("Введите второе число: "))
  number_return_one = return_number_three(number_one)
  number_return_two = return_number_four(number_two)
  print("Сумма чисел =", number_return_one + number_return_two)

def return_number_three(number_one):
  temp = number_one
  count = 0
  iterration = 0
  between_number = ""
  while temp > 0:
    count += 1
    temp //= 10
  if count < 3:
    print("В первом числе меньше трёх цифр.")
    restart()
  else:
    for number in str(number_one):
      if 1 <= iterration < count - 1:
        between_number += number
      iterration += 1
  number_new = int(str(number_one % 10) + between_number + str(number_one // 10 ** (count - 1)))
  print('Изменённое первое число:', number_new)
  return number_new

def return_number_four(number_two):
  temp = number_two
  count = 0
  iterration = 0
  between_number = ""
  while temp > 0:
    count += 1
    temp //= 10
  if count < 4:
    print("В втором числе меньше 4-ех цифр.")
    restart()
  else:
    for number in str(number_two):
      if 1 <= iterration < count - 1:
        between_number += number
      iterration += 1
  number_two_new = int(str(number_two % 10) + between_number + str(number_two // 10 ** (count - 1)))
  print('Изменённое второе число:', number_two_new)
  return number_two_new

number_one = int(input("Введите первое число: "))
number_two = int(input("Введите второе число: "))

number_return_one = return_number_three(number_one)
number_return_two = return_number_four(number_two)

print("Сумма чисел =", number_return_one + number_return_two)



"""

first_n = int(input("Введите первое число: "))
first_num_count = 0
temp = first_n

while temp > 0:
    first_num_count += 1
    temp = temp // 10

if first_num_count < 3:
    print("В первом числе меньше трёх цифр.")
else:
    last_digit = first_n % 10
    first_digit = first_n // 10 ** (first_num_count - 1)
    between_digits = first_n % 10 ** (first_num_count - 1) // 10
    first_n = last_digit * 10 ** (first_num_count - 1) + between_digits * 10 + first_digit
    print('Изменённое первое число:', first_n)
    second_n = int(input("\nВведите второе число: "))
    second_num_count = 0
    temp = second_n
    
    while temp > 0:
        second_num_count += 1
        temp = temp // 10
    if second_num_count < 4:
        print("Во втором числе меньше четырёх цифр.")
    else:
        last_digit = second_n % 10
        first_digit = second_n // 10 ** (second_num_count - 1)
        betweenDigits = second_n % 10 ** (second_num_count - 1) // 10
        second_n = last_digit * 10 ** (second_num_count - 1) + between_digits * 10 + first_digit
        print('Изменённое второе число:', second_n)
        print('\nСумма чисел:', first_n + second_n)