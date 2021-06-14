def summ_numbers(number):
    summ_of_numbers = 0
    while number != 0:
        summ_of_numbers += number % 10
        number //= 10
    return summ_of_numbers
def count_of_numbers(number):
    count_of_numbers = 0
    while number != 0:
        number //= 10
        count_of_numbers += 1
    return count_of_numbers
number_input = int(input("Введите число: "))
while number_input <= 0:
    number_input = int(input("Введите число > 0: "))
summ_of_numbers = summ_numbers(number_input)
count_of_numbers = count_of_numbers(number_input)

print("Сумма цифр: ", summ_of_numbers)
print("Кол-во цифр в числе: ", count_of_numbers)
print("Разность суммы и кол-ва цифр: ", summ_of_numbers - count_of_numbers)