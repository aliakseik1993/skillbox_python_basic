name = input("Имя: ")
number_order = input("Номер заказа: ")
print('Здравствуйте, {name_client}! Ваш номер заказа: {order}. Приятного дня!'.format
      (name_client=name,
       order=number_order
       ))

print('Здравствуйте, {0}! Ваш номер заказа: {1}. Приятного дня!'.format
      (name, number_order))