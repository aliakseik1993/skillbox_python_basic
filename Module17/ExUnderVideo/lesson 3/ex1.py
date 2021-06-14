import random
# original_prices = [-12, 3, 5, -2, 1]
original_prices = [random.randint(-100, 100) for _ in range(5)]
new_prices = original_prices[:]

for i in range(len(original_prices)):
    if new_prices[i] < 0:
        new_prices[i] = 0
print("Список", original_prices)
print("Мы потеряли: ",  sum(original_prices) - sum(new_prices))