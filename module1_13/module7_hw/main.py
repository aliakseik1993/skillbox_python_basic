print('Задача 10.')

#Для настольной игры используются карточки с номерами от 1 до N.
# Одна карточка потерялась.
# Найдите ее, зная номера оставшихся карточек.
# 
# Вводится число N,
# далее еще N − 1 чисел: 
# номера оставшихся карточек (различные числа от 1 до N).
# Программа должна вывести номер потерянной карточки.
number = int(input("Введите число N: "))
summ = 0
summ_1 = 0
for cart in range(1, number):
  carts_range = int(input("Введите номер карточки: "))
  summ_1 += carts_range
for carts in range(1, number + 1):
  summ += carts
#print(summ)
#print(summ_1)
print("Номер потерявшейся карточки =", summ - summ_1)