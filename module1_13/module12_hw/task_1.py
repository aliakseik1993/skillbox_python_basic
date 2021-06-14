print('Задача 1. Сумма чисел')

# Напишите функцию summa_n,
# которая принимает одно целое положительное число N 
# и выводит сумму всех чисел от 1 до N включительно.
# 
# Пример работы программы:
# Введите число: 5
# 
# Я знаю, что сумма чисел от 1 до 5 равна 15
def summa_n(number):
  result = 0
  for summ in range(1, number + 1):
    #print(summ)
    result += summ
  print("сумма чисел от 1, до", number + 1, " =", result)

number = int(input("Введите число: "))
while number < 0:
  number = int(input("Введите число > 0: "))
summa_n(number)