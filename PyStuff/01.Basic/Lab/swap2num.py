print("Swap two Number's ")

x, y = [int(x) for x in input("Enter two Number's: ").split()]
print(f"the Number before swap are x={x},y={y}")
x,y=y,x
print(f"The Number After the swapping x={x},y={y}")