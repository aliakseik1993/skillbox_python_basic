print('Задача 5. Простые числа')


#Напишите программу,
#которая считает количество простых чисел в заданной последовательности 
#и выводит ответ на экран.
usual_numbers = 0
input_number = int (input("Введите число: "))
for num in range(1, input_number):
  for num_1 in range(2, num - 1):
   if num % num_1 == 0:
     break
  else:
    usual_numbers += 1
    #print(num, "Натуральное число")
print("Натуральных чисел =", usual_numbers, end = "\n")
#Не до конца понял с else, тоесть я отнес else к второму вложеному циклу(методом подбора, на уровне мозга не допер^), тоесть что у нас этот else делает