import matplotlib.pyplot as plt

x = [2, 4, 6, 8, 10]
y = [5, 1, 7 , 8, 3]

x2 = [1, 3, 5, 7, 9]
y2 = [7, 2, 3 ,1 ,4]

plt.bar(x, y, label = "BAR-1" )
plt.bar(x2, y2, label = "BAR-2")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Graph Below")

plt.legend()
plt.show()