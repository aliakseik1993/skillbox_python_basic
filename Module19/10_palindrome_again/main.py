text = input("Введите строку: ")
set_text = set(text)
count_result = 0

for i_sym in set_text:
    count = 0
    for sym in text:
        if i_sym in sym:
            count += 1
    if count % 2 != 0:
        count_result += 1


if count_result < 2:
    print("Можно сделать палиндромом")
else:
    print("Нельзя сделать палиндромом")


# # while " " in text:
# #     text = input("Введите строку без пробелов: ")
# text_set = set(text)
# result = False
# print(text_set)
# # print(text_set)
# if len(text) % 2 != 0:
#     if len(text_set) - 1 == len(text) // 2:
#         result = True
# else:
#     if len(text_set) == len(text) // 2:
#         result = True
#
# if result:
#     print("Можно сделать палиндромом")
# else:
#     print("Нельзя сделать палиндромом")


# протестировал код на разных примерах, вроде 100% работает.