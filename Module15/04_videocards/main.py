videocards = int (input("Кол-во видеокарт: "))
videocarts_base = []
new_base = []
for number in range(videocards):
    print(number + 1, "Видеокарта: ", end = "")
    name = int(input())
    videocarts_base.append(name)
result = videocarts_base[0]
for index in range(videocards):
    if result < videocarts_base[index]:
        result = videocarts_base[index]

for index in range(videocards):
    if videocarts_base[index] != result:
        new_base.append(videocarts_base[index])
print("Старый список видеокарт: ", videocarts_base)
print("Новый список видеокарт: ", new_base)