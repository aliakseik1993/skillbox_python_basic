print('Задача 8. Режем число на части')

# Реализуйте программу,
# которая получает на вход четырёхзначное число
# и выводит на экран каждую его цифру отдельно
# (в одну строчку либо каждая цифра в новой строчке).
# Само число при этом изменять нельзя, то есть нужно обойтись без переприсваивания.
# Однако можно использовать сколько угодно переменных
number = int(input("Введите четерехзначное число: "))
result1 = number % 10
result2 = (number // 10) % 10
result3 = (number // 100) % 10
result4 = number // 1000
print("Первая цифра вашего числа =", result4)
print("Вторая цифра вашего числа =", result3)
print("Третья цифра вашего числа =", result2)
print("Четвертая цифра вашего числа =", result1)