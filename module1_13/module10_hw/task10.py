print('Задача 10. Яма ')


# В одной компьютерной текстовой игре рисуются всяческие элементы ландшафта.
#
# Напишите программу,
# которая получает на вход число N и выводит на экран числа в виде “ямы”:

# Введите число: 5
# 
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345
num = int(input('Высота пирамиды: '))
count = 0
pre_count = ""
a = ""
b = ""
for i in range(1, num+1):
  for j in range (1):
    pre_count += str(num - count)
    print (pre_count, end = "")
    count += 1
  for j in range((num-i) * 2):
    print('.', end='')
  b = -(count - 1 - num)
  a = str(b) + a
  print (a, end = "")
  print()