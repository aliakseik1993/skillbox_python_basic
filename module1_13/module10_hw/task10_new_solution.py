num = int(input('Высота пирамиды: '))
count = 0
pre_count = ""
for i in range(1, num+1):
  for j in range (1):
    pre_count += str(num - count)
    print (pre_count, end = "")
    count += 1
  for j in range((num-i) * 2): 
    print('.', end='')
  a = ""
  a = a + pre_count
  print (a, end = "")
  print()