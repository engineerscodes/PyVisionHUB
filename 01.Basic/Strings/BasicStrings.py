
names="Naveen"
k='naveen'
ks="naveen's"
kss='hello\'s'

print(kss)

print(r'naveen\'s')

#multiple line String

multipleStr ='''
  i am a noob Fellow
praveen is pro
bala is Super Key
       I am Virat Fan

'''

print(multipleStr)

multipleStr ="""
call me Nav
   MR . NAV
   
"""


print(multipleStr)

arrayString ='WANDAVISION'

print(arrayString[0],arrayString[-1])

for i in arrayString :
    print(i)

len=  len(arrayString)
print(len)
for i in range(-1,-len-1,-1) :
    print(arrayString[i],end="")

print("\nDirect Print",arrayString)

print(arrayString[0:len:2])


print(arrayString[0:])

copy=arrayString
copy="jbhfgrfe"
print(arrayString,"String is not reference in python")


print(copy[1:-1])