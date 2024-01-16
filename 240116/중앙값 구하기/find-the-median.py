a = list(map(int,input().split()))

for i in a:
    if i!=max(a) and i!=min(a):
        print(i)