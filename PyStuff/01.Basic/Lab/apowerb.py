try:
    a=int(input("Enter the number A:"))
    b=int(input("Enter the number B:"))

    print(f" a^b :({str(a)+'^'+str(b)}) is --->:{a**b}")

except Exception as e:
    print(e)