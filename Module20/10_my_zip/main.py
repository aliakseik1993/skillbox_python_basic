def length():
    if len(pre_res) > len(input_user):
        finish = len(input_user)
    else:
        finish = len(pre_res)
    return finish


# input_user = "abcd"
# input_user = ["a", "b", "c", "d"]
# input_user = {"a", "b", "c"}
# input_user = {1: 1, 2: 2, 3: 3}
input_user = {"a": 1, "b": 2, "c": 3, "d": 4}

user_tuple = (10, 20, 30, 40)
pre_res = [elem for elem in input_user]
finish = length()

result = ((pre_res[count], user_tuple[count]) for count in range(finish))

print(f"Работа генератора в действии:\n",  result)
for elem in result:
    print(elem)












#
#
# def length():
#     if len(a) > len(b):
#         finish = len(a)
#     else:
#         finish = len(b)
#     return finish
# a = "abcd"
# b = (10, 20, 30, 40)
# dict_c = dict()
# c = tuple()
#
# finish = length()
# print(finish)
# for count in range(0, finish):
#     dict_c[a[count]] = b[count]
# print(dict_c)
#
# c = ((x, y) for x, y in dict_c.items())
# # for elem in range(0, finish - 1):
# #     i_elem = a[elem], b[elem]
# #     c += (i_elem, )
# print(c)
# for i_num in c:
#     print(i_num)
#
# print("следующий способ")
#
# def length():
#     if len(a) > len(b):
#         finish = len(a)
#     else:
#         finish = len(b)
#     return finish
# a = "abcd"
# b = (10, 20, 30, 40)
# dict_c = dict()
# c = tuple()
#
# finish = length()
# print(finish)
# for count in range(0, finish):
#     dict_c[a[count]] = b[count]
# print(dict_c)
# c = ((a[s], b[s]) for s in range(finish))
# # for elem in range(0, finish - 1):
# #     i_elem = a[elem], b[elem]
# #     c += (i_elem, )
# print(c)
# for i_num in c:
#     print(i_num)
#
# print("следующий способ")
#
# def length():
#     if len(a) > len(b):
#         finish = len(a)
#     else:
#         finish = len(b)
#     return finish
# a = "abcd"
# b = (10, 20, 30, 40)
# dict_c = dict()
# c = (i for i in a)
#
# finish = length()
# print(finish)
# for count in range(0, finish):
#     dict_c[a[count]] = b[count]
# print(dict_c)
# c = ((a[s], b[s]) for s in range(finish))
# # for elem in range(0, finish - 1):
# #     i_elem = a[elem], b[elem]
# #     c += (i_elem, )
# print(c)
# for i_num in c:
#     print(i_num)