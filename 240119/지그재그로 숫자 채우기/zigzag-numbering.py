n , m= map(int,input().split())
result=[[0]*m for _ in range(n)]

cnt=0
for i in range(m): 
    for j in range(n):
        if i%2==0:
            result[j][i]=cnt
        else:
            result[n-1-j][i]=cnt

        cnt+=1

for row in result:
    for num in row:
        print(num, end=' ')
    print()