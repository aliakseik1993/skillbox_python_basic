print('Задача 8. Сумма ряда')

# Дано натуральное число N.
# Напишите программу для вычисления следующей суммы ряда (начиная с единицы)

# S = 1 - 1/2 + 1/4 - 1/8 + … (-1)**N * 1/2**N 
"""
result = 0
number_input = int(input("Задайте число: "))
for number in range (0, number_input):
 next_number = (- 1)** number * 1 / 2 ** number
 #print(number)
 #result += next_number
 #print(result)
 print("следующие число", next_number)
#s = 1 - 1 ** n * 1 / 2 ** n
"""
number_input = int(input("Задайте колличество чисел в формуле: "))
for number in range (0, number_input, 1):
 next_number = (- 1)** number * 1 / 2 ** number
 #print(number)
 print("следующие число:", next_number)
#Вроде моя программа определяет какое будет следующее число и с каким знаком исходя из последовательности, но точно ли это от меня требовалось, если нет, можете подсказать, какой должен быть финал