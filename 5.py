def prime(n):
    prime=0
    value=False
    for i in range(1, (n+1)):
        if n%i==0:
            prime+=1
    if prime==2:
        value=True
    if value:
        print(f"{n} is  a PRIME number.")

    elif value>2:
        print(f"{n} is NOT a PRIME number.")

prime(7)