import math 

def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def findPrimes(n):
    return[i for i in range(2,n) if isPrime(i)]



print(findPrimes(20))