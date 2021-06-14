# TODO здесь писать код
number = int(input("Введите число > 0: "))
while number <= 0:
    number = int(input("Введите число > 0: "))
numbers_list = []
for number_list in range(1, number):
    if number_list % 2 != 0:
        numbers_list.append(number_list)

print(f"Список из нечетных чисел от 1 до {number} = ", numbers_list)