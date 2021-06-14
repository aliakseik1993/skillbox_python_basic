phonebook = dict()
while True:
    contact = input("Введите имя, фамилию и телефон через пробел, или слово закрыть ").split()
    if contact == ["закрыть"]:
        print("Текущий словарь контактов:\n", phonebook)
        break
    while len(contact) != 3:
        contact = input("Введите имя, фамилию и телефон через пробел, или слово закрыть ").split()
    name_and_lname = (contact[0], contact[1])
    if name_and_lname in phonebook.keys():
        print("Такой человек уже есть")
    else:

        phone = int(contact[2])
        phonebook[name_and_lname] = phone
    print("Текущий словарь контактов:\n", phonebook)