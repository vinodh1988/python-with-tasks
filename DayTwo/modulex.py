def formatprint(sno,name,city):
    return f"sno: {sno} name: {name} city: {city}"

def addN(*args):
    return sum(args)

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
def isprime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True