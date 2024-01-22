n,m = map(int,input().split())

def lcm(a,b):
    return a*b//gcd(a,b)

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

print(lcm(n,m))