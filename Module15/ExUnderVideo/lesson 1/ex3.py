working_right_now = int(input("Кол-во сотрудников в офисе: "))
id_right_now = []
for _ in range(working_right_now):
    id_input = int(input("ID сотрудника: "))
    id_right_now.append(id_input)
employee_to_searching = int(input("Какой ID ищем? "))
new_list = []

for number in id_right_now:
    if number == employee_to_searching:
        new_list = id_right_now
        #print("новый лист, потому что равен", new_list)
        break
    else:
        new_list.append(employee_to_searching)
    #print(id_right_now)
    #print(new_list)

if new_list == id_right_now:
    print("Сотрудник на месте")
else:
    print("Сотрудник не работает")