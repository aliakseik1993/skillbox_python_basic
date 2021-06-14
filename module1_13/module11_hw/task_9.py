print('Задача 9. Уравнение')

# Даны действительные коэффициенты a, b, c,
# при этом a≠0. 
# Решите квадратное уравнение ax2+bx+c=0 и выведите все его корни.
# 
# Если уравнение имеет два корня,
# выведите два корня в порядке возрастания,
# если один корень — выведите одно число, 
# если нет корней — не выводите ничего
import math
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))
discriminant = b ** 2 - 4 * a * c
if discriminant > 0:
  x_1 = (-b + math.sqrt(discriminant)) / (2 * a)
  x_2 = (-b - math.sqrt(discriminant)) / (2 * a)
  print("Так как дискриминант =", discriminant, "> 0", "корень x1 = ", x_1, " корень x2 =", x_2)
elif discriminant == 0:
  x = (-b + math.sqrt(discriminant)) / 2 * a
  print("Так как дискриминант =", discriminant,"корень  = ", x)
else:
  print(discriminant, "< 0")
  print("Корней нет! и не будет, overrrrrrrrrrr! все по домам!")