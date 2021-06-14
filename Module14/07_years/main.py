first_year = int(input("Введите первый год: "))
second_year = int(input("Введите второй год: "))
while first_year > second_year and first_year <= 999 and second_year <= 999:
    print("Первый год должен быть меньше второго")
    first_year = int(input("Введите первый год: "))
    second_year = int(input("Введите второй год: "))
print(f"Года с {first_year} до {second_year} с тремя одинаковыми числами:")
for number in range(first_year, second_year):
    iteration = 0
    last_number = number % 10
    pre_number = (number // 10) % 10
    if last_number == pre_number and last_number == (number // 100) % 10 or \
        last_number == pre_number and last_number == number // 1000:
        print(number)
    elif pre_number == (number // 100) % 10 and pre_number == number // 1000:
        print(number)