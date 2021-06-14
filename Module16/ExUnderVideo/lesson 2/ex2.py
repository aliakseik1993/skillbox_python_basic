first_message = input("Первое сообщение: ")
second_message = input("Второе сообщение: ")
if len(first_message) == len(second_message):
    print("Ой!")
elif len(first_message) > len(second_message):
    print("Третье сообщение", first_message + second_message)
else:
    print("Третье сообщение ", second_message + " " + first_message)