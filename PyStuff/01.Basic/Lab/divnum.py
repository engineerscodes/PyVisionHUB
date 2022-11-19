print("Python Program to Find Numbers Divisible by Another Number")
try:

   num=int(input("Enter the number :"))
   div=[]
   if num>0:
       for i in range(1,101): #other number till 1-100
           if num % i==0 and i!=num:
               div.append(i)
       print(f"list of Divisors of number :{num} is :{div} ")

except Exception as e:
    print(e)