print('Задача 3. Слишком большие числа')

# У неудачливого бухгалтера всё опять идёт наперекосяк:
# ему приносят такие большие счета, что числа не помещаются на бумаге.
 
# Напишите программу,
# которая считала бы для него,
# сколько десятичных цифр (знаков) во вводимом числе.
number_input = int(input("Введите число: "))
how_many_symbol = 0
while number_input != 0:
  number_input = number_input // 10 # или надо сколько чисел начиная от 10 до 100, тогда можно изменить на 100
  how_many_symbol += 1
print ("Десятичных цифр в вашем числе:" ,how_many_symbol)