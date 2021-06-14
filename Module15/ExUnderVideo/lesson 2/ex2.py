count_of_number = int(input("Кол-во чисел в списке: "))
numbers_list = []
for i in range(count_of_number):
    print(f"\nВведите {i + 1} число: ", end = "")
    number = int(input(""))
    numbers_list.append(number)
number_dropper = int(input("Введите делитель: "))
count = 0
summ = 0
for result in numbers_list:
    if result % number_dropper == 0:
        summ += count
        print(f"Индекс числа {result} : {count}")
    count += 1
print("Сумма индексов: ", summ)
