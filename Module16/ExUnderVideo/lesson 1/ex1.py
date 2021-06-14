zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
zoo.insert(1, "bear")
zoo.remove("elephant")
print("Зоопарк:", zoo)
print("Лев сидит в клетке номер", zoo.index("lion") + 1)
print("Обезьяна сидит в клетке номер", zoo.index('monkey') + 1)