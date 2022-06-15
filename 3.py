def armstrong():
    num=input("What is the Number :\n")

    lst=[]

    lst=list(num)

    result = 0

    for i in range(len(lst)):
        lst[i]=int(lst[i])

        result+=(lst[i]**3)

    if str(result)==num:
        print("It is  an Armstrong Number\n")

    else:
        print("It is not an Armstrong Number\n")


armstrong()
