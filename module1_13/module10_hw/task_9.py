print('Задача 9. Пирамидка 2')


# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
# 
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29
number_ex = 1
num = int (input("Введите высоту пирамиды: "))
iteration = num
for row in range (num):
  for col in range (row + 1):
      print( " " * (iteration + 1 - row), number_ex, end = " ")
      number_ex += 2
  print()