spy_word = input("Введите зашифрованное сообщение: ")
word = ""
count_of_word = 0
print ("Расшифрованное слово:", end = " ")
for number_1 in spy_word:
  count_of_word += 1
  if count_of_word % 2 != 0:
    print(number_1, end = "")
  else:
    word = number_1 + word
print(word)