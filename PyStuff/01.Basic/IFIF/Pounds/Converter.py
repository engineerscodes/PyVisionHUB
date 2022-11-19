
inputswg=float(input("Enter the Weight :"))
inputs =input("Enter the Units KG(K) OR POUND(L) ")
output=0
outunit=""
if inputs.lower()=="k" :
    output=2.20462*inputswg
    outunit="pounds"
else :
    output=float(1/2.20462)*float(inputswg)
    outunit="KG"
print(f"YOU ARE {round(output)} {outunit}")
