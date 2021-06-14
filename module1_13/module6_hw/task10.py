print('Задача 10. Игра «Компьютер угадывает число»')

# Поменяйте мальчика и компьютер из прошлой задачи местами.
# Теперь мальчик загадывает число между 1 и 100 (включительно).
# Компьютер может спросить у мальчика:
# «Твое число равно, меньше или больше, чем число N?»,
# где N — число, которое хочет проверить компьютер.
# Мальчик отвечает одним из трёх чисел:
# 1 — равно,
# 2 — больше,
# 3 — меньше.
 
# Напишите программу, 
# которая с помощью цепочки таких вопросов и ответов мальчика угадывает число.
 
# Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за семь попыток.
number_correctly = 5
number_input = int(input("Загадайте число: "))
answer_server = 50
answer_client = 0
half_part = 50
onn = 200
count_of_iteration = 1
while answer_server != onn:
  print("Твое число равно, больше или меньше, чем число", answer_server, "?")
  answer_client = int(input("введите 1(=), 2(>) или 3(<)"))
  half_part //= 2
  if half_part >= 0 and half_part < 3:
    half_part = 1
  if answer_client == 1:
    break
  if answer_client == 2:
    answer_server += half_part
  if answer_client == 3:
    answer_server -= half_part
  #print(answer_server)
  #print(half_part)
  count_of_iteration += 1
print("Это число:", answer_server)
print("Колличество итераций:", count_of_iteration)