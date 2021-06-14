"""
print()

print('Задача 1. Тестовое задание')
for row in range(6):
  for col in range(row, row + 12, 2):
    print(col,end='\t')
  print()


summ = 0
number_input = int (input("Введите число: "))
for number in range(1, number_input + 1):
  for number_1 in range(1, number):
    #print(number, number_1)
    number *= number_1
    #print(number, " =")
  else:
    summ += number
print("Сумма факториалов от 1 по", number_input, "=", summ)



num = int(input('Высота пирамиды: '))

# количество дополнительных # для правой части пирамиды
count = 0
for i in range(1, num+1):
  for j in range(num-i): # печатаем нужное количество пробелов для каждого уровня
    print('.', end='')
  for j in range(i+count): # печатаем нужное количество # для каждого уровня
    print('#', end='')
  count += 1
  print()


  print('Задача 10. Яма ')

"""
# В одной компьютерной текстовой игре рисуются всяческие элементы ландшафта.
#
# Напишите программу,
# которая получает на вход число N и выводит на экран числа в виде “ямы”:

# Введите число: 5
# 
# 5........5 8 .
# 54......45 6 .
# 543....345 4 .
# 5432..2345 2 .
# 5432112345
num = int(input('Высота пирамиды: '))
count = 0
pre_count = ""
for i in range(1, num+1):
  for j in range (1):
    pre_count += str(num - count)
    print (pre_count, end = "")
    count += 1
  for j in range((num-i) * 2): # печатаем нужное количество пробелов для каждого уровня
    print('.', end='')
  a = ""
  a = a + pre_count
  print (a, end = "")
  print()

