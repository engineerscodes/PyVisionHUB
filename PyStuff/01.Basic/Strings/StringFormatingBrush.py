
name='M.NAVEEN'
types='Coder'

finals=name +' is ['+types+']'

print(finals)

#String Formatting

FrStr=f'{name} is pro {types} but stil noob fellow'
print(FrStr)

print(FrStr.upper())

#find char or sequence of characters

print(FrStr.find("N")) #return 2 index of char in string
#finds -1 is the char did not exit
print(FrStr.find("xxxxx")) #-1 is returned

#seq of Character

print(FrStr.find("NAVEEN")) #The index of Starting Letter

#replace

print(FrStr.replace("E","X")) #replace all E with X
print(FrStr.replace("M.NAVEEN","N.WICKET"))

#The (in keyword) is used to check if a value is present in a sequence (list, range, string etc.)

print("NAVEEN" in FrStr) #return's TRUE

print("nav" in FrStr) #return's False