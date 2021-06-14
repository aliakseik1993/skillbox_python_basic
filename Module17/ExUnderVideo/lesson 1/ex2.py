string_input = input("Введите строку: ")
add_symbol = input("Введите символ: ")
list = [x * 2 for x in string_input]
print("Список удвоенных символов:", list)
list_new = [x + add_symbol for x in list]
print("Склейка с дополнительным символом: ", list_new)