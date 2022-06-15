
def prime(n):
    prime=0
    value=False
    for i in range(1, (n+1)):
        if n%i==0:
            prime+=1
    if prime==2:
        value=True
    if value:
        print(n)

def calculator(m):
    for i in range(1, m):
        prime(i)


calculator(100)

                    
        

    
