count_packets = int(input("Введите колличество пакетов? "))
main_base = []
base = []
bad = 0
for i_pack in range(count_packets):
    print("Пакет номер", i_pack + 1)
    for bit in range(4):
        pack_input = int(input(f"{bit + 1} бит: "))
        base.append(pack_input)
    if base.count(-1) > 1:
        bad += 1
        print("Очень много Ошибок!")
    else:
        main_base.extend(base)
    base = []
print("Полученное сообщение: ", main_base)
print("Кол-во ошибок в сообщении:", main_base.count(-1))
print("Кол-во потерянных пакетов: ", bad)