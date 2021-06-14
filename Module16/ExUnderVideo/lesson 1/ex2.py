cout_employes = int(input("Введите колличество сотрудников: "))
print("Колличество соотрудников: ", cout_employes)
salary_list = []
for salary in range(cout_employes):
    print(f"Зарплата {salary + 1} сотрудника:", end = " ")
    salary_employee = int(input())
    if salary_employee != 0:
        salary_list.append(salary_employee)
# for fired in salary_list:
#     print(salary_list)
#     if fired == 0:
#         salary_list.remove(fired)
#         print(salary_list)
print("Зарплата: ", salary_list)
print("Осталось сотрудников:", len(salary_list))
print("Максимальная ЗП = ", max(salary_list))
print("Минимальная ЗП = ", min(salary_list))