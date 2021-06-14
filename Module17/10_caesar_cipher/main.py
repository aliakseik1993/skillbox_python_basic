def caesar_cipher(word):
    abc_russ = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й",
                "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф",
                "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"
                ]
    new_word = ""
    for sym in word:
        for _ in range(1):
            # print(sym, "каждый символ")
            if sym == " ":
                new_word += " "
                break
            index = abc_russ.index(sym) + shift
            if index > 32:
                index = index - 33
            new_word += abc_russ[index]
    return new_word


word_input = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))
# print(word_list)
result = caesar_cipher(list(word_input))

print("Зашифрованное сообщение:", result)

"""
def caesar_cipher(word, shift):
    abc_russ = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    word_list = [abc_russ[(abc_russ.index(symbal) + shift) % 33] if symbal != " " else " " for symbal in word_input]
    new_word = ""
    for i_sym in word_list:
        new_word += i_sym
    return new_word

word_input = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))
result = caesar_cipher(word_input, shift)

print("Зашифрованное сообщение:", result)
"""