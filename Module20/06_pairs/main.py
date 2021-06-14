import random
ex_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = []
for i in range(0, len(ex_list), 2):
    if i < len(ex_list) - 1:
        new_list.append((ex_list[i], ex_list[i + 1]))

print("Оригинальный список: ", ex_list)
print("Новый список: ", new_list)

#Способ 2
print()
print("****************Способ №2****************")

ex_list_new = [random.randint(0, 100) for _ in range(10)]
print("Оригинальный список", ex_list_new)
value = list(zip(ex_list_new[0:len(ex_list_new):2], ex_list_new[1:len(ex_list_new):2]))
print("Новый список", value)