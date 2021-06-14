student = input(
    "Введите информацию о студенте через пробел \n"
    "(имя, фамилия, город, место учёбы, оценки): "
)
student_list = student.split()
student_dict = dict()

student_dict["Имя"] = student_list[0]
student_dict["Фамилия"] = student_list[1]
student_dict["Город"] = student_list[2]
student_dict["Место учёбы"] = student_list[3]
student_dict["Оценки"] = []
for mark in student_list[4:]:
    student_dict["Оценки"].append(int(mark))

for i_info in student_dict:
    print(i_info, "-", student_dict[i_info])