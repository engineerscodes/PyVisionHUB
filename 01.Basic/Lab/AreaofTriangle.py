
print("AREA OF TRIANGLE ")
print("Enter the Sides of Triangle (a,b,c)")
try :
 x,y,z=input("ENTER THE VALUES OF X,Y,Z ").split() #split my space
except Exception as e:
    print(e)
    exit(0)

print(f"X={x}\nY={y}\nZ={z}")
x=int(x)
y=int(y)
z=int(z)
s=(x+y+z)/2

print(f"Semi-perimeter={s}")
area = (s*(s-x)*(s-y)*(s-z)) ** 0.5

print(f"Area of given triangle with sides ({x},{y},{z}) is : {area}")

