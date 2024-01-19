result=[[1]*5 for _ in range(5)]


for i in range(1,5):
    for j in range(1,5):
        result[i][j] = result[i-1][j]+result[i][j-1]


for row in result:
    for num in row:
        print(num, end=' ')
    print()