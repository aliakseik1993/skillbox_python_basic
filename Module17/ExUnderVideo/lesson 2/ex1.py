a = int(input("Введите начальное число диапозона: "))
b = int(input("Введите конечное число диапозона: "))
list_square = [x ** 2 for x in range(a, b) if x % 2 == 0]
print(f"Квадраты четных чисел от {a} до {b}", list_square)