text = input("Введите строку: ")
print("Ответ", end = " ")
for index, value in enumerate(text):
    if value == "~":
        print(index, end = " ")