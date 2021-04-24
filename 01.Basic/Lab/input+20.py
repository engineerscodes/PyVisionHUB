try:
    print("Enter the 20 input Number to get summary")
    num=[]
    for i in range(0, 20):
        temp = int(input())
        num.append(temp)
    print(f"List with Number's : {num}\nlength :{len(num)}")
    count_p=0
    count_n=0
    count_odd=0
    count_even=0
    count_zero=0
    for i in num:
        if i>0:
            count_p+=1
        if i<0:
            count_n+=1
        if i==0:
            count_zero+=1
        if i%2==0:
            count_even+=1
        if i%2!=0:
            count_odd+=1
    print(f"Summary About List of 20 Number Entered\nnumber of positive numbers :{count_p}\nnumber of negative numbers :{count_n}\n"
          f"number of odd numbers :{count_odd}\nnumber of even numbers :{count_even}\nnumber of Zero's :{count_zero}")
except Exception as E:
    print(E)