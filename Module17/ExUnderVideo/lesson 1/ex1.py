a = int(input("Введите начальное число диапозона: "))
b = int(input("Введите конечное число диапозона: "))
list_square = [x ** 2 for x in range(a, b)]
list_cube = [x ** 3 for x in range(a, b)]
print(f"Кубы чисел от {a} до {b}", list_cube)
print(f"Квадраты чисел от {a} до {b}", list_square)