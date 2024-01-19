n , m= map(int,input().split())
result=[[0]*m for _ in range(n)]
cnt=1
x,y=0,0
for i in range(m+n-1):
    x,y=0,i
    if i>=m:
        x=i-m+1
        y=m-1    
    while(True):
        result[x][y]=cnt
        cnt+=1
        y-=1
        x+=1
        if y<0 or x>=n:
            break

for row in result:
    for num in row:
        print(num, end=' ')
    print()