import matplotlib.pyplot as plt

size = [1700, 2100, 1900, 1300, 1600, 2200]
price = [53000, 44000, 59000, 82000, 50000, 68000]

size_vars, price_vars = zip(*sorted(zip(size,price)))
size, price = list(size_vars), list(price_vars)
# plt.plot(size,price) # you can do a scatterplot or a linear graph.
plt.scatter(size, price)
plt.show()
