
def Collatz_conjecture(a, n=0):

    # Limit case: a = 1
    if (a == 1) and (n != 3):          
        a = 3*a+1  
        n += 1
        print(a)
        return Collatz_conjecture(a,n)
        
    # Even number case
    elif ((a % 2) == 0) and (n != 3):  
        a /= 2
        print(a)
        return Collatz_conjecture(a,n)

    # Odd number case
    elif ((a % 2) == 1) and (n != 3):
        a = 3*a+1  
        print(a)
        return Collatz_conjecture(a,n)
        
    # Conjecture fulfilled
    else:
        print("Collatz's conjecture is fulfilled")

