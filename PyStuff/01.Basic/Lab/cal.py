print("Simple Calculator")


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def div(num1, num2):
    return num1 / num2


def multiply(num1, num2):
    return num1 * num2


while 1:
    print("1)Add \n2)Sub \n3)Divide \n4)Multiply \n5)Exit")
    try:
        choice=input("Enter choice :")
        if choice!="5" :
            num1=int(input("Enter number1 :"))
            num2=int(input("Enter number2 :"))
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=",sub(num1, num2))

        elif choice == '3':
            print(num1, "/", num2, "=", div(num1, num2))

        elif choice == '4':
            print(num1, "*", num2, "=", multiply(num1, num2))


        elif choice=='5':
            print("Bye----Bye")
            exit(0)
        else :
             print("Invalid choice")
    except Exception as e:
        print(e)