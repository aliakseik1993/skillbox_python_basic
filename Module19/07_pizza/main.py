orders = int(input("Введите кол-во заказов: "))
pizza_dict = dict()
for i_order in range(orders):
    print(f"{i_order + 1} заказ: ", end = "")
    order = input().split()
    while len(order) != 3:
        print("Введите правильно через пробел, фамилия название_пиццы колличество")
        print(f"{i_order + 1} заказ: ", end="")
        order = input().split()
    check = pizza_dict.get(f"{order[0]}")
    if check != None:
        last_check = pizza_dict.get(f"{order[0]}").get(f"{order[1]}")
        if last_check != None:
            pizza_dict[order[0]].update({order[1]: str(int(order[2]) + int(pizza_dict.get(f"{order[0]}").get(f"{order[1]}")))})
        else:
            pizza_dict[order[0]].update({order[1]: order[2]})
    else:
        pizza_dict[order[0]] = {order[1]: order[2]}
# print(pizza_dict)


for key in pizza_dict:
    print(f"{key}:")
    for value in pizza_dict[key]:
        print("             ",
              f"{value}: {pizza_dict[key][value]}")


#
# order = "Иванов Пепперони 1".split()
# pizza_dict = dict()
# pizza_dict[order[0]] = {order[1]: order[2]}
# print(pizza_dict)
# order = "Иванов Пепперони 3".split()
# check = pizza_dict.get(f"{order[0]}").get(f"{order[1]}")
# if check != None:
#    pizza_dict[order[0]] = {order[1]: str(int(order[2]) + int(pizza_dict.get(f"{order[0]}").get(f"{order[1]}")))}
# else:
#     pizza_dict[order[0]] = {order[1]: order[2]}
# print(check)
# print(pizza_dict)
#
# order = "Петров Де-Люкс 2".split()
# print(order)
# check = pizza_dict.get(f"{order[0]}", {}).get(f"{order[1]}")
# print(check)
# if check != None:
#    pizza_dict[order[0]] = {order[1]: str(int(order[2]) + int(pizza_dict.get(f"{order[0]}").get(f"{order[1]}")))}
# else:
#     pizza_dict[order[0]] = {order[1]: order[2]}
# print(pizza_dict)
#
# order = "Иванов Мексиканская 2".split()
# print("last print", pizza_dict.get(f"{order[0]}"))
# check = pizza_dict.get(f"{order[0]}")
# if check != None:
#     last_check = pizza_dict.get(f"{order[0]}").get(f"{order[1]}")
#     print(pizza_dict.get(f"{order[0]}").get(f"{order[1]}"))
#     if last_check != None:
#         pizza_dict[order[0]] = {order[1]: str(int(order[2]) + int(pizza_dict.get(f"{order[0]}").get(f"{order[1]}")))}
#     else:
#         # new_dict = dict()
#         # new_dict[order[0]] = {order[1]: order[2], pizza_dict[order[0]].keys(): pizza_dict[order[0]].values() }
#         # print(new_dict)
#         print(pizza_dict.get(f"{order[0]}"), "print")
#         pizza_dict[order[0]].update({order[1]: order[2]})
# print(pizza_dict)
#
# order = "Иванов Мексиканская 4".split()
# print("last print", pizza_dict.get(f"{order[0]}"))
# check = pizza_dict.get(f"{order[0]}")
# if check != None:
#     last_check = pizza_dict.get(f"{order[0]}").get(f"{order[1]}")
#     print(pizza_dict.get(f"{order[0]}").get(f"{order[1]}"))
#     if last_check != None:
#         pizza_dict[order[0]] = {order[1]: str(int(order[2]) + int(pizza_dict.get(f"{order[0]}").get(f"{order[1]}")))}
#     else:
#         # new_dict = dict()
#         # new_dict[order[0]] = {order[1]: order[2], pizza_dict[order[0]].keys(): pizza_dict[order[0]].values() }
#         # print(new_dict)
#         pizza_dict[order[0]].update({order[1]: order[2]})
# print(pizza_dict)
#
# order = "Иванов Геморойная 203".split()
# print("last print", pizza_dict.get(f"{order[0]}"))
# check = pizza_dict.get(f"{order[0]}")
# print(len(pizza_dict[order[0]]), "Длина")
# if check != None:
#     last_check = pizza_dict.get(f"{order[0]}").get(f"{order[1]}")
#     print(pizza_dict.get(f"{order[0]}").get(f"{order[1]}"))
#     if last_check != None:
#         pizza_dict[order[0]].update({order[1]: str(int(order[2]) + int(pizza_dict.get(f"{order[0]}").get(f"{order[1]}")))})
#     else:
#         # new_dict = dict()
#         # new_dict[order[0]] = {order[1]: order[2], pizza_dict[order[0]].keys(): pizza_dict[order[0]].values() }
#         # print(new_dict)
#         pizza_dict[order[0]].update({order[1]: order[2]})
# print(pizza_dict)
#
# order = "Иванов Геморойная 2".split()
# print("last print", pizza_dict.get(f"{order[0]}"))
# check = pizza_dict.get(f"{order[0]}")
# if check != None:
#     last_check = pizza_dict.get(f"{order[0]}").get(f"{order[1]}")
#     print(pizza_dict.get(f"{order[0]}").get(f"{order[1]}"))
#     print(len(pizza_dict[order[0]]), "Длина")
#     if last_check != None:
#         pizza_dict[order[0]].update({order[1]: str(int(order[2]) + int(pizza_dict.get(f"{order[0]}").get(f"{order[1]}")))})
#     else:
#         # new_dict = dict()
#         # new_dict[order[0]] = {order[1]: order[2], pizza_dict[order[0]].keys(): pizza_dict[order[0]].values() }
#         # print(new_dict)
#         pizza_dict[order[0]].update({order[1]: order[2]})
# print(pizza_dict)
# order = "Иванов Пепперони 1".split()
# pizza_dict = dict()
# pizza_dict[order[0]] = order[1]: order[2]
# print(pizza_dict)
# order = "Иванов Пепперони 3".split()
# check = pizza_dict.get(f"{order[0]}").get(f"{order[1]}")
# if check != None:
#    pizza_dict[order[0]] = {order[1]: str(int(order[2]) + int(pizza_dict.get(f"{order[0]}").get(f"{order[1]}")))}
# else:
#     pizza_dict[order[0]] = {order[1]: order[2]}
# print(check)
# print(pizza_dict)
#
# order = "Петров Де-Люкс 2".split()
# print(order)
# check = pizza_dict.get(f"{order[0]}", {}).get(f"{order[1]}")
# print(check)
# if check != None:
#    pizza_dict[order[0]] = {order[1]: str(int(order[2]) + int(pizza_dict.get(f"{order[0]}").get(f"{order[1]}")))}
# else:
#     pizza_dict[order[0]] = {order[1]: order[2]}
# print(pizza_dict)
#
# order = "Иванов Мексиканская 2".split()
# print("last print", pizza_dict.get(f"{order[0]}"))
# check = pizza_dict.get(f"{order[0]}")
# if check != None:
#     last_check = pizza_dict.get(f"{order[0]}").get(f"{order[1]}")
#     if last_check != None:
#         pizza_dict[order[0]] = {order[1]: str(int(order[2]) + int(pizza_dict.get(f"{order[0]}").get(f"{order[1]}")))}
#     else:
#         # new_dict = dict()
#         # new_dict[order[0]] = {order[1]: order[2], pizza_dict[order[0]].keys(): pizza_dict[order[0]].values() }
#         # print(new_dict)
#         pizza_dict[order[0]] = {order[1]: order[2]}
# print(pizza_dict)


