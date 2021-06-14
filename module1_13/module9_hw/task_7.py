text = input("Введите слова через пробел: ")
word = 0
pre_word = 0
for number in text:
  if number != " ":
    word += 1    
    if word > pre_word:
      pre_word = word
  else:
    word = 0
print("Самая длинное слово:", pre_word)
"""
 сделал правильно, но троху запутался, если я во вложеном   if word > pre_word:
      word = pre_word, то результат всегда 0. получается что оно видет пробел после последнего слово, и присваевает word значение 0?
"""