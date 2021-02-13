
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

REFList=LISTNAME
REFList[2]="NAVEEN"
print(f"REFERNCES List :{REFList}")

print(f"OLD REFERNCES List :{LISTNAME}")
