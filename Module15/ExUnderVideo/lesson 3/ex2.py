s = input("Введите строку: ")
text = list(s)
symbol = int(input("Введите номер символа"))

print("Символ слева: ", text[symbol - 2])
print("Символ справа: ", text[symbol])
if text[symbol - 1] == text[symbol - 2] and text[symbol - 1] == text[symbol]:
    print("в тексте два таких символа")
elif text[symbol - 1] == text[symbol - 2] or text[symbol - 1] == text[symbol]:
    print("в тексте один такой же символ.")
else:
    print("таких символов нет")