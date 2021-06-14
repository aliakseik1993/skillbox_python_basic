print('Задача 10. Метод бутерброда')

# Секретное агентство «Super-Secret-no» решило
# для шифрования переписки своих сотрудников использовать «метод бутерброда».
# Сначала буквы слова нумеруются в таком порядке:
# первая буква получает номер 1,
# последняя буква - номер 2,
# вторая – номер 3,
# предпоследняя – номер 4, потом третья … и так для всех букв (см. рисунок).
# Затем все буквы записываются в шифр в порядке своих номеров.
# 
# Например, слово «sandwich» зашифруется в «shacnidw».
# 
# К сожалению, программист «Super-Secret-no», написал только программу шифрования и уволился.
# И теперь агенты не могут понять, что же они написали друг другу. Помогите им.
# 
# Пример:
# Введите зашифрованное сообщение: shacnidw
# Расшифрованное сообщение: sandwich
#          1   3   5   7   8   6   4   2
# Слово: | s | a | n | d | w | i | c | h |
#
# Шифр:  | s | h | a | c | n | i | d | w |

spy_word = input("Введите зашифрованное сообщение: ")
word = ""
count_of_word = 0
iterration = 0
for number_1 in spy_word:
  count_of_word += 1
print(count_of_word)
if count_of_word % 2 == 0:
  for number in spy_word:
      iterration += 1
      for cycl in range (1, count_of_word, +2):
        if iterration == cycl:
          print(number, end = "")
  iterration = 0
  for number_2 in spy_word:
    iterration += 1
    for cycl_2 in range (count_of_word, 1, -2):
      if iterration == cycl_2:
        word = number_2 + word
print (word)


#Сделал решение красивее
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