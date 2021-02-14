
'''
Technically both self and this are used for the same thing.
They are used to access the variable associated with the current instance. Only difference is,
you have to include self explicitly as first parameter to an instance method in Python,
whereas this is not the case with Java.
'''

class Point :

      def __init__(self,x,y,): #constructor init=short hand for initialization
          self.x=x
          self.y=y
        #  return x,y #TypeError: __init__() should return None, not 'tuple'
      def move(self) :
          print("Move")

point =Point(x=100,y=20)
print(f" x :{point.x} y:{point.y}")

