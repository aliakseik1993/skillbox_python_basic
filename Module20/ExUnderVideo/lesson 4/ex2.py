

nums_1.discard(min(nums_1))
nums_2.discard(min(nums_2))

print(nums_1)
print(nums_2)

nums_1.add(random.randint(100, 200))
nums_2.add(random.randint(100, 200))

print(nums_1)
print(nums_2)

unity_set = nums_1.union(nums_2)
print("Объединение множеств: ", sorted(unity_set))
print("Пересечение множеств: ", nums_1.intersection(nums_2))
print("Элементы, входящие в nums_2, но не входящие в nums_1:  ", nums_2 - nums_1)
print("Элементы, входящие в nums_2, но не входящие в nums_1:  ", nums_2.difference(nums_1))