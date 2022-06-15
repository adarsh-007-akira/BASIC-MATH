def compound_intrest():
    principal=int(input("Principal Amount :\n"))
    rate=int(input("Rate of Intrest: \n"))
    n=int(input("Number of time per Year the Intrest is Compounded :\n"))
    time=int(input("Time in Years :\n"))

    amount=principal*(1+(rate/n))**(n*time)
    profit=amount-principal

    print(f"Total Amount - {amount}\nProfit - {profit}")


compound_intrest()

    
