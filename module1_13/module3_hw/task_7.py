print('Задача 7. Поездка по кругу')

# Вася решил потренироваться перед марафоном и покататься вокруг Москвы на скорость.
# Длина дороги — 115 километров.
# Вася стартует с нулевого километра и едет со скоростью v километров в час. 
# На какой отметке он остановится через t часов?
# 
# Реализуйте программу, 
# которая спрашивает у пользователя v и t,
# и выводит целое число от 0 до 114 — номер километра, на котором остановится Вася.
# Учтите, что он может прокатиться больше одного круга.
Route = 115
InputSpeed = int(input('Введите скорость в км\ч: '))
InputTime = int(input('Введите время в часах: '))
ResultDistance = InputSpeed * InputTime
result = ResultDistance % Route
print("Вы на: ", result,"км", "из 115 км круга трассы")