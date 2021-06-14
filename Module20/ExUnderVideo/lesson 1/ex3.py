import random

def change(nums):
    nums = list(nums)
    index = random.randint(0, 4)
    value = random.randint(100, 1000)
    nums[index] = value
    nums = tuple(nums)
    return nums, value


my_nums = (1, 2, 3, 4, 5)
new_nums, rand_val = change(my_nums)

print(f" Кортеж - {new_nums}, Измененное число - {rand_val}")

new_ex = change(new_nums)
# print(new_ex)
new_nums = new_ex[0]

rand_val += new_ex[1]

print(f" Кортеж - {new_nums}, Cумма измененных чисел - {rand_val}")
