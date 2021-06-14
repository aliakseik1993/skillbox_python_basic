contacts_book = dict()

while True:
    print("Текущие контакты на телефоне:")
    if len(contacts_book) == 0:
        print("<Пусто>")
    for key in contacts_book:
        print(f"{key} {contacts_book[key]}")
    name = input("Введите имя или сохранить список: ")
    if name == "сохранить список":
        break
    phone_number = int(input("Введите номер телефона:  "))
    contacts_book[name] = phone_number
