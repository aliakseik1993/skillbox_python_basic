print("Введите координаты монетки: ")
x = float(input("X: "))
y = float(input("Y: "))
r = int(input("Введите радиус: "))
#if -r <= x <= r or -r <= y <= r:
if x ** 2 + y ** 2 <= r ** 2:
    print("Монетка где-то рядом")
else:
    print("Монетки в области нет")