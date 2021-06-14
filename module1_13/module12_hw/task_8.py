print('Задача 8. НОД')

#Напишите функцию, вычисляющую наибольший общий делитель двух чисел

def nod_numbers(number_input_1, number_input_2):
  number_1 = number_input_1
  number_2 = number_input_2
  if number_input_1 > number_input_2:
    number_2 = number_input_1
    number_1 = number_input_2
  result_finish = 0
  result = 0
  #print(number_1, "1 chislo")
  #print(number_2, "2 chislo")
  for number in range (1, abs(number_1) + 1):
    if number_1 % number == 0:
      result = number
      #print(result, "number 1")
      if number_2 % result == 0:
        result_finish = result
        #print(result_finish, "number 2")
  print("Максимальный нод для чисел", number_1, ",", number_2, "=", result_finish)


number_input_1 = int(input("Введите число: "))
number_input_2 = int(input("Введите число: "))
nod_numbers(number_input_1, number_input_2)
