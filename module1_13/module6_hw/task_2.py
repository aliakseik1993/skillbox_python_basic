print('Задача 2. Коллекторы')

# Напишите робота для коллекторов.
# В самом начале он спрашивает имя должника и сумму долга,
# а затем начинает требовать у него погашения до тех пор, 
# пока он не введёт нужную сумму (равную сумме долга или больше).
# После погашения долга сообщите об этом пользователю и поблагодарите его.
 
# Пример:
# Василий, ваша задолженность составляет 100 рублей.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 50
 
# Маловато, Василий. Давайте ещё раз.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 90
# Маловато, Василий. Давайте ещё раз.
 
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 110
# Отлично, Василий! Вы погасили долг. Спасибо!
name_input = input("Введите ваше имя: ")
money_input =  int(input("Введите сумму вашего долга: "))
debt = False
while debt !=True:
  summ_input = int(input("Cколько рублей вы внесёте прямо сейчас, чтобы её погасить? "))
  if summ_input == money_input:
    print("Отлично,", name_input, "Вы погасили долг. Спасибо!")
    break
  print("Маловато", name_input, "Давай еще раз")