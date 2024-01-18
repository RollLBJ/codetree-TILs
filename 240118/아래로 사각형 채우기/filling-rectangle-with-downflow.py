n = int(input())
result=[[0]*n for _ in range(n)]
# print(result)
cnt=0
for i in range(n):
    for j in range(n):
        cnt+=1
        result[j][i]=cnt

for row in result:
    for n in row:
        print(n, end=' ')
    print()