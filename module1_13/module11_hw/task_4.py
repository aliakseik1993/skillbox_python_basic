print('Задача 4. Первая цифра')

# Дано положительное действительное число X. 
# Выведите его первую цифру после десятичной точки. 
# При решении этой задачи нельзя пользоваться условной инструкцией, циклом или строками
import math
number = float(input("Введите число: "))
number_int = int(number)
number_round_2 = round(number, 2)
#print("инт намбер =", number_int, " округленное число =", number_round_2)
new_number = round(number_round_2 - number_int, 1)
print("Первая цифра после десятичной дроби = ", int(new_number * 10))