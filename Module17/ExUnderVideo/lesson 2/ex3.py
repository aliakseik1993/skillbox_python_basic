import random
first_squad = [random.randint(50, 80) for _ in range(10)]
second_squad = [random.randint(30, 60) for _ in range(10)]
result = ["Выжил" if first_squad[i] + second_squad[i] < 100
          else "Погиб" for i in range(10)
          ]
print("Урон первого отряда: ", first_squad)
print("Урон первого отряда: ", second_squad)
print("Состояние третьего отряда: ", result)