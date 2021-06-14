import random
first_list = list()
second_list = list()

for _ in range(5):
    number = random.randint(0, 5)
    first_list.append(number)

for _ in range(5):
    number = random.randint(-5, 0)
    second_list.append(number)

first_tuple = tuple(first_list)
second_tuple = tuple(second_list)

# print(first_tuple)
# print(second_tuple)

third_tuple = first_tuple + second_tuple

print(third_tuple, " - третий кортеж")
print("Колличество 0 =", third_tuple.count(0))