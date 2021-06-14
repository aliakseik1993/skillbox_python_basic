def back_number(number,):
    result_right = ""
    flag = False
    for x in str(number):
        if flag == True:
            result_right = x + result_right
        if x == ".":
            flag = True
        #print(result_right)
    number = int(number)
    #print("number", number)
    result_left = ""
    while number != 0:
        result_left += str(number % 10)
        number //= 10
    result = float(result_left + "." + result_right)
    return result

number_one_input = float(input("Введите первое число: "))
number_two_input = float(input("Введите второе число: "))
first_number = back_number(number_one_input)
second_number = back_number(number_two_input)

print("Первое число наоборот:", first_number)
print("Второе число наоборот:", second_number)
print("Сумма:", first_number + second_number)
