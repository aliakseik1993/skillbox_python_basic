"""
boys = int(input("Введите колличество мальчиков: "))
girls = int(input("Введите колличество девочек: "))
result = ""
if girls < boys:
  for number in range (0, girls):
    if boys - girls >= 3 or girls - boys >= 3:
      print("Нет решения")
      break
    result += "BG"
    if number > 1:
      reвsult += "G" * (boys - girls)
      break   
else:
   for number in range (0, boys):
    if boys - girls >= 3 or girls - boys >= 3:
      print("Нет решения")
      break
    result += "GB"
    if number > 1:
      result += "B" * (girls - boys)
      continue
print(result)
"""
boys = int(input("Введите колличество мальчиков: "))
girls = int(input("Введите колличество девочек: "))
result = ""
if boys > 2 * girls or girls > boys * 2:
  print("Нет решения")
elif boys >= girls:
  multiplier = boys - girls
  for bgb in range(multiplier):
    result += "BGB"
  for bg in range(girls - multiplier):
    result += "BG"
else:
  multiplier = girls - boys
  for bgb in range(multiplier):
    result += "GBG"
  for bg in range(boys - multiplier):
    result += "GB"
print(result)
#Посмотрел видео разбор, сам так и не смог догадаться как решить.