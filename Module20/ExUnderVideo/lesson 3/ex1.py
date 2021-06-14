incomes = {
'apple': 5600.20,

'orange': 3500.45,

'banana': 5000.00,

'bergamot': 3700.56,

'durian': 5987.23,

'peach': 10000.50,

'pear': 1020.00,

'persimmon': 310.00,
}

for key, values in incomes.items():
    print("{key} -- {values}".format(
        key=key,
        values=values
    ))