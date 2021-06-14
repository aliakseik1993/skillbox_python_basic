user_text = input("Введите строку: ")
text = list(user_text)
print(text)
count = 0
count_i = 0
for i in text:
    if i == ":":
        text[count] = ";"
        count_i += 1
    count += 1
print("Измененная строка: ", end = "")
for new_text in text:
    print(new_text, end = "")
print()
print("Кол-во замен", count_i)