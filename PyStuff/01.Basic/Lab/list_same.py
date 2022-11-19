try :
    print("Enter a list L1")
    l1=[int(i) for i in input("EG :2, 3 ,15--->:").split(",")]



    print("Enter a list L2")
    l2=[int(i) for i in input("EG : 15 3 2 --->:").split(",")]

    if len(l1) == len(l2):
        if(l1==l2) :
            print("same list without reverseing")
            print(f"L1 :{l1}\nL2 :{l2}")
            exit(0)
        l2.reverse()
        if  l2==l1:
            print("same list After reverseing")
            print(f"L1 :{l1}\nL2 :{l2}")
            exit(0)
        else :
            print("Not same List ")
            print(f"L1 :{l1}\nL2 :{l2}")
    else:
        print("Not same List ")
        print(f"L1 :{l1}\nL2 :{l2}")
except Exception as e:
    print(e)







