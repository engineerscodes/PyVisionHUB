import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [5, 7, 4]

x2 = [1, 2, 3] 
y2 = [10, 14, 12]

plt.plot (x, y, label="FIRST LINE")
plt.plot (x2, y2, label="SECOND LINE")
plt.xlabel("PLOT NUMBER")
plt.ylabel("Important Bar")
plt.title("Graph")

plt.legend()
plt.show ()