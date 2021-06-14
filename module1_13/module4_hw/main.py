number_input_1 = int(input("Введите первое число: "))
number_input_2 = int(input("Введите второе число: "))
number_input_3 = int(input("Введите третье число: "))
if number_input_1 > number_input_2 and number_input_1 > number_input_3:
  print("Самое большое число =",number_input_1)
elif number_input_2 > number_input_1 and number_input_2 > number_input_3:
  print("Самое большое число =",number_input_2)
else:
  print("Самое большое число =",number_input_3)