small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}



big_storage = {
    'доски': 1000,
    'балки': 150,
    'рейки': 600
}
big_storage.update(small_storage)
print(big_storage)
name_product = input("Введите название товара: ")
print("{0} - {1}".format(name_product, big_storage.get(name_product)))