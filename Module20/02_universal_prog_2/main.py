# list_new = [100, 200, 300, 'буква', 0, 2, 'а']
# text_new = 'О Дивный Новый мир!'
# dict_new = {"100 ": 0, "200": 1, "300": 2, 'буква' : 3, "0": 4, "2" : 5, 'а': 6}
# dict_new = {100: "пупсик", 99: "нечетный пупсик", 200: 200, 300: "300 баксов", 'буква': 2, 0: "черное", 2: "Иванов садись два", 'а': 44}
# tuple_new = (1,2,3,4,5,6,7,7,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
# значение для проверки, лучше копировать в текст


text = 'О Дивный Новый мир!'

def crypto(input_user):
    return [value for index, value in enumerate(input_user) if is_prime(index)]


def is_prime(number):
    for i_num in range(2, number):
        if number % i_num == 0:
            print(i_num)
            return False
    return True

result = crypto(text)
print(result)

# number = 47
# result = is_prime(number)
# print(result)
# if result:
#     print(number)
#
#
# text = {100: "пупсик", 99: "нечетный пупсик", 200: 200, 300: "300 баксов", 'буква': 2, 0: "черное", 2: "Иванов садись два", 'а': 44}
# print(type(text))


# def even_list(string):
#     if type(string) == str:
#         new_list = list()
#         for index, value in enumerate(string):
#             if index % 2 == 0:
#                 new_list.append(value)
#     elif type(string) == list:
#         new_list = string
#         print(new_list)
#         for index, value in enumerate(new_list):
#             if index % 2 != 0:
#                 new_list.remove(value)
#     elif type(string) == dict:
#         new_list = dict()
#         for key, value in string.items():
#             if type(key) == int and key % 2 == 0:
#                 new_list[key] = value
#     elif type(string) == tuple:
#         new_list = list()
#         for index, value in enumerate(string):
#             print(index, value)
#             if index % 2 == 0:
#                 new_list.append(value)
#     return new_list
# # list = [100, 200, 300, 'буква', 0, 2, 'а']
# # text = 'О Дивный Новый мир!'
# # dict_new = {"100 ": 0, "200": 1, "300": 2, 'буква' : 3, "0": 4, "2" : 5, 'а': 6}
# # dict_new = {100: "пупсик", 99: "нечетный пупсик", 200: 200, 300: "300 баксов", 'буква': 2, 0: "черное", 2: "Иванов садись два", 'а': 44}
# # tuple_new = (1,2,3,4,5,6,7,7,7)
# # print(dict_new)
#
# my_list = even_list(text)
# print(my_list)