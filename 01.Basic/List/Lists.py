
LISTNAME =["JED ","FRF","FRFE","XED"]

for i in LISTNAME :
    print(i,end=" ")
print()

print("Direct :",LISTNAME[1:3]) #last index is not printed
print(LISTNAME)

newList =LISTNAME[:] #return's a new List #WITHOUT REFERNCES (COPY WITHOUT REFERNCES)
print(newList)
newList[0]="James"
print("new List",newList)
print("Old List",LISTNAME)

#copy list without refernces
newList=LISTNAME.copy()
print(f"new LSIT WITH COPY {newList}")

REFList=LISTNAME
REFList[2]="NAVEEN"
print(f"REFERNCES List :{REFList}")

print(f"OLD REFERNCES List :{LISTNAME}")


#2D LISTS
matrix =[
    [1,2,3],
    [4,5,6,7],
    [0,9,8]
]

print(matrix)
print("1c to 2c")
print(matrix[1:3])
#access each items

print(matrix[1][3]) #7

#List Method

listss=list(range(0,100,10))
print(type(listss))
#adding new values
listss.append(500)
print(listss)
#insert and position
listss.insert(0,9) #if pos is greater than > len of list the it will add to the end
print(listss)

#remove
listss.remove(50)
print(listss)
#remove from end
listss.pop()
print(listss)

#find index of first occurences
print(listss.index(20)) #if element is not present then throws error

#count
listss.append(20)
print(f"NUmber of 2's in list {listss.count(20)}")

#sorting list
listss.sort()
print(listss)
#display number in reverse
listss.reverse()
print(f"REVERSE LIST :{listss}")
#remove all
listss.clear()
print(listss)




















