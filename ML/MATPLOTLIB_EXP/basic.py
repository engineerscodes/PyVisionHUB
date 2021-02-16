
import  matplotlib.pyplot as plt

x =[i for i in range(100)]
y=[2*i for i in range(100)]

print(f"x ={x} \n y = {y} ")

plt.plot(x,y)
plt.show()

y=[i*i for i in range(10) ]
plt.scatter(x[:10],y)  # y and x must be of same size
plt.xlabel(" x-axis")
plt.ylabel('y-axis')
plt.show()