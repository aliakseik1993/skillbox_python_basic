while True:
    template = input("Введи шаблон поздравления используя конструкции {age} и {name}: ")
    if "{age}" in template and "{name}" in template:
        break
    print("В шаблоне меньше 2-ух конструкций")


name_list = input("Введите имя и фамилию, отделяю от следующей пары ,: ").split(", ")
age_str = input(("Введите возраст через пробел: "))
age = [int(number) for number in age_str.split()]
print(age, "возраст")

for i_man in range(len(name_list)):
    print(template.format(name=name_list[i_man], age=age[i_man]))

people = [" ".join([name_list[i_man], str(age[i_man])])
          for i_man in range(len(name_list))
          ]
print(people, "список people")
print("\nИменники:", end = " ")
print(", ".join(people))
