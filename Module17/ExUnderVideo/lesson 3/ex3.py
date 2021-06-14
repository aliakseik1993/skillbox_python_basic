import random
list_num = [random.randint(-20, 20) for _ in range(20)]
print(list_num)
a = 2
b = 10
list_num[2:10] = []
print(list_num)