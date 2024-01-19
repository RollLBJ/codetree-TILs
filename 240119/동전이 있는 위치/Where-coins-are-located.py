n,m = map(int, input().split())

arr = [list(map(int,input().split())) for _ in range(m)]
mat = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        _flag=0
        for k in arr:
            if k[0]-1==i and k[1]-1==j:
                _flag=1
        if _flag:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()