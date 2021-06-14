ip_address = []
for ip in range(4):
    ip_num = int(input(f"Введите {ip + 1} часть Ip adress: "))
    while ip_num > 255:
        ip_num = int(input(f"Введите {ip + 1} часть < 255: "))
    ip_address.append(ip_num)
ip_home = "{0}.{1}.{2}.{3}".format(
    ip_address[0],
    ip_address[1],
    ip_address[2],
    ip_address[3],
)
print("Ip_address:", ip_home)