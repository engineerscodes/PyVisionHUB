
import  random

Number=random.randint(1,10)
print("GUESS NUMBER 1-10 ONLY 3 LIFE'S")
i=1
while i <=3 :
    guess=int(input("ENTER THE NUMBER"))
    if guess==Number :
        print("GOD LUCK !!!!!")
        exit(0)
    print(f"life Left {3-i}")
    i=i+1
print("RIP")
