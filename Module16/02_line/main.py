first_class = list(range(160, 176 + 1, 2))
second_class = list(range(162, 180 + 1, 3))

first_class.extend(second_class)

# count = len(first_class)
# iteration = 1
# print(count)
# for index in range(0, count):
#     for index_inside in range(iteration, count):
#         if first_class[index] > first_class[index_inside]:
#             first_class[index], first_class[index_inside] = first_class[index_inside], first_class[index]
#     iteration += 1
# Решение тоже работает, но по-старинке

first_class.sort()

print("Шеренга учеников", first_class)

