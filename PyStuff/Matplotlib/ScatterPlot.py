import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
sleeping = [7, 8, 6, 11, 10]
Gaming = [2, 3, 4, 1, 4]
studing = [7, 3, 8, 3, 1]
playing = [8, 3, 2, 6, 13]

# This block is only to make legends, as ScatterPlot does not support it.
plt.plot([], [], color = 'm', label = "sleeping", linewidth = 5)
plt.plot([], [], color = 'c', label = "Gaming", linewidth = 5)
plt.plot([], [], color = 'r', label = "studing",  linewidth = 5)
plt.plot([], [], color = 'k', label = "playing",  linewidth = 5)


plt.stackplot(days, sleeping,Gaming,studing,playing, colors=['m', 'c', 'r', 'k'])

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Graph Below")
plt.legend()
plt.show()

