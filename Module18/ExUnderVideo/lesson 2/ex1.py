words_list = input("Введите три слова через пробел: ").split()

while len(words_list) != 3:
    words_list = []
    print("вы ввели не 3 слова, введите заного")
    words_list = input("Введите три слова через пробел: ").split()

count = 0
text = input("Введите текст использую только пробелы между слов: ").split()

for sum_num in words_list:
    for symbal in text:
        if sum_num == symbal:
            count += 1

print(text)
print(f"Слова встречаются в тексте {count} раз")