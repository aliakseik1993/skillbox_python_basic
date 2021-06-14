goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
new_fruit = []

new_var = input("Новый фрукт: ")
new_price = int(input("Цена: "))
new_fruit.insert(5, new_var)
new_fruit.insert(5, new_price)

print("Текущий ассортимент:", goods)
goods.append(new_fruit)

print("Новый ассортимент: ", goods)

for price in range(6):
    goods[price][1] += (goods[price][1] * 8 / 100)

print("Новый ассортимент с увел. ценой:  ", goods)