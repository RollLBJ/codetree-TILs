n = int(input())

result = [[0]*n for _ in range(n)]

for i in range(1,n):
    for j in range(1,n):
        if j<=i:
            result[i][j] = result[i-1][j-1] + result[i-1][j]



for i in range(n):
    for j in range(n):
        if j<i:
            print(result[i][j], end=' ')
        elif j==i:
            print(1, end=' ')
    print()