print('Задача 5. Число Эйлера')

# Напишите программу, которая находит сумму  ряда с точностью до 1e-5.

# P.S: Формулу смотреть на сайте :)
 
# Пример:
 
# Точность: 1e-20
# Результат: 2.7182818284590455

import math
precision = float(input("Точность: "))

var_number = 0
let_number = 1
result = 0
while let_number > precision:
  let_number = 1 / math.factorial(var_number)
  #print(let_number, "add number")
  result += let_number
  #print(result, " every times")
  var_number += 1
print("Результат", result)
#print(math.e)