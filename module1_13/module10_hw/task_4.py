print('Задача 4. Крест')

# Напишите программу,
# которая выводит на экран крест из символов “^”.
#
# (Символы выводятся по диагоналям воображаемого квадрата.)




# ^        ^
#  ^      ^ 
#   ^    ^  
#    ^  ^   
#     ^^    
#     ^^    
#    ^  ^   
#   ^    ^  
#  ^      ^ 
# ^        ^

number = 30
x = 30
for row in range (number):
  for col in range (number):
    if row == col:
      print ("^", end = "")
    elif col == x - 1:
      x -= 1
      print ("^", end = "")
    else:
      print (" ", end = "")
  print()