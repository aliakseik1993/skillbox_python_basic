print('Задача 6. Успеваемость в классе')

# В классе N человек.
# Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было. 
# 
# Напишите программу, 
# которая получает список оценок - N чисел - и выводит на экран сообщение о том, 
# кого сегодня больше: отличников, хорошистов или троечников.
excellent = 0
good = 0
bad = 0
number_of_students = int(input("Введите колличество студентов: "))
for students in range(number_of_students):
  print("Студент: ", students + 1)
  rating_input = int(input("Введите оценку: "))
  if rating_input == 3:
    bad += 1
  elif rating_input == 4:
    good += 1
  else:
    excellent += 1
if bad > good and bad > excellent:
  print("Сегодня больше троечников")
elif good > bad and good > excellent:
  print("Сегодня больше хорошистов")
else:
  print("Сегодня больше отличников")