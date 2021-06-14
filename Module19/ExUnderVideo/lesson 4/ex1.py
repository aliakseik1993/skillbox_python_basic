text = input("Введите строку: ")
text_set = set(text)
print(text_set)
# spec_symb = {"!, @, #, $, %, ^, ;, №, :, &, ?, *, (, ), -, =, +, [, ], {, }, ?, /, ., >, <, \, |, ~"}
# spec_str = "!,@,#,$,%,^,;,№,:,&,?,*,(,),-,=,+,[,],{,},?,/,.,>,<,\,|,~"
spec = ".,;:!?"
spec_str = set(spec)
intersection = spec_str.intersection(text_set)
print(intersection)
print("text", text)
result = len(spec_str.intersection(text_set)) + len(spec_str - text_set)

print("Количество знаков пунктуации:", result)
count = 0
for number in text:
    if number in spec_str:
        count += 1
print("Количество знаков пунктуации:", count)
