import string
import random
def create_dict(list):
    new_dict = dict()
    for index, value in enumerate(list):
        new_dict[index] = value
    return new_dict
# def random_char():
#     list_new = [','.join(random.choice(string.ascii_lowercase) for _ in range(10))]
#     return list_new
#
#
# first_list = random_char()
# second_list = random_char()

letters = string.ascii_lowercase
first_list = random.choices(letters, k=10) # where k is the number of required rand_letters
second_list = random.choices(letters, k=10)

first_dict = create_dict(first_list)
second_dict = create_dict(second_list)

print(f"Первый список: {first_list}"
      f"\nВторой список: {second_list}"
      f"\nПервый словарь: {first_dict}"
      f"\nВторой словарь: {second_dict}")