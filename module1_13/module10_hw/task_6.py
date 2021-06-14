print('Задача 6. Сумма факториалов')

# Напишите программу,
# которая запрашивает у пользователя число N
# и находит сумму факториалов 1! + 2! + 3! +... + N! 
summ = 0
number_input = int (input("Введите число: "))
for number in range(1, number_input + 1):
  for number_1 in range(1, number):
    #print(number, number_1)
    number *= number_1
    #print(number, " =")
  summ += number
print("Сумма факториалов от 1 по", number_input, "=", summ)