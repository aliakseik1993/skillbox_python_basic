print('Задача 4. Площадь треугольника')

# Напишите программу,
# которая запрашивает у пользователя длины двух катетов
# в прямоугольном треугольнике и выводит его площадь.

# Формула: 
# S = ab/2
cathetusA = int(input("Введите катет первой стороны треугольника: "))
cathetusB = int(input("Введите катет второй стороны треугольника: "))
print ("Площадь треугольника =", (cathetusA*cathetusB)/2 )