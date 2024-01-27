n = int(input())
a = list(map(int, input().split()))

for num, i in enumerate(a):
    if i%2 == 1:
        _temp = a[:num+1]
        print(_temp[len(_temp)//2 if len(_temp)%2 == 1 else len(_temp)//2-1], end=' ')