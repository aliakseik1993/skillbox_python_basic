#Способ №1
number_kin = int(input("Введите количество человек: "))
kin_level = dict()
main_kin_1 = dict()

for i in range(number_kin - 1):
    parent, kin = input(f"{i + 1} пара: ").split()
    main_kin_1[parent] = kin
    kin_level[parent] = 0
    kin_level[kin] = 0
print(main_kin_1)
for i_kin in main_kin_1:
    one_of_parent = i_kin
    print(one_of_parent, "one_of_parent")
    while one_of_parent in main_kin_1:
        one_of_parent = main_kin_1[one_of_parent]
        kin_level[i_kin] += 1
        print(kin_level)

for i_kin in sorted(kin_level):
    print(i_kin, kin_level[i_kin])

#Cпособ №2
def height(person):
    if person not in main_kin:
        return 0
    else:
        print(person)
        print(height(main_kin[person]), "height(main_kin[person])")
        return 1 + height(main_kin[person])


main_kin = dict()
number_kin = int(input("Введите количество человек: "))

for kin in range(number_kin - 1):
    print(f"{kin + 1} пара: ", end = "")
    kin_list = input().split()
    main_kin.update({kin_list[0]:kin_list[1]})

# alex_set = set(main_kin.keys()).union(set(main_kin.values()))
# print(alex_set, "set")
heights = {}
for person in set(main_kin.keys()).union(set(main_kin.values())):
    heights[person] = height(person)

for key, value in sorted(heights.items()):
    print(key, value)





# main_kin = {'Alexei': 'Peter_I', 'Anna': 'Peter_I', 'Elizabeth': 'Peter_I', 'Peter_II': 'Alexei'}
# # print(main_kin)
# parent_main = ""
# for parent in main_kin.values():
#     # print(parent)
#     if parent not in main_kin.keys():
#         parent_main = parent
# # print(parent_main)
# main_kin.update({parent_main: int(0)})
# print(main_kin)
# hight = 0
# for descendant in main_kin.keys():
#     print(descendant, "desc")
#     while True:
#         if main_kin[descendant] ==
#         main_kin.update({descendant: main_kin[descendant]})
#
#         print(main_kin)
#     else:
#         break

# for i_kin in main_kin:
#     if main_kin[i_kin] == 0:
#         print(i_kin, "равное инт")
#         for re in main_kin.keys():
#             print(re, "re")
#             if main_kin[re] == i_kin:
#                 print(main_kin[re], "main_kin re")
#                 print(main_kin[i_kin], "znachenie")
#                 main_kin.update({re: main_kin[i_kin] + 1})
# print(main_kin)

