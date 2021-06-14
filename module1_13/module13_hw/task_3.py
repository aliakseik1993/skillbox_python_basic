print('Задача 3. Число наоборот 2')


# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример: 

# Введите первое число: 102
# Введите второе число: 123
 
 
# Первое число наоборот: 201
# Второе число наоборот: 321
 
# Сумма: 522
# Сумма наоборот: 225
def number_return():
  number_back_n = ""
  number_back_k = ""

  for number in str(number_n):
    number_back_n = number + number_back_n # получаем обратное число number_n в виде строки
  for number in str(number_k):
    number_back_k = number + number_back_k # получаем обратное число number_k в виде строки
  
  print()
  print("Первое число наоборот:", number_back_n)
  print("Второе число наоборот:", number_back_k)
  print()

  print("Сумма:", number_n + number_k)
  print("Сумма наоборот:", int(number_back_n) + int(number_back_k))

number_n = int(input("Введите первое число: "))
number_k = int(input("Введите второе число: "))

number_return()