print('Задача 7. Наибольшая сумма цифр')

# Вводится N чисел. 
# Среди натуральных чисел, которые были введены, 
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.
pre_summ = 0
summ = 0
number_biggest = 0
for number in range(3):
  print("Введите число №", number + 1)
  number_input = int(input())
  temp_number = number_input
  if number_input <= 0:
    number_input = int(input("Введите число > 0 "))
  while number_input > 0:
    summ += number_input % 10
    number_input //= 10
  if summ > pre_summ:
    number_biggest = temp_number
    pre_summ = summ
  summ = 0
print("Наибольшее число по сумме цифр:", number_biggest, "\n сумма его цифр =", pre_summ)