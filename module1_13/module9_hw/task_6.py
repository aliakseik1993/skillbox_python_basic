print('Задача 6. Спецшифр')

# Два сотрудника спецслужб переписываются необычным шифром.
# Каждую букву они шифруют в виде строки,
# внутри которой есть длинная последовательность букв “s”, 
# а длина самой длинной - это и есть номер буквы алфавита, которую хотят отправить.
# 
# Напишите программу,
# которая получает на вход строку,
# подсчитывает в ней самую длинную последовательность подряд идущих букв “s” и выводит ответ на экран.
# 
# Пример:
# Введите строку: ssbbbsssbc
# Самая длинная последовательность: 3
"""
text = input("Введите строку: ")
summ = 0
max_summ = 0
for number in text:
  if number == "s":
    summ += 1
  elif number != "s" and max_summ <= summ:
    print(summ)
    max_summ = summ
    summ = 0
  elif max_summ >= summ and number == "s":
    summ += 1
print("Самая длинная последовательность:", max_summ)
""""

text = input("Введите строку: ")
summ = 0
max_summ = 0
for number in text:
  if number == 's':
    summ += 1
    if summ > max_summ:
      max_summ = summ
  else:
    summ = 0
print("Самая длинная последовательность:", max_summ)