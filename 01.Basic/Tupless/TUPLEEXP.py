num =(1,5,5,8,7,9,3)
print(num[0])
#TUPLE ARE NOT MUTTABLE CAN NOT CHANGE THE VALUE\
#num[2]=100
'''
    num[2]=100
TypeError: 'tuple' object does not support item assignment
'''

print(f"NUMBER OF 5 IN TUPLES  {num.count(5)}")


#Upacking

nums=(1,2,3)
'''
x=nums[0]
y=nums[1]
z=nums[2] or u can use x,y,z=nums (Shorthand for unpacking)'''

x,y,z =nums
print(f"x :{x } y :{y} z :{z}")







