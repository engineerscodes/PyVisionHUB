print("Find the factorial of a number")
fact=1
try :
    num=int(input("Enter a Number :"))
    if num >=1:
        for i in range(1,num+1):
            fact=fact*i
        print(f"Factorial of number :{num} is ->{fact}")
    if num ==0:
        print(f"Factorial of number :{num} is ->{fact}")
    else :
        print("Sorry, factorial does not exist for negative numbers")

except Exception as e:
    print(e)