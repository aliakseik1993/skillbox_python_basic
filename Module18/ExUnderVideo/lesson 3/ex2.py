path = input("Путь к файлу: ")
disk = input("На каком диске должен лежать файл: ")
file_extension = input("Требуемое расширение файла: ")
if path.endswith(file_extension) and path.startswith(disk):
    print("Путь корректен!")
else:
    print("Путь не корректный")