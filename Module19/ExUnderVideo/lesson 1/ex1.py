num = int(input("Введите число: "))
num_dict = dict()
for key in range(1, num + 1):
    num_dict[key] = key * key
print("Результат:", num_dict)