n,m = map(int,input().split())
a = list(map(int,input().split()))
arr = [list(map(int,input().split())) for _ in range(m)]


for i in arr:
    print(sum(a[ i[0]-1:i[1] ]))