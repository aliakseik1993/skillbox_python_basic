def score_key(tuple):
    return tuple[1][0] - tuple[1][1]


score_tuple = tuple()
score_table = dict()
how_many = int(input("Сколько записей вносится в протокол? "))
print("Записи (результат и имя):\n")

for queue in range(how_many):
    score, name = input('{} запись: '.format(queue+1)).split()
    score = int(score)
    if name in score_table:
        if score > score_table[name][0]:
            score_table[name] = (score, queue)
    else:
        score_table[name] = (score, queue)

score_tuple = tuple(score_table.items())
res_list = sorted(score_tuple, key=score_key, reverse=True)
winner = 1

print("Итоги соревнований:")
for i_winner in res_list[0:3]:
    name = i_winner[0]
    score = i_winner[1][0]
    print(f"{winner} место. {name} ({score})")
    winner += 1


# result = dict()
# how_many = int(input("Сколько записей вносится в протокол? "))
# for i_number in range(how_many):
#     print("{0} запись: ".format(i_number + 1), end="")
#     value = input("").split()
#     result[value[1]] = int(value[0])
#     if result.get(value[1]) != None:
#         if result[value[1]] > int(value[0]):
#             result[value[1]] = result[value[1]]
#         if result[value[1]] < int(value[0]):
#             result[value[1]] = int(value[0])
#
# print("Итоги соревнований:")
# for i_place in range(3):
#     key = max(sorted(result), key = lambda k: result[k])
#     print("{0} место. {1} ({2})".format(i_place + 1, key, result[key]))
#     result[key] = 0


#
# def score_key(tuple):
#     return tuple[1][0] - tuple[1][1]
#
# dict_1 = {'Jack': (95715, 5), 'qwerty': (197128, 4), 'Alex': (95715, 2), 'M': (95715, 8)}
# dict_2 = tuple(dict_1.items())
# res_list = sorted(dict_2, key=score_key, reverse=True)
# print(res_list)
# winner = 1
# for i_winner in res_list[0:3]:
#     print(i_winner)
#     name = i_winner[0]
#     score = i_winner[1][0]
#     print(f"{winner} место. {name} ({score})")
#     winner += 1
# def score_key(tuple):
#     return tuple[1][0] - tuple[1][1]
#
# score_tuple = tuple()
# score_table = dict()
# how_many = int(input("Сколько записей вносится в протокол? "))
# print("Записи (результат и имя):\n")
# for queue in range(how_many):
#     score, name = input('{} запись: '.format(queue+1)).split()
#     score = int(score)
#     if name in score_table:
#         if score > score_table[name][0]:
#             score_table[name] = (score, queue)
#     else:
#         score_table[name] = (score, queue)
# score_tuple = tuple(score_table.items())
# res_list = sorted(score_tuple, key=score_key, reverse=True)
# print(res_list)
# winner = 1
# for i_winner in res_list[0:3]:
#     print(i_winner)
#     name = i_winner[0]
#     score = i_winner[1][0]
#     print(f"{winner} место. {name} ({score})")
#     winner += 1
#
#



# for key, value in dict_new:
#     dict_new_new += (key, tuple(value))


#
# def score_key(a):
#     return a[1][0] - a[1][1]
#
#
# score_table = {}
# amount = int(input("Сколько записей вносится в протокол? "))
# print("Записи (результат и имя):\n")
#
# for time in range(amount):
#     score, name = input('{} запись: '.format(time+1)).split()
#     score = int(score)
#     if name in score_table:
#         if score > score_table[name][0]:
#             score_table[name] = (score, time)
#     else:
#         score_table[name] = (score, time)
#
# scores = list(score_table.items())
# print(score_table)
# scores.sort(key=score_key, reverse=True)
# print(score_table)
# print("\nИтоги соревнований:\n")
# for winner_index in range(3):
#     print(winner_index + 1, 'место.', scores[winner_index][0], end=' ')
#     print('(', scores[winner_index][1][0], ')', sep='')




# result = dict()
# how_many = int(input("Сколько записей вносится в протокол? "))
# for i_number in range(how_many):
#     print("{0} запись: ".format(i_number + 1), end="")
#     value = input("").split()
#     result[value[1]] = int(value[0])
#     if result.get(value[1]) != None:
#         if result[value[1]] > int(value[0]):
#             result[value[1]] = result[value[1]]
#         if result[value[1]] < int(value[0]):
#             result[value[1]] = int(value[0])
#
# print("Итоги соревнований:")
# for i_place in range(3):
#     key = max(sorted(result), key = lambda k: result[k])
#     print("{0} место. {1} ({2})".format(i_place + 1, key, result[key]))
#     result[key] = 0


# result = dict()
# how_many = int(input("Сколько записей вносится в протокол? "))
# queue = 1
# for i_number in range(how_many):
#     print("{0} запись: ".format(i_number + 1), end="")
#     value = input("").split()
#     result[(int(value[0]), queue)] = value[1]
#     queue += 1

# result = {(69485, 1): 'Jack', (95715, 2): 'qwerty', (95715, 3): 'Alex', (83647, 4): 'M', (197128, 5): 'qwerty', (95715, 6): 'Jack', (93289, 7): 'Alex', (95715, 8): 'Alex', (95715, 9): 'M'}
# print(result)
# winner = ""
# for i_place in range(3):
#     max_score = max(result.keys())
#     max_value = max_score[0]
#     min_queue = max_score[1]
#     print(max_value)
#     print("Итоги соревнований:")
#     for keys, value in result.items():
#         if keys[0] == max_value and keys[1] < min_queue:
#             min_queue = keys[1]
#
#     winner = result[(max_value), min_queue]
#     print(winner, " Winner")
#     print(f"{i_place + 1} место. {result[(max_value), min_queue]} ({max_value})")
#     del result[(max_value), min_queue]
