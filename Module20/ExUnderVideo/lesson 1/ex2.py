import math
def squad_cylinder():
    side_squad = 2 * math.pi * radius * hight
    squad = side_squad + 2 * math.pi * radius * radius
    return side_squad, squad
radius = int(input("Введите радиус: "))
hight = int(input("Введите высоту: "))
result = squad_cylinder()
print("Площадь боковой поверхности цидиндра = {0}, "
      "\nПлощадь цилиндра = {1}".format(result[0], result[1]))
