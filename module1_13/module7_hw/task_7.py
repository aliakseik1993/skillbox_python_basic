print('Задача 7. Отрезок')

# Напишите программу,
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль 
#среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3.
number_begin = int(input("Введите начальное число: "))
number_end = int(input("Введите конечное число: "))
divider = 0
number_summ = 0
for number in range(number_begin, number_end + 1):
  #print(number)
  if number % 3 == 0:
    divider += 1
    number_summ += number
    #print("Число подходящие под условия", number)
    #print("сумма таких чисел", number_summ)
#print("Колличество такие числе", divider)
print("Среднее арифметическое =", number_summ / divider)