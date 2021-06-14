x = 7
for i in range (1, x):
  a = (x - (2 ** i - 1))
  b = (x - (2 ** i))
  if i == 1:
    summ_1 = a
    summ_2 = b
  if i > 1:
    summ_1 *= a
    summ_2 *= b
print("Результат выражения из примера =", summ_1 / summ_2)
#при значение x = 7, повторяется выражение из примера, правда в числителе в одних скобках получается 0 и поэтому при делении на 0, получается результат 0

xc = int(input("Введите число: "))
for i in range (1, xc):
  c = (xc - (2 ** i -1))
  y = (xc - (2 ** i ))
  #print(y)
  if i == 1:
    summ_3 = c
    summ_4 = y
  if i > 1:
    summ_3 *= c
    summ_4 *= y
  if c == 0 or y == 0:
    print("Введите другое число, а иначе результат будет равен 0")
    break
#print(summ_3)
#print(summ_4)
print("Результат выражения", summ_3 / summ_4)