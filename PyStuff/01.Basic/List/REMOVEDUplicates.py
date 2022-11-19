
lists=[5,5,6,7,89,0,0,0,7,7,7,5,4,4,35,4,68]
print(type(lists))
print(f"List :{lists}")
newlist=[]
for i in lists :
    if  i  not in newlist :
        newlist.append(i)

print(f"List with no duplicates {newlist}")