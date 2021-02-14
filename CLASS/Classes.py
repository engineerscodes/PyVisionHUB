
class  Coorid:

    def poitns(self):
        print("Points")
    def draw(self):
        print("DRAW")


coorid =Coorid()
coorid.draw()
coorid.x=10  #Object attributes can be added anywhere in Pyhton
coorid.y =100 #Object attributes can be added anywhere in Pyhton
print(coorid.x,coorid.y)

coorid2C=Coorid()

#print(coorid2C.x,coorid2C.y) because x and y are not defined for coorid2C
'''
raceback (most recent call last):
  File "C:/Users/HP/PycharmProjects/LearnPython/CLASS/Classes.py", line 17, in <module>
    print(coorid2C.x,coorid2C.y)
AttributeError: 'Coorid' object has no attribute 'x'
'''
#refernces Object
corREF=coorid
coorid.x=1
print(f" references {corREF.x}")
corREF.x=5000
print(coorid.x)

