a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

cnt=0
for t in [a,b,c]:
    if t[0] == 'Y' and t[1]>=37:
        cnt+=1
if cnt>=2:
    print("E")
else:
    print("N")