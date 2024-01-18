n, m = map(int,input().split())

num=0
for i in range(n):
    for j in range(m):
        num+=1
        print(num, end=' ')
    print()