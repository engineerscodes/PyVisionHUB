print("Sum of natural Number")
sum=0
try:
  num=int(input("Enter the number :"))
  if num>=1:
      for i in range(1, num + 1):
          sum =sum+ i
      print(f"Sum  of Natural number :{num} is ->{sum}")
  else:
      print("Not Natural Number")

except Exception as e:
    print(e)