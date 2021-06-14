def price(element):
    return float(input("Цена на товар: "))
def new_price(procent, price):
    return price * (1 + procent / 100)
price_list = [price(x) for x in range(5)]
x = int(input("Повышение на первый год: "))
y = int(input("Повышение на второй год: "))
price_first = [new_price(x, i_price) for i_price in price_list]
price_second = [new_price(y, i_price) for i_price in price_first]
print(price_first)
print("Сумма цен за каждый год:", round(sum(price_list) ,2), round(sum(price_first) ,2), round(sum(price_second) ,2) )