n = int(input())

result = [[1]*n for _ in range(n)]

for i in range(1,n):
    for j in range(1,n):
        if j<=i:
            result[i][j] = result[i-1][j-1] + result[i-1][j]
        else:
            result[i][j]=0



for i in range(n):
    for j in range(n):
        if j<=i:
            print(result[i][j], end=' ')
    print()