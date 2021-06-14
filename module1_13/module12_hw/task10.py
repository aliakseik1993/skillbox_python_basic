print('Задача 10')

# Напишите игру - текстовый квест.
# Игрок находится в квартире, его задача - покинуть ее.
# 
# Игрок свободно перемещается по квартире, пока не покинет ее.
# 
# В квартире есть три комнаты (спальня, кухня, ванна) и коридор.
# В ванну можно попасть из коридора и спальни.
# В спальню можно попасть из ванны и коридора.
# На кухню можно попасть только из коридора.
# Коридор связан со всеми комнатами, но в нем дополнительно есть дверь наружу.
# На кухне открыто окно.
# Если игрок пытается выбраться через него, то разбивается и проигрывает


# Пример:

# Вы в спальне. Куда идем?
# 1 - в ванну
# 2 - в коридор
 
# 2

# Вы в коридоре. Куда идем?
# 1 - в спальню
# 2 - в ванну
# 3 - на кухню
# 4 - в дверь
 
# 2
 
# Вы в ванне. Куда идем?
# 1 - в коридор
# 2 - в спальню
 
# 2
 
# Вы в спальне...
def kitchen():
  print("Вы на кухне, куда идем?")
  print("1 - в открытое окно")
  print("2 - вернуться в коридор")
  answer = input("Введите цифру: ")
  if answer == "1":
    print("Вы разбились. Конец игры")
  elif answer == "2":
    main_menu()
  else:
    print("Ошибка ввода")
    kitchen()

def bathroom():
  print("Вы в ванне. Куда идем?")
  print("1 - в коридор")
  print("2 - в спальню")
  answer = input("Введите цифру: ")
  if answer == "1":
    main_menu()
  elif answer == "2":
    sleep_room()
  else:
    print("Ошибка ввода")
    bathroom()


def exit():
  print("Вы вышли на улицу и у вас в руках бонг")
  print("На встречу к вам идет наркоконтроль")
  print("2 - Убежать домой")
  print("1 - Использовать бонг и спрятаться за кустом")
  answer = input("Введите цифру: ")
  if answer == "1":
    print("Это был не Куст! Конец игры!")
  elif answer == "2":
    print("Дежавю!!")
    sleep_room()
  else:
    print("Ошибка ввода")
    exit()
  

  
def main_menu():
  print("Вы в коридоре. Куда идем?")
  print("1 - в спальню")
  print("2 - в ванну")
  print("3 - на кухню")
  print("4 - в дверь")
  answer = input("Введите цифру: ")
  if answer == "1":
    sleep_room()
  elif answer == "2":
    bathroom()
  elif answer == "3":
    kitchen()
  elif answer == "4":
    exit()  
  else:
    print("Ошибка ввода")
    main_menu()

def sleep_room():
  print("Вы в спальне. Куда идем?")
  print("1 - в ванну")
  print("2 - в коридор")
  answer = input("Введите цифру: ")
  if answer == "1":
    bathroom()
  elif answer == "2":
    main_menu()
  else:
    print("Ошибка ввода")
    sleep_room()

game = True
while game == True:
  answer = input("Сыграем в игру?(да\нет): ")
  if answer == "Нет" or answer == "нет":
    print("Вы скучный, так и жизнь пролетела")
    game = False
    break
  sleep_room()