print('Задача 3. Посчитай чужую зарплату...')

# Бухгалтер устала постоянно считать вручную среднегодовую зарплату сотрудников компании
# и, чтобы облегчить себе жизнь, обратилась к программисту.
 
# Напишите программу,
# которая принимает от пользователя зарплату сотрудника за каждый из 12 месяцев 
# и выводит на экран среднюю зарплату за год.
months = 0
summ = 0
for number in range(12):
  months += 1
  print("Месяц:", months, "из 12")
  salary_input = int(input("Введите зарплату: "))
  summ += salary_input
print("Средняя зарплата за год =", summ / 12)