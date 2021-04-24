
print("Enter 10 Number In List :")

num=[]

for i in range(0,10):
    temp=int(input())
    num.append(temp)

print(f"List with duplicates {num}")
none_dup_num=[]
for i in range(0,len(num)) :
    if num[i] not in none_dup_num:
        none_dup_num.append(num[i])

print(f"List with No duplicates {none_dup_num}")