


def name (name) : # Parameter
    print(name)



name("cdrcrecrcrcrc") # arguments
name(r"c\naveen")
name(15)

from math import *

print(round(15.9000000000000000000000000000000000006))
print(ceil(15.90000000000000000000000000000000000006))

print(floor(15.9999))

  #covert  deg to rad
  #radians = degrees / 180.0 * math.pi
  #sin 45=
#print(sin(45/180*pi))


#Keyword Argument
def callme(firstname,lastname) :
    print(f" HI {firstname } {lastname} ")

callme(lastname="m",firstname="Naveen")

def callme2(firstname,lastname="JAMES") :
    print(f" HI {firstname } {lastname} ")

callme2(firstname="Naveen")

def callme3(firstname,lastname="Jammy wooo") :
    print(f" HI {firstname } {lastname} ")

#callme3(lastname="m","Naveen") #position argument must be before keyword arguments
callme3("Virat",lastname="Kohli") ##position argument must be before keyword arguments

print(callme3("Virat",lastname="Kohli"))  #by default all fuction return none
#return statement

def retSquare(num) :  #by default all fuction return none
    return num *num

print(retSquare(5))

sqr=retSquare(9)
print(sqr)


def retMultipleV (n,n2):
    return [n,n2] #return a list

lists=retMultipleV(100,"Naveen")
print(type(lists))


def retMultipleVTuple (n,n2):
    return n,n2 #return a Tuple

lists=retMultipleVTuple(100,"Naveen")
print(type(lists))