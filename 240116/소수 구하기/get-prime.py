def isPrime(n):
    for i in range(2,int(n/2)):
        if n%i==0:
            return 0
    return 1

n = int(input())

for i in range(2,n+1):
    if isPrime(i):
        print(i, end = " ")