"""
dogs_exp = []
dog_count = int(input("Сколько собак участвует в бегах? "))
for number in range(dog_count):
    print(f"Сколько очков у собаки № {number +1}:", end = "")
    exp_dog = int(input())
    dogs_exp.append(exp_dog)
min_exp = dogs_exp[0]
max_exp = dogs_exp[0]
for exp in dogs_exp:
    if exp < min_exp:
        min_exp = exp
    if exp > max_exp:
        max_exp = exp
print("Старый список", dogs_exp)
count = 0
for index in dogs_exp:
    if index == min_exp:
        dogs_exp[count] = max_exp
    if index == max_exp:
        dogs_exp[count] = min_exp
    count += 1

print("Новый список", dogs_exp)
"""
dogs_exp = []
dog_count = int(input("Сколько собак участвует в бегах? "))
for number in range(dog_count):
    print(f"Сколько очков у собаки № {number +1}:", end = "")
    exp_dog = int(input())
    dogs_exp.append(exp_dog)
minimum = 0
maximum = 0
print("старый список", dogs_exp)
for i in range(dog_count):
    if dogs_exp[i] < dogs_exp[minimum]:
        minimum = i
    if dogs_exp[i] > dogs_exp[maximum]:
        maximum = i
dogs_exp[minimum], dogs_exp[maximum] = dogs_exp[maximum], dogs_exp[minimum]
print("новый список", dogs_exp)
