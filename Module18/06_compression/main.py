s = input("Введите строку: ")
def zip(text):
    result = []
    result.append([text[0]])
    list_count = 0
    # print(len(text))
    for num in range(len(text)):
        for sum in range (num + 1, len(text)):
            if text[num] == text[sum]:
                result[list_count] += text[num]
                break
            else:
                result.append([text[sum]])
                list_count += 1
                break
    # for element in result:
    #     print(element)
    return "".join([element[0] + str(len(element)) for element in result])
    print(result)


print("Закодированная строка:", zip(s))



# s = "aaAAbbсaaaA"
# result = ""

# for number in range(len(s)):
#     for count in range(number, len(s)):
#         count_num = 1
#         if s[number] == s[count]:
#             count_num += 1
#     result += s[number] + str(count_num)
#
# print(result)


# s = "aaAAbbсaaaA"
# result = []
# final_index = 0
# for sum in range(len(s)):
#     if s.find(s[sum]) == sum:
#         final_index = s.find(s[sum])
#     else:
#
# print(result)

# for number in range(len(s)):
#     finish = number + 1
#     if finish >= len(s):
#         finish = len(s) - 1
#     if s[number] == s[finish]:
#         count += 1
#     else:
#         result += s[number] + str(count)
#         count = 1
#
# print(result)