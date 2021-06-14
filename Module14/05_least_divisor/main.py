number_input = int(input("Введите число: "))
while number_input <= 1:
    number_input = int(input("Введите число > 1 : "))
for number in range(number_input + 1, 1, -1):
    if number_input % number == 0:
        result = number

print("Наименьший делитель, отличный от единицы:", result)