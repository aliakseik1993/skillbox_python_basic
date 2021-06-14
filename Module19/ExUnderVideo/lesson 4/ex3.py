text = input("Введите строку: ")
text= set(text)
result = ""
for i_num in text:
    if '0'<=i_num<='9':
        result += i_num
print("Различные цифры строки:", sorted(result))

