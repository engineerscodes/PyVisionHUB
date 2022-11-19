import matplotlib.pyplot as plt

data = [18,55,21,25,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]

# ids = [x for x in range(len(ages))]

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(data, bins, histtype='bar' , rwidth=0.8 )

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Graph Below")

plt.show()