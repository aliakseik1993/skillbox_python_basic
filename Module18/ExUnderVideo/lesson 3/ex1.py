# def caesar_cipher(word, shift):
#     abc_russ = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
#     word_list = [abc_russ[(abc_russ.index(symbal) + shift) % 33] if symbal != " " else " " for symbal in word_input]
#     new_word = ""
#     for i_sym in word_list:
#         new_word += i_sym
#     return new_word
#
# word_input = input("Введите сообщение: ")
# shift = int(input("Введите сдвиг: "))
# result = caesar_cipher(word_input, shift)
#
# print("Зашифрованное сообщение:", result)

def caesar_cipher(word, shift):
    abc_russ = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    word_list = [abc_russ[(abc_russ.index(symbal) + shift) % 33] if symbal != " " else " " for symbal in " ".join(word)]
    return word_list

word_input = input("Введите сообщение: ").split()
shift = int(input("Введите сдвиг: "))

result = caesar_cipher(word_input, shift)

print("Зашифрованное сообщение:", "".join(result))