print('Задача 9. Сумма ряда')

# Пользователь вводит действительное число
# "х" и точность "precision".

# P.S: Формулу смотреть на сайте :)


# Напишите программу,
# которая по число х вычисляет сумму ряда в точности до precision.


# Операцией возведения в степень и функцией factorial пользоваться нельзя.

# Пример:
# Введите точность: 0.001
# total = x ** (2 * y) / math.factorial(2 * y) * (-1) ** y
# Введите x: 5
# Сумма ряда =  0.2836250150891709

def formula(y):
  x_inside = x
  if y == 0:
    x_inside = 1
  for number in range (2 * y - 1):
    x_inside = x_inside * 5
  ############################################
  y_factorial = 1
  for number in range (1, y * 2 + 1):
    y_factorial *= number
  ############################################
  y_inside = -1
  if y % 2 == 0:
    y_inside = 1
  #############################################
  total = x_inside / y_factorial * y_inside 
  return total

precision = float(input("Введите точность: "))
x = float(input("Введите x: "))
number_n = 0
finish = formula(number_n)
result = finish
#print(result)
while abs(finish) > precision:
  number_n += 1
  finish = formula(number_n)
  result += finish
print("Сумма ряда =", result)




"""



import math

def formula(y):
  total = x ** (2 * y) / math.factorial(2 * y) * (-1) ** y 
  return total

precision = float(0.001)
x = float(5)
number_n = float(0)

finish = formula(number_n)
result = finish
print(result)
while abs(finish) > precision:
  number_n += 1
  finish = formula(number_n)
  result += finish
  print(result)



import math

def formula(y):
  result_1 = (-1) ** y
  result_2 = x ** (2 * y)
  result_3 = math.factorial((2 * y))
  total = result_2 / result_3 * result_1
  return total

precision = float(0.001)
x = float(5)
number_n = float(0)

finish = formula(number_n)
result = finish
print(result)
while abs(finish) > precision:
  number_n += 1
  finish = formula(number_n)
  result += finish
  print(result)




import math


x = 5
y = 4

x_1 = (-1) ** y 
x_2 = -1

if y % 2 == 0:
  x_2 = 1

print(x_1, x_2)
print("-----------------------------")


import math



def formula(y):
  total = x ** (2 * y) / math.factorial(2 * y) * (-1) ** y 
  return total

precision = float(0.001)
x = float(5)
number_n = float(0)

finish = formula(number_n)
result = finish
#print(result)
while abs(finish) > precision:
  number_n += 1
  finish = formula(number_n)
  result += finish
  print(result)


#total = x ** (2 * y) / math.factorial(2 * y) * (-1) ** y 



def formula(y):
  x_inside = x
  if y == 0:
    x_inside = 1
  for number in range (2 * y - 1):
    x_inside = x_inside * 5
  ############################################
  y_factorial = 1
  for number in range (1, y * 2 + 1):
    y_factorial *= number
  ############################################
  y_inside = -1
  if y % 2 == 0:
    y_inside = 1
  #############################################
  total = x_inside / y_factorial * y_inside 
  return total

precision = float(input("Введите точность: "))
x = float(input("Введите x: "))
number_n = 0
finish = formula(number_n)
result = finish
#print(result)
while abs(finish) > precision:
  number_n += 1
  finish = formula(number_n)
  result += finish
print("Сумма ряда =", result)

"""
