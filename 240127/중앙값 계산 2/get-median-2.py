n = int(input())
a = list(map(int, input().split()))

for index, number in enumerate(a):
    if (index+1)%2 == 1:
        _temp = a[:index+1]
        _temp.sort()
        median = _temp[len(_temp)//2] if len(_temp)%2 == 1 else (_temp[len(_temp)//2-1]+_temp[len(_temp)//2])/2
        print(median, end=' ')