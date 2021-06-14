line = input("Введите строку: ")
count_lower = 0
count_upper = 0

for count in line:
    if count.islower():
        count_lower += 1
    elif count.isupper():
        count_upper += 1

if count_lower > count_upper:
    print("Результат:", line.lower())
else:
    print("Результат:", line.upper())

print(f"lower {count_lower}, upper = {count_upper}")