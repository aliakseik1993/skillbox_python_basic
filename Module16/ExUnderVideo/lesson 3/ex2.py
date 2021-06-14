n = int(input("Колличество участников? "))
members_list = []
k = int(input("Введите колличество человек в группе? "))
start = 1
print(n % k, "n / k")
while n % k != 0:
    k = int(input("Введите число кратное к? "))
for i_sportsmens in range(n // k):
    members_list.append(list(range(start, start + k)))
    start += k
print(members_list)