#
# order = "Иванов Пепперони 1".split()
# pizza_dict = dict()
# pizza_dict[order[0]] = [order[1], order[2]]
# print(pizza_dict)
# order = "Иванов Пепперони 3".split()
# check = pizza_dict.get(f"{order[0]}")
# print(pizza_dict[order[0]][1])
# if check != None:
#    for i_sym in pizza_dict[order[0]]:
#        print(i_sym)
#        if order[1] == i_sym:
#            pizza_dict[order[0]][1] = str(int(pizza_dict[order[0]][1]) + int(order[2]))
# else:
#     pizza_dict[order[0]] = [values for values in pizza_dict.get(f"{order[0]}")]
# print(check)
# print(pizza_dict)
#
# order = "Петров Де-Люкс 2".split()
# check = pizza_dict.get(f"{order[0]}")
# if check != None:
#    for i_sym in pizza_dict[order[0]]:
#        print(i_sym)
#        if order[1] == i_sym:
#            pizza_dict[order[0]][1] = str(int(pizza_dict[order[0]][1]) + int(order[2]))
#            break
#    else:
#        pizza_dict[order[0]] = [values for values in pizza_dict.get(f"{order[0]}")]
# else:
#     pizza_dict[order[0]] = [order[1], order[2]]
# print(check)
# print(pizza_dict)
#
# order = "Иванов Мясная 3".split()
# check = pizza_dict.get(f"{order[0]}")
# if check != None:
#    for i_sym in pizza_dict[order[0]]:
#        flag = False
#        print(i_sym)
#        if order[1] == i_sym:
#            pizza_dict[order[0]][1] = str(int(pizza_dict[order[0]][1]) + int(order[2]))
#            flag = True
#    if flag == False:
#        pizza_dict[order[0]] = [values for values in pizza_dict.get(f"{order[0]}")], [order[1], order[2]]
# else:
#    pizza_dict[order[0]] = [order[1], order[2]]
# print(check)
# print(pizza_dict)
#
# order = "Петров Интересная 5".split()
# check = pizza_dict.get(f"{order[0]}")
# print(pizza_dict[order[0]])
# if check != None:
#    for i_sym in pizza_dict[order[0]]:
#
#        if order[1] == i_sym:
#            pizza_dict[order[0]][1] = str(int(pizza_dict[order[0]][1]) + int(order[2]))
#            break
#    else:
#        pizza_dict[order[0]] = [values for values in pizza_dict.get(f"{order[0]}")], [order[1], order[2]]
# else:
#    pizza_dict[order[0]] = [order[1], order[2]]
# print(check)
# print(pizza_dict)
#
# order = "Петров Интересная 2".split()
# check = pizza_dict.get(f"{order[0]}")
# print(pizza_dict[order[0]][1])
# if check != None:
#    for i_sym in pizza_dict[order[0]]:
#        print(i_sym, " i_sym")
#        if order[1] == i_sym:
#            pizza_dict[order[0]][1] = str(int(pizza_dict[order[0]][1]) + int(order[2]))
#            break
#    else:
#        pizza_dict[order[0]] = [values for values in pizza_dict.get(f"{order[0]}")], [order[1], order[2]]
# else:
#    pizza_dict[order[0]] = [order[1], order[2]]
# print(check)
# print(pizza_dict)
# print(pizza_dict)