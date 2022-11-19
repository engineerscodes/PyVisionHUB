print("FIND THE SQUARE ROOT OF GIVEN NUMBER")

try :
    num=int(input("Enter the number "))
    print(f"Square root of a Number: {num} is -> {num**(1/2)}")
except Exception as e:
    print(e)


