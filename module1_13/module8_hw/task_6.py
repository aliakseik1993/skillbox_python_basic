print('Задача 6. Письмо')

# У нас есть
# квадратный конверт размера 12х12 сантиметров и письмо на квадратном листе бумаги,
# которое не помещается в конверт.
# 
# Напишите программу,
# которая подскажет сколько раз нужно сложить письмо пополам,
# чтобы оно поместилось в конверт.
# Размеры письма вводятся с клавиатуры.
long = int(input("Введите одну сторону письма: "))
summ = 0
while long > 12:
  summ += 2
  long /= 2
  print("Сложите письмо")
  #print(long)
print("Письмо надо сложить", summ, "раз")
#Теперь понял, мы складываем каждую сторону письма
