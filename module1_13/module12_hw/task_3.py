print('Задача 3. Апгрейд калькулятора')

# Степан, как и большая часть населения планеты,
# для расчёта суммы и разности чисел использует калькулятор.
# 
# Однако в работе ему нужно
# делать не только  обычные действия вроде сложения и вычитания,
# а делать что-то вручную он уже устал.
# 
# Поэтому Степан решил немного расширить функциональность своего калькулятора.
# 
# Напишите программу,
# которая спрашивает у пользователя число и действие, 
# которое нужно с ним сделать: 
# вывести сумму его цифр,
# вывести максимальную цифру или вывести минимальную цифру. 
# 
# Каждое действие оформите в виде отдельной функции, 
# а основную программу зациклите.
def summ_numbers():
  var_numbers = number
  result = 0
  while var_numbers > 0:
    result += var_numbers % 10
    var_numbers //= 10
  print("Cумма чисел числа", number, "=", result)
  print()
  print("Чтобы вернутся в меню, нажмите Enter")
  print()
  choice = input("Нажми Enter")

def max_numbers():
  var_numbers = number
  pre_number = 0
  while var_numbers > 0:
    #print(var_numbers)
    if pre_number < var_numbers % 10:
      pre_number = var_numbers % 10
    var_numbers //= 10
  print("Максммальное цифра = ", pre_number,)
  print()
  print("Чтобы вернутся в меню, нажмите Enter")
  print()
  choice = input("Нажми Enter")

def min_numbers():
  var_numbers = number
  pre_number = 9
  while var_numbers > 0:
    #print(var_numbers)
    if pre_number > var_numbers % 10:
      pre_number = var_numbers % 10
    var_numbers //= 10
  print("Минимальная цифра = ", pre_number,)
  print()
  print("Чтобы вернутся в меню, нажмите Enter")
  print()
  choice = input("Нажми Enter")

"""
onn = True
def exit(onn):
  print("Работа с программой калькулятор завершена")
  print("Хорошего дня и ночи! и да прибудет с вами сила джидая!")
  return False
# Жаль, но не получилось реализовать
"""

def menu():
  print("Чтобы вывести сумму его цифр, нажмите 1 и подтвердите ввод")
  print("Чтобы вывести максимальную цифру, нажмите 2 и подтвердите ввод")
  print("Чтобы вывести минимальную цифру, нажмите 3 и подтвердите ввод")
  print("Для выхода из программы нажмите 0")
  print()
  choice = int(input("Итак, ваш выбор: "))
  print()
  if choice == 1:
    summ_numbers()
  elif choice == 2:
    max_numbers()
  elif choice == 3:
    min_numbers()
    
while True:
  print()
  print("Для выхода из программы введите 0")
  number = int(input("Введите число: "))
  print()
  if number == 0:
    print("Работа с программой калькулятор завершена")
    print("Хорошего дня и ночи! и да прибудет с вами сила джидая!")
    break
  menu()
  
