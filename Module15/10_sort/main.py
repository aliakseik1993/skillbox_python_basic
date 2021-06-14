begin_list = [1, 4, -3, 0, 10]
print("Изначальный список:", begin_list)
count = len(begin_list) - 1
iterration = 0
for num in range(0, count):
    for num_inside in range(iterration, count):
        if begin_list[num] > begin_list[num_inside]:
            begin_list[num], begin_list[num_inside] = begin_list[num_inside], begin_list[num]
    iterration += 1

# count_inside = 0
# while count > 0:
#     begin_list[count], begin_list[count_inside] = begin_list[count_inside], begin_list[count]
#     count -= 1
#     count_inside += 1
print("Отсортированный список:", begin_list)