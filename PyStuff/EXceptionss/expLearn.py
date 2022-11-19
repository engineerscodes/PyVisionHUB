

try :
     intputs=int(input("Enter the Number"))
     print(f"Number is : {intputs}")

except  :
    print("Invaild type entered")
try :
    intputs = int(input("Enter the Number"))
    print(f"Number is : {intputs}")
    intputs=intputs/0
except ArithmeticError :
    print("CATCHES ONLY ArithmeticError")
except ValueError :
    print("CATCHES ONLY VALUE ERROR")