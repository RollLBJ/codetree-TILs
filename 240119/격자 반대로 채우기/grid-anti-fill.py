n= int(input())

result=[[0]*n for _ in range(n)]
cnt=1
flag = 1 if n%2==0 else 0
for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        if i%2==flag:
            result[j][i]=cnt
        else:
            result[n-1-j][i]=cnt
        cnt+=1


for row in result:
    for num in row:
        print(num, end=' ')
    print